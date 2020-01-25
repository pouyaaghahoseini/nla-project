import numpy as np
import scipy
from scipy.linalg import solve


def jacobi(A, b, x, n):
    counter = 0
    D = np.diag(A)
    R = A - np.diagflat(D)
    x0 = x
    x = (b - np.dot(R, x0)) / D
    print("Iteration " + str(counter) + ": " + str(x))
    counter += 1
    while np.linalg.norm(np.subtract(x, x0)) > 0.0001:
        x0 = x
        x = (b - np.dot(R, x0)) / D
        print("Iteration " + str(counter) + ": " + str(x))
        counter +=1
    return x


'''___Main___'''

A = np.array([[4.0, -2.0, 1.0], [1.0, -3.0, 2.0], [-1.0, 2.0, 6.0]])
b = [1.0, 2.0, 3.0]
x = [1.0, 1.0, 1.0]
n = 25

x = jacobi(A, b, x, n)
print("Final Result: ", solve(A, b))
