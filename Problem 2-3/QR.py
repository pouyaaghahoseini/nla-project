import numpy as np


def mult_matrix(M, N):
    """Multiply square matrices of same dimension M and N"""
    # Converts N into a list of tuples of columns
    tuple_N = zip(*N)

    # Nested list comprehension to calculate matrix multiplication
    return [[sum(el_m * el_n for el_m, el_n in zip(row_m, col_n)) for col_n in tuple_N] for row_m in M]


def QR(A):
    m, n = A.shape
    Q = np.eye(m)
    for i in range(n - (m == n)):
        H = np.eye(m)
        H[i:, i:] = Householder(A[i:, i])
        Q = np.dot(Q, H)  # Create Q
        A = np.dot(H, A)  # Create R
    return Q, A


def Householder(a):
    v = a / (a[0] + np.copysign(np.linalg.norm(a), a[0]))
    v[0] = 1
    H = np.eye(a.shape[0])
    H -= (2 / np.dot(v, v)) * np.dot(v[:, None], v[None, :])
    return H


def SolveQR(a, b):
    q, r = QR(a)
    _, n = r.shape
    return np.linalg.solve(r[:n, :], np.dot(q.T, b)[:n])



a = np.array([[2, 3, 1],
              [5, 1, 2],
              [2, 8, 1]])
b = np.array([6, 8, 11])
Q, R = QR(a)
Q = Q.round(6)
R = R.round(6)
qq, rr = np.linalg.qr(a)
print("Q:")
print(Q)
print(qq)
print("R:")
print(R)
print(rr)

x = SolveQR(a,b)
print("X: ",x)
