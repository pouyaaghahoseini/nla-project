import numpy as np
import time

def create_tridiag(a, b, c, n):
    A = np.zeros((n, n))
    for i in range(n):
        A[i][i] = b
        if i < n - 1:
            A[i + 1][i] = a
            A[i][i + 1] = c
    return A


def LU(A, b):
    n = len(A)

    L = np.eye(n)

    U = np.zeros((n,n))
    for i in range(0, n):
        for j in range(0, n):
            U[i][j] = A[i][j]

    n = len(U)

    # Find both U and L matrices
    for i in range(0, n):
        # Find the maximun value in a column in order to change lines
        maxElem = abs(U[i][i])
        maxRow = i
        for k in range(i + 1, n):  # Interacting over the next line
            if abs(U[k][i]) > maxElem:
                maxElem = abs(U[k][i])  # Next line on the diagonal
                maxRow = k

        # Swap the rows pivoting the maxRow, i is the current row
        for k in range(i, n):  # Interacting column by column
            tmp = U[maxRow][k]
            U[maxRow][k] = U[i][k]
            U[i][k] = tmp

        # Subtract lines
        for k in range(i + 1, n):
            c = -U[k][i] / float(U[i][i])
            L[k][i] = c  # (4.4) Store the multiplier
            for j in range(i, n):
                U[k][j] += c * U[i][j]  # Multiply with the pivot line and subtract

        # Make the rows bellow this one zero in the current column
        for k in range(i + 1, n):
            U[k][i] = 0

    return L, U

n = 50
a = create_tridiag(1, 4, -1, n)
b = [1 for i in range(n)]
start = time.time()
L, U = LU(a, b)
end = time.time()

print("L: ")
print(L)
print("U: ")
print(U)
print("Time: ", end - start)
