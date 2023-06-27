import numpy as np
from scipy.optimize import minimize

def algorithm(input_config):
    constraints = []
    for c in input_config['cons']:
        c = c.replace('x_1', '-x[0]').replace('x_2', '-x[1]')
        if ">=" in c:
            equation = c.replace(">=", "+(") + ")"
            constraints.append({'type': 'ineq', 'fun': lambda x, eq=equation: -eval(eq)})
        elif "<=" in c:
            equation = c.replace("<=", "+(") + ")"
            constraints.append({'type': 'ineq', 'fun': lambda x, eq=equation: eval(eq)})
        else:
            raise ValueError(
                "Invalid constraint format. Constraints should be in the format: 'expression>=0' or 'expression<=0'.")

    def objective_function(variables):
        x1, x2 = variables
        func_str = input_config['func'].replace('min=', '').replace('^', '**').replace('x_1', 'x1').replace('x_2','x2')
        return eval(func_str, {'x1': x1, 'x2': x2})

    initial_point = input_config['initial_point']

    result = minimize(objective_function, initial_point, constraints=constraints , tol=input_config['tol'])

    obj = result.fun
    res = result.xz

    return obj, res


if __name__ == "__main__":
    input_configs = [
        {
            'func': "min=2*x_1^2+4*x_2^2-4*x_1*x_2-6*x_1-3*x_2",
            'initial_point': (1, 0),
            'cons': ['3-x_1-x_2>=0', '9-4*x_1-x_2>=0', 'x_1>=0', 'x_2>=0'],
            'tol': 0.001
        },
        {
            'func': "min=3/2*x_1^2+1/2*x_2^2-x_1*x_2-2*x_1",
            'initial_point': (3, 0),
            'cons': ['x_1>=2', 'x_2>=0'],
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
    for i, input_config in enumerate(input_configs):
        obj, res = algorithm(input_config)
        print('Q{}:'.format(i+1))
        print('obj : ', obj)
        print('res : ', res)
