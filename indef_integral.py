# %% md
# # Indefinite Integral
# A sympy based code to quickly evaluate indefinite integral

# %% imports
from sympy import *

# %% symbol creation
x = symbols('x')

# %% function creation
f = sin(x**2)

# %% integration
I=Integral(f, x)

# %% result
F=I.doit()

# %% display
print(F)
