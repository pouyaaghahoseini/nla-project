import numpy as np

def create_tridiag(a, b, c, n):
    A = np.zeros((n, n))
    for i in range(n):
        A[i][i] = b
        if i < n - 1:
            A[i + 1][i] = a
            A[i][i + 1] = c
    return A


def solve_gauss(A, B):
    n = len(A)
    det = 1
    for i in range(n):

        # Find Maximum Row
        maxRow = i
        for j in range(i + 1, n):
            if abs(A[j][i]) > abs(A[maxRow][i]):
                maxRow = j
            # Swap Rows
        if maxRow != i:
            det *= -1
            for k in range(0, n):
                temp = A[i][k]
                A[i][k] = A[maxRow][k]
                A[maxRow][k] = temp
            temp = B[maxRow]
            B[maxRow] = B[i]
            B[i] = temp

        # Make upper diagonal
        for k in range(i + 1, n):
            t = -A[k][i] / A[i][i]
            for c in range(i, n):
                A[k][c] += t * A[i][c]
            B[k] += t * B[i]

    # Solve equation Ax=b for an upper triangular matrix A
    X = [0 for i in range(n)]
    for i in range(n - 1, -1, -1):
        X[i] = B[i] / A[i][i]
        for k in range(i - 1, -1, -1):
            B[k] -= A[k][i] * X[i]
        det *= A[i][i]
    return det, X


n=500
a = create_tridiag(1, 4, -1, n)
b = [1 for i in range(n)]
d, result = solve_gauss(a, b)
print("Determinant: ", d)
print("Result: ", result)
print("NumPy Result: ", np.linalg.solve(a, b))
