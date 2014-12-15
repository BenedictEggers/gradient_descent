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

# Get the gradient of A at x
def grad(A, b, x):
    return -2 * rhe(A, b, x)

# Error on the right-hand side. b - Ax
def rhe(A, b, x):
    b - A.dot(x)


# ititial conditions
A = get_matrix()
b = get_target()
x = np.array([0 for i in range(b.shape[0])])
report(A, b, x)

# do the actual descente
grad = grad(A, b, x)
while grad is not 0:



report(A, b, x)
