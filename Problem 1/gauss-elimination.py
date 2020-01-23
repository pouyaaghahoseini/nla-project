import numpy as np


def create_tridiag(a, b, c, n):
    A = np.zeros((n, n))
    for i in range(n):
        A[i][i] = b
        if i<n-1:
            A[i + 1][i] = a
            A[i][i + 1] = c
    return A

x = create_tridiag(1,4,-1,50)
print(x)
