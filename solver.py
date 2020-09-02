#math module for solving the schrödinger equation numerically for arbitrary potentials
from scipy.linalg import eigh_tridiagonal as tridiag
import numpy as np

"""
d = 3*np.ones(4)
e = -1*np.ones(3)

print(tridiag(d, e))
"""
def linear_path(Ax, Ay, Bx, By, x):
	return Ay+(By-Ay)/(Bx-Ax)*(x-Ax)



def generate_potential(xmin, xmax, intpoints, npoints, mode = "linear"):
	V = np.zeros((int(npoints), 2))
	print(V)
	if mode == "linear":
		dx = (xmax-xmin)/npoints
		x = xmin
		n = 0
		i = 0
		while x <= xmax:
			V[i] = np.array([x, linear_path(*intpoints[n], *intpoints[n+1], x)])
			i += 1
			print(i, n)
			x += dx
			if x > intpoints[n + 1][0]:
				n += 1
	np.savetxt("potential.dat", V)
	return V


print(generate_potential(-2.0, 2.0, [[-2.0, 5], [0., 0.], [2.0, 5.0]], 500))


