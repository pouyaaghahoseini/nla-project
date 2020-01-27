import numpy as np
import time
from scipy.linalg import solve
def create_tridiag(l, r, u, n):
    A = np.zeros((n, n))
    temp = np.ones(n - 1)
    np.fill_diagonal(A, r)
    np.fill_diagonal(A[1:], l)
    np.fill_diagonal(A[:, 1:], u)
    return A


def seidel(a, x, b, Iteration= False):
    x0 = np.copy(x)
    n = len(x)
    # Finding X1
    for j in range(n):
        d = b[j]
        for i in range(0, n):
            if (j != i):
                d -= a[j][i] * x[i]
        x[j] = d / a[j][j]
    # Iterate Seidel
    while np.linalg.norm(np.subtract(x, x0)) > 0.0001:
        if Iteration == True:
            print("Iteration: " + str(x))
        x0 = np.copy(x)
        for j in range(0, n):
            # temp variable d to store b[j]
            d = b[j]
            for i in range(0, n):
                if (j != i):
                    d -= a[j][i] * x[i]
                # updating the value of our solution
            x[j] = d / a[j][j]
        # returning our updated solution
    return x

n = 50
a = create_tridiag(1, 4, -1, n)
b = np.ones(n)
x = np.ones(n)
print(x)

# loop run for m times depending on m the error value
start = time.time()
x = seidel(a, x, b, Iteration= False)
    # print each time the updated solution
end = time.time()
print("Scipy Result: ", solve(a, b))
print(x)
print("Time: ", end - start)
