import numpy as np

def f(x):
    return 100 * (x[1] - x[0]**2)**2 + (1 - x[0])**2

def grad_f(x):
    df_dx = -400 * x[0] * (x[1] - x[0]**2) - 2 * (1 - x[0])
    df_dy = 200 * (x[1] - x[0]**2)
    return np.array([df_dx, df_dy])

def hessian_f(x):
    d2f_dx2 = -400 * x[1] + 1200 * x[0]**2 + 2
    d2f_dxdy = -400 * x[0]
    d2f_dydx = -400 * x[0]
    d2f_dy2 = 200
    return np.array([[d2f_dx2, d2f_dxdy], [d2f_dydx, d2f_dy2]])

x0 = np.array([-1.2, 1])
x = x0
tolerance = 1e-6
k = 0

while np.linalg.norm(grad_f(x)) > tolerance:
    print(f"Iteration {k}: x({k}) = {x}")
    h_inv = np.linalg.inv(hessian_f(x))
    x = x - h_inv.dot(grad_f(x))
    k += 1

print(f"Final Iteration {k}: x({k}) = {x}")
