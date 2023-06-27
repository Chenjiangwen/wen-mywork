import numpy as np
from scipy.optimize import optimize
import re

input_configs = [
        {
            'func': "min=2*x_1^2+4*x_2^2-4*x_1*x_2-6*x_1-3*x_2",
            'initial_point': (1, 0),
            'cons': ['3-x_1-x_2>=0', '9-4*x_1-x_2>=0', 'x_1>=0', 'x_2>=0'],
            # 'cons': ['x_1+x_2-3<=0', '4*x_1+x_2-9<=0', '-x_1<=0', '-x_2<=0'],
            'tol': 0.001
        },
        {
            'func': "min=3/2*x_1^2+1/2*x_2^2-x_1*x_2-2*x_1",
            'initial_point': (3, 0),
            # 'cons': ['x_1>=2', 'x_2>=0'],
            'cons': ['2-x_1<=0', '-x_2<=0'],
            'tol': 0.001
        },
        {
            'func': "min=x_1^2+25*x_2^2",
            'initial_point': (1, 0),
            'cons': ['x_1+x_2>=1'],
            'tol': 0.001
        },
        {
            'func': "min=x_1^2+x_2^2-4*x_1-4*x_2+8",
            'initial_point': (1, 0),
            'cons': ['x_1+2*x_2<=4'],
            'tol': 0.001
        },
        {
            'func': "min=x_1^2+2*x_2^2+0.3*x_1*x_2-98*x_1-277*x_2",
            'initial_point': (0, 1),
            'cons': ['x_1+x_2<=100', 'x_1-2*x_2<=0', 'x_1>=0', 'x_2>=0'],
            'tol': 0.001
        }
    ]

results = []
for config in input_configs:
    # 提取问题参数
    obj_func = config['func']
    initial_point = config['initial_point']
    constraints = config['cons']
    tolerance = config['tol']

    # 提取目标函数的系数及常数项
    c_idx = max(obj_func.find('x_1'), obj_func.find('x_2'))
    c_str = obj_func[obj_func.find('=', c_idx) + 1:]
    c_parts = re.findall(r'(-?\d+(?:\.\d+)?)\*(x_1|x_2)\^(\d+)', c_str)
    c = [0, 0]
    for part in c_parts:
        coeff = float(part[0])
        var_idx = int(part[2])
        if part[1] == 'x_1':
            c[0] += coeff
        else:
            c[1] += coeff

    # 提取约束条件的系数及常数项
    A_ub, b_ub = [], []
    for constraint in constraints:
        constraint = constraint.replace('<=', '>=')
        constraint = constraint.replace('>=', '<=')
        constraints_split = constraint.split('=')
        constraint_vars = constraints_split[0].strip().split(' ')

        constraint_coefficients = []
        for var in constraint_vars:
            if var[-3:] == 'x_1':
                var_idx = 0
            else:
                var_idx = 1
            coeff_parts = re.findall(r'(-?\d+(?:\.\d+)?)\*{}(\^\d+)?'.format(var[:-3]), var)
            coeff = float(coeff_parts[0][0])
            constraint_coefficients.append(coeff)

        constraint_coefficients = [float(constraints_split[1])] + constraint_coefficients
        A_ub.append(constraint_coefficients[1:])
        b_ub.append(-constraint_coefficients[0])

    # 设置变量边界
    bounds = [(0, None), (0, None)]

    # 执行线性规划
    result = optimize.linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method='highs', tol=tolerance, options={'maxiter': 1000})
    results.append(result)
