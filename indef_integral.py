# %% md
# # Indefinite Integral
# A sympy based code to quickly evaluate indefinite integral
# ### v2.0

# %% imports
from sympy import *

# %% symbol creation
x = symbols('x')

# %% function creation
f = 1/log(x)**3

# %% integration
I=Integral(f, x)

# %% result
F=I.doit()

# %% display
pprint(F)
