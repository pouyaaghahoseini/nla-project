import numpy as np
import time
MAX = 100;
def create_tridiag(a, b, c, n):
    A = np.zeros((n, n))
    for i in range(n):
        A[i][i] = b
        if i < n - 1:
            A[i + 1][i] = a
            A[i][i + 1] = c
    return A

def Doolittle(mat, n):
    lower = np.zeros((n,n))
    upper = np.zeros((n,n))

    for i in range(n):

        # Upper Triangular
        for k in range(i, n):

            # Summation of L(i, j) * U(j, k)
            sum = 0;
            for j in range(i):
                sum += (lower[i][j] * upper[j][k]);

            # Evaluating U(i, k)
            upper[i][k] = mat[i][k] - sum;

        # Lower Triangular
        for k in range(i, n):
            if (i == k):
                lower[i][i] = 1;  # Diagonal as 1
            else:

                # Summation of L(k, j) * U(j, i)
                sum = 0;
                for j in range(i):
                    sum += (lower[k][j] * upper[j][i]);

                # Evaluating L(k, i)
                lower[k][i] = int((mat[k][i] - sum) /
                                  upper[i][i]);

            # setw is for displaying nicely
    print("Lower Triangular\t\tUpper Triangular");
    return lower, upper

n = 50
a = create_tridiag(1, 4, -1, n)
b = [1 for i in range(n)]
start = time.time()
L, U = Doolittle(a, n);
end = time.time()

print("L: ")
print(L)
print("U: ")
print(U)
print("Time: ", end - start)

