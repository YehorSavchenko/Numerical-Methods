import numpy as np

def back_substitution(A_d, A_nd1, z):
    n = A_d.shape[0]
    y = np.empty(n)
    y[n - 1] = z[n - 1] / A_d[n - 1]
    y[n - 2] = (z[n - 2] - (y[n - 1] * A_nd1[n - 2])) / A_d[n - 2]

    for i in range(n - 3, -1, -1):
        y[i] = (z[i] - (y[i + 1] * A_nd1[i])) / A_d[i]

    return y


# Rozmiar Macierzy
N = 50
# Macierz NxN
A = np.zeros((N, N))
# Przykładowa inicjalizacja macierzy dla bibliotek numerycznych
for i in range(N):
    for j in range(N):
        A[i][j] = 1
        if i == j:
            A[i][j] = 10
        if i == j - 1:
            A[i][j] = 8

# Przechowywanie macierzy do zadania. Macierz , gdzie element diagonalny 9 ,a naddiagonalny 7. (A + uv^T)
U_d = np.empty(N)  # diagonalny
U_nd1 = np.empty(N - 1)  # pierwszy nad diagonalny
u = np.empty(N)  # wektor jedynek
v = np.empty(N)  # wektor jedynek
b = np.empty(N)  # wektor piatek

# inicjalizacja macierzy do zadania
for i in range(0, N):
    U_d[i] = 9
    v[i] = 1
    u[i] = 1
    b[i] = 5

for i in range(0, N - 1):
    U_nd1[i] = 7

u = np.expand_dims(np.array(u), axis=1)
v = v.reshape(1, N)
z = back_substitution(U_d, U_nd1, b).reshape(N, 1)
z_prim = back_substitution(U_d, U_nd1, u).reshape(N, 1)
y = np.subtract(z, (np.dot(z_prim, np.dot(v, z)) / (1 + np.dot(v, z_prim)))).reshape(1, N)
print("Rezultat zadania: ")
print("Wektor y:\n ", y)
print("------------------------------------")
y1 = np.linalg.solve(A, b)
print("Rezultat bibliotek algebraicznych: ")
print("Wektor y:\n", y1)
print("Sprawdzanie, że rezultaty są równe: ", np.isclose(y1, y).all())
