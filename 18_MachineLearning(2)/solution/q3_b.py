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
