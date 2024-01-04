import sympy as sp
from sympy.physics.matrices import msigma
from sympy.physics.quantum import TensorProduct
from sympy.physics.quantum.spin import Jx, Jy, Jz, Jplus, Jminus, J2
from sympy.physics.quantum.cg import CG
from sympy.physics.quantum.represent import represent
from sympy.physics.quantum.spin import Rotation
from sympy.physics.quantum.spin import WignerD
from sympy.physics.quantum.spin import couple
from sympy.physics.quantum.spin import uncouple
from sympy import symbols
from sympy import plotting

from sympy import sin, cos, pi, sqrt, exp, I, simplify, expand, factor, collect, diff, integrate, oo, limit, Matrix, Eq, solve, Poly, Function, Derivative, dsolve, linsolve, nonlinsolve, dsolve, solve_linear_system, solve_linear_system_LU, solve_linear_system_LU, solve_linear_system, solve_linear_system_LU, solve

# define operators
def comm(A,B):
    return A*B - B*A

def propagator(H,t):
    return exp(-I*H*t)


# define symbols
H = sp.Symbol('H')
Hz = sp.Symbol('H_z')
Hcs = sp.Symbol('H_cs')
Hj = sp.Symbol('H_j')
omega0 = sp.Symbol('\omega_0', real=True)
sigma1, sigma2 = sp.symbols('\sigma_1 \sigma_2', real=True)
J12 = sp.Symbol('J_{12}', real=True)

id2 = sp.eye(2)