import scipy.optimize as optimize

c = [2, 4]  # 目标函数的系数
A_ub = [[-1, -1], [-4, -1]]  # 不等式约束的系数矩阵
b_ub = [-3, -9]  # 不等式约束的右侧常数向量
bounds = [(0, None), (0, None)]  # 变量的边界条件，表示 x₁ 和 x₂ 都为非负数

result = optimize.linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds)

if result.success:
    print("最优解:")
    print("x₁ =", result.x[0])
    print("x₂ =", result.x[1])
    print("目标函数的最小值:", result.fun)
else:
    print("求解失败:", result.message)


import numpy as np
from scipy.optimize import minimize

def objective(x):
    # 定义目标函数
    return 2 * x[0]**2 + 4 * x[1]**2 - 4 * x[0] * x[1] - 6 * x[0] - 3 * x[1]

def constraint1(x):
    # 定义第一个约束条件
    return 3 - x[0] - x[1]

def constraint2(x):
    # 定义第二个约束条件
    return 9 - 4 * x[0] - x[1]

# 定义初始点和容差
x0 = [1, 0]
tol = 0.001

# 定义约束条件字典
cons = ({'type': 'ineq', 'fun': constraint1},
        {'type': 'ineq', 'fun': constraint2})

# 使用拟牛顿法进行优化
result = minimize(objective, x0, method='SLSQP', tol=tol, constraints=cons)

print("优化结果:")
print("最小值:", result.fun)
print("最优解:", result.x)
