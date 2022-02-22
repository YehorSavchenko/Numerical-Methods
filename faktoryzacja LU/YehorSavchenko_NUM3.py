import numpy as np
import scipy.linalg as sc


def forward_substitution(A_pd, x):
    n = A_pd.shape[0]
    z = np.empty(len(x))
    z[0] = x[0]

    for i in range(1, n + 1):
        z[i] = x[i] - (z[i - 1] * A_pd[i - 1])

    return z


def back_substitution(A_d, A_nd1, A_nd2, z):
    n = A_d.shape[0]
    y = np.empty(n)
    y[n - 1] = z[n - 1] / A_d[n - 1]
    y[n - 2] = (z[n - 2] - (y[n - 1] * A_nd1[n - 2])) / A_d[n - 2]

    for i in range(n - 3, -1, -1):
        y[i] = (z[i] - (y[i + 1] * A_nd1[i]) - (y[i + 2] * A_nd2[i])) / A_d[i]

    return y


def determinant(A_d):
    n = A_d.shape[0]
    det = 1.0
    for i in range(0, n):
        det = det * A_d[i]

    return det


# Rozmiar Macierzy
N = 100
# Macierz NxN
A = np.zeros((N, N))
# Przykładowa inicjalizacja macierzy dla bibliotek numerycznych
for i in range(N):
    for j in range(N):
        if i == j:
            A[i][j] = 1.2
        if i - 1 == j:
            A[i][j] = 0.2
        if i == j - 1:
            A[i][j] = 0.1 / (i + 1)
        if i == j - 2:
            A[i][j] = 0.4 / ((i + 1) * (i + 1))

# Przechowywanie macierzy do zadania
A_pd = np.empty(N - 1)  # pod diagonalny
A_d = np.empty(N)  # diagonalny
A_nd1 = np.empty(N - 1)  # pierwszy nad diagonalny
A_nd2 = np.empty(N - 2)  # drugi nad diagonalny
x = np.empty(N)

# inicjalizacja macierzy do zadania
for i in range(0, N):
    A_d[i] = 1.2
    x[i] = i + 1

for i in range(0, N - 1):
    A_pd[i] = 0.2
    A_nd1[i] = (0.1 / (i + 1))

for i in range(0, N - 2):
    A_nd2[i] = (0.4 / ((i + 1) * (i + 1)))

# Rozkład LU
for i in range(1, N):
    A_pd[i - 1] = A_pd[i - 1] / A_d[i - 1]  # L(i+1)(i)
    A_d[i] = A_d[i] - (A_pd[i - 1] * A_nd1[i - 1])  # U(i)(i)
    if i < N - 1:
        A_nd1[i] = A_nd1[i] - (A_pd[i - 1] * A_nd2[i - 1])  # U(i)(i+1)

z = forward_substitution(A_pd, x)
y = back_substitution(A_d, A_nd1, A_nd2, z)
print("Rezultat zadania: ")
print("y = ", y)
print("Wyznacznyk = ", determinant(A_d))

print("----------------------------------------------------")
p, l, u = sc.lu(A)
x1 = np.linalg.solve(l, x)
y1 = np.linalg.solve(u, x1)
print("Rezultat bibliotek algebraicznych: ")
print("y = ", y1)
print("Wyznacznyck bibliotek algebraicznych: ", np.linalg.det(A))
print("Sprawdzanie, że rezultaty są równe: ", np.isclose(y1, y).all())
