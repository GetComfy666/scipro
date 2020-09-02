#math module for solving the schrödinger equation numerically for arbitrary potentials
from scipy.linalg import eigh_tridiagonal as tridiag
import numpy as np
d = 3*np.ones(4)
e = -1*np.ones(3)

print(tridiag(d, e))





