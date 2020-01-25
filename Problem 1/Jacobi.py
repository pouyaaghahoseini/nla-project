import numpy as np
import scipy
from scipy.linalg import solve


def create_tridiag(a, b, c, n):
    A = np.zeros((n, n))
    for i in range(n):
        A[i][i] = b
        if i < n - 1:
            A[i + 1][i] = a
            A[i][i + 1] = c
    return A


def jacobi(A, b, x, n, Iteration= False):
    counter = 0
    D = np.diag(A)
    R = A - np.diagflat(D)
    x0 = x
    x = (b - np.dot(R, x0)) / D
    if Iteration==True:
        print("Iteration " + str(counter) + ": " + str(x))
    counter += 1
    while np.linalg.norm(np.subtract(x, x0)) > 0.0001:
        x0 = x
        x = (b - np.dot(R, x0)) / D
        if Iteration==True:
            print("Iteration " + str(counter) + ": " + str(x))
        counter += 1

    print("Result: " + str(x))
    return x


'''___Main___'''
n = 50
A = np.zeros((n, n))
temp = np.ones(n-1)
np.fill_diagonal(A,4)
np.fill_diagonal(A[1:], temp)
np.fill_diagonal(A[:,1:], -temp)
b = np.ones(n)
x = np.ones(n)
jacobi(A,b,x,n, Iteration=False)
print("Scipy Result: ", solve(A, b))
