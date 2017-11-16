import sympy as sym

# 1階微分
def differentiate(function, x):
    (dx) = sym.symbols('dx')
    return sym.limit((function(x+dx) - function(x)) / dx, dx, 0)

# 2階微分
def differentiate2(function, x):
    (dx) = sym.symbols('dx')
    return sym.limit((function(x+dx) + function(x-dx) - 2 * function(x)) / dx**2, dx, 0)
