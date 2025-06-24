import numpy as np
import sympy as sp

def gradient_descent(X, Y, theta, learning_rate, iteration):
    m=len(Y)
    for _ in range(iteration):
        predictions = np.dot(X,theta)
        errors = predictions - Y
        gradients=(1/m) * np.dot(X.T, errors)
        theta -=learning_rate*gradients
    return theta

x, y = sp.symbols('x y')
f=x**2 + 3*y**2 - 4*x*y
derivative=sp.diff(f,x,y)
print("Derivative: ",derivative)

par_x=sp.diff(f,x)
par_y=sp.diff(f,y)
print(f"Gradient [{par_x}, {par_y}]")

X = np.array([[1, 1], [1, 2], [1, 3]])
Y = np.array([2, 2.5, 3.5])
theta = np.array([0.1, 0.1])
learning_rate=0.1
iterations=1000
print(gradient_descent(X,Y,theta,learning_rate,iterations))
