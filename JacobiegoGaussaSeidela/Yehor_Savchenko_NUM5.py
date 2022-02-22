import numpy as np
import matplotlib.pyplot as plt


def gauss_seidel(x, previous_gauss):
    while True:
        previous_gauss.append(x.copy())
        for i in range(N):
            if i == 0:
                x[i] = (b[i] - A_nd1[i] * x[i + 1] - A_nd2[i] * x[i + 2]) / A_d[i]
            if i == 1:
                x[i] = (b[i] - A_pd1[i - 1] * x[i - 1] - A_nd1[i] * x[i + 1] - A_nd2[i] * x[i + 2]) / A_d[i]
            if i != 0 and i != 1 and i != N - 1 and i != N - 2:
                x[i] = (b[i] - A_pd2[i - 2] * x[i - 2] - A_pd1[i - 1] * x[i - 1] - A_nd1[i] * x[i + 1] - A_nd2[i] * x[
                    i + 2]) / A_d[i]
            if i == N - 2:
                x[i] = (b[i] - A_pd2[i - 2] * x[i - 2] - A_pd1[i - 1] * x[i - 1] - A_nd1[i] * x[i + 1]) / A_d[i]
            if i == N - 1:
                x[i] = (b[i] - A_pd2[N - 3] * x[i - 2] - A_pd1[N - 2] * x[i - 1]) / A_d[i]

        if abs(previous_gauss[-1][0] - x[0]) < PRECISION:
            break


def jacobi(x, previous_jacobi):
    while True:
        previous_jacobi.append(x.copy())
        for i in range(0, N):
            if i == 0:
                x[i] = (b[i] - A_nd1[i] * x[i + 1] - A_nd2[i] * x[i + 2]) / A_d[i]
            if i == 1:
                x[i] = (b[i] - A_pd1[i - 1] * previous_jacobi[-1][i - 1] - A_nd1[i] * x[i + 1] - A_nd2[i] * x[i + 2]) / \
                       A_d[
                           i]
            if i != 0 and i != 1 and i != N - 1 and i != N - 2:
                x[i] = (b[i] - A_pd2[i - 2] * previous_jacobi[-1][i - 2] - A_pd1[i - 1] * previous_jacobi[-1][i - 1] -
                        A_nd1[
                            i] * x[i + 1] - A_nd2[i] * x[
                            i + 2]) / A_d[i]
            if i == N - 2:
                x[i] = (b[i] - A_pd2[i - 2] * previous_jacobi[-1][i - 2] - A_pd1[i - 1] * previous_jacobi[-1][i - 1] -
                        A_nd1[
                            i] * x[i + 1]) / A_d[i]
            if i == N - 1:
                x[i] = (b[i] - A_pd2[N - 3] * previous_jacobi[-1][i - 2] - A_pd1[N - 2] * previous_jacobi[-1][i - 1]) / \
                       A_d[i]

        if abs(previous_jacobi[-1][0] - x[0]) < PRECISION:
            break


def start_values(x_jacobi, x_gauss, prev_jacobi, prev_gauss, deviation_jacobi, deviation_gauss, values):
    prev_jacobi.clear()
    prev_gauss.clear()
    deviation_jacobi.clear()
    deviation_gauss.clear()
    for i in range(N):
        x_gauss[i] = values
        x_jacobi[i] = values


def methods(x_jacobi, prev_jacobi, x_gauss, prev_gauss):
    # Jacobi
    jacobi(x_jacobi, prev_jacobi)
    for i in range(len(prev_jacobi)):
        deviation_jacobi.append(np.linalg.norm(x_jacobi - prev_jacobi[i]))

    # Gauss
    gauss_seidel(x_gauss, prev_gauss)
    for i in range(len(prev_gauss)):
        deviation_gauss.append(np.linalg.norm(x_gauss - prev_gauss[i]))


def graphics(deviation_gauss, deviation_jacobi, i):
    plt.title("Jacobi and Gauss-Seidel")
    plt.xlabel("iteration")
    plt.ylabel("deviation")
    plt.yscale("log")
    plt.grid()
    plt.plot(list(range(len(deviation_gauss))), deviation_gauss, 'g', label='Gauss-Seidel')
    plt.plot(list(range(len(deviation_jacobi))), deviation_jacobi, 'r', label='Jacobi')
    plt.legend()
    plt.savefig("plot" + i.__str__() + ".svg")
    plt.show()


# Rozmiar Macierzy
N = 100
PRECISION = 10 ** -10
# Macierz NxN
A = np.zeros((N, N))
# PrzykЕ‚adowa inicjalizacja macierzy dla bibliotek numerycznych
for i in range(N):
    for j in range(N):
        if i == j:
            A[i][j] = 3
        if i - 1 == j:
            A[i][j] = 1
        if i - 2 == j:
            A[i][j] = 0.2
        if i == j - 1:
            A[i][j] = 1
        if i == j - 2:
            A[i][j] = 0.2

# Przechowywanie macierzy do zadania
A_d = np.empty(N)  # diagonalny
A_pd1 = np.empty(N - 1)  # pod diagonalny pierwszy
A_pd2 = np.empty(N - 2)  # pod diagonalny drugi
A_nd1 = np.empty(N - 1)  # pierwszy nad diagonalny
A_nd2 = np.empty(N - 2)  # drugi nad diagonalny
b = np.empty(N)  # wektor wolnych wyrazow
x_jacobi = np.empty(N)
x_gauss = np.empty(N)
prev_gauss = []
prev_jacobi = []
deviation_gauss = []
deviation_jacobi = []

# inicjalizacja macierzy do zadania
for i in range(0, N):
    A_d[i] = 3
    b[i] = i + 1

for i in range(0, N - 1):
    A_pd1[i] = 1
    A_nd1[i] = 1

for i in range(0, N - 2):
    A_pd2[i] = 0.2
    A_nd2[i] = 0.2

start_values(x_jacobi, x_gauss, prev_jacobi, prev_gauss, deviation_jacobi, deviation_gauss, 1)
methods(x_jacobi, prev_jacobi, x_gauss, prev_gauss)
graphics(deviation_gauss, deviation_jacobi, 1)

start_values(x_jacobi, x_gauss, prev_jacobi, prev_gauss, deviation_jacobi, deviation_gauss, 10)
methods(x_jacobi, prev_jacobi, x_gauss, prev_gauss)
graphics(deviation_gauss, deviation_jacobi, 2)

start_values(x_jacobi, x_gauss, prev_jacobi, prev_gauss, deviation_jacobi, deviation_gauss, 100)
methods(x_jacobi, prev_jacobi, x_gauss, prev_gauss)
graphics(deviation_gauss, deviation_jacobi, 3)

print("Method Jacobi: \n", x_jacobi)
print("Method Gauss-Seidel: \n", x_gauss)
# Resultat z numpy
x1 = np.linalg.solve(A, b)
print("Numpy: \n", x1)
print(np.isclose(x_jacobi, x_gauss, x1).all())
