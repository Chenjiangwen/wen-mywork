# import numpy as np
# import matplotlib.pyplot as plt
# from mpl_toolkits.mplot3d import Axes3D
#
# def f(x, y):
#     return 100 * (y - x**2)**2 + (1 - x)**2
#
# # Create grid coordinates for x and y
# x = np.linspace(-2, 2, 100)
# y = np.linspace(-1, 3, 100)
# X, Y = np.meshgrid(x, y)
#
# # Compute the values of f(x, y) for all grid points
# Z = f(X, Y)
#
# # Create a 3D plot
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(X, Y, Z, cmap='viridis')
#
# # Set labels and title
# ax.set_xlabel('x')
# ax.set_ylabel('y')
# ax.set_zlabel('f(x, y)')
# ax.set_title('3D Plot of f(x, y)')
#
# # Show the plot
# plt.savefig('pic/q3_b.png')
# plt.show()
#
# # Compute the gradient of f(x, y)
# grad_x = -400 * X * (Y - X**2) - 2 * (1 - X)
# grad_y = 200 * (Y - X**2)
#
# # Compute the Hessian matrix of f(x, y)
# hess_xx = -400 * (Y - 3*X**2) + 2
# hess_xy = hess_yx = -400 * X
# hess_yy = 200 * np.ones_like(X)
#
# # Print the gradient and Hessian
# print("Gradient of f(x, y):")
# print(grad_x)
# print(grad_y)
#
# print("\nHessian matrix of f(x, y):")
# print(hess_xx)
# print(hess_xy)
# print(hess_yx)
# print(hess_yy)


import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

# Define the function
def f(x, y):
    return 100 * (y - x**2)**2 + (1 - x)**2

# Create a meshgrid of x and y values
x = np.linspace(-2, 2, 100)
y = np.linspace(-1, 3, 100)
X, Y = np.meshgrid(x, y)

# Calculate the corresponding z values using the function
Z = f(X, Y)

# Create a 3D plot
fig = plt.figure()
ax = plt.axes(projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis')

# Set labels and title
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('f(x, y)')
ax.set_title('3D Plot of f(x, y)')

# Display the plot
plt.show()

import sympy as sp

# Define the symbols
x, y = sp.symbols('x y')

# Define the function
f = 100 * (y - x**2)**2 + (1 - x)**2

# Calculate the gradient
grad = [sp.diff(f, var) for var in (x, y)]
print("Gradient: ", grad)

# Calculate the Hessian
hessian = [[sp.diff(var2, var1) for var1 in (x, y)] for var2 in (x, y)]
print("Hessian: ", hessian)
