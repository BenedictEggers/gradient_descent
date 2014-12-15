# Ben Eggers <ben.eggers36@gmail.com>
#
# A simple, gradient-descent-based linear system solver. The idea is as follows:
#
# We are given a matrix A and a vector b, and want to find x such that Ax = b.
#
# We turn this into an optimization problem, with our objective function f(x) =
# the A-norm of the error (Ax - b). We use an iterative method. At each step,
# we find the gradient at our current guess (initialized to 0), then take the
# optimal step size (computable because matrices are awesome) in the direction
# of the gradient. We repeat until the gradient = 0, which is when our guess
# will be the solution to the system.
#
# I only want to deal with SDD systems here, so the matrix input will be in
# graph form, with the matrix defined to be the Laplacian of the input graph.

import numpy as np
import time

# Get the gradient of A at x
def grad(A, b, x):
    return -2 * rhe(A, b, x)

# Error on the right-hand side. b - Ax
def rhe(A, b, x):
    return b - A.dot(x)

def get_matrix():
    return np.array([1, -1, 0,     -1, 2, -1,     0, -1, 2 ]).reshape((3, 3))

def get_target(length):
    return np.array([x for x in range(length)])

def report(A, b, x):
    print "x =", x
    print "Error norm:", np.linalg.norm(rhe(A, b, x))

# ititial conditions
A = get_matrix()
b = get_target(A.shape[0])

x = np.array([0 for i in range(b.shape[0])])

# do the actual descent
g = grad(A, b, x)
err = float(raw_input("Desired gradient norm? "))
while np.linalg.norm(g) > err:
    r = rhe(A, b, x)
    x = x + ((1. * r.dot(r)) / (r.dot(A).dot(r))) * r
    g = grad(A, b, x)

report(A, b, x)
