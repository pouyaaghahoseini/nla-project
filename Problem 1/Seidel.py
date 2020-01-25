import numpy as np

def create_tridiag(l, r, u, n):
    A = np.zeros((n, n))
    temp = np.ones(n - 1)
    np.fill_diagonal(A, r)
    np.fill_diagonal(A[1:], l)
    np.fill_diagonal(A[:, 1:], u)
    return A


def seidel(a, x, b):
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
        print("Iteration: " + str(x))
        x0 = np.copy(x)
        for j in range(0, n):
            # temp variable d to store b[j]
            d = b[j]
            # to calculate respective xi, yi, zi
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
x = seidel(a, x, b)
    # print each time the updated solution
print(x)
