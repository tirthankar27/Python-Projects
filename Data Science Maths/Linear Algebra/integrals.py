import numpy as np
import sympy as sp

x=sp.symbols('x')
f=sp.exp(-x)

definite_integral=sp.integrate(f,(x,1,3))
indefinite_integral=sp.integrate(f,x)
print("Definite integral: ",definite_integral)
print("Indefinite integral: ",indefinite_integral)