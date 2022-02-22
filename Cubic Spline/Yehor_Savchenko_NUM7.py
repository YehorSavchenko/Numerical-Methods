import numpy as np
import matplotlib.pyplot as plt


def f_y(x):
    return 1 / (1 + 25 * x ** 2)


def f_x(i, n):
    return -1 + 2 * i / (n - 1)


def initialization(n, x, y):
    for i in range(n):
        x.append(f_x(i, n))
        y.append(f_y(x[i]))


def initialization_tab(n, tablica_ch):
    for i in range(n):
        for j in range(n):
            if j == i:
                tablica_ch[i][j] = 4
                if i < n - 1:
                    tablica_ch[i + 1][j] = 1
                    tablica_ch[i][j + 1] = 1


def initialization_wyrazy_wolne(y, B, n, delta):
    for i in range(1, n - 1):
        B.append((y[i - 1] - 2 * y[i] + y[i + 1]) * 6 / (delta ** 2))


def initialization_A(i, delta, array_of_x, x):
    return (array_of_x[i + 1] - x) / delta

def initialization_B(i, delta, array_of_x, x):
    return (x - array_of_x[i]) / delta


def intialization_C_D(A, delta):
    return (A ** 3 - A) * (delta ** 2) / 6


def cubic_spline_interpolation(array_of_x, f, delta, wekotr_ksi, arrays_random_x, n):
    interpolacja = []
    roznica_interpolacji = []
    j = 0
    for i in range(n - 1):
        while j < len(arrays_random_x) and arrays_random_x[j] <= array_of_x[i + 1]:
            x = arrays_random_x[j]
            j += 1
            interpolacja.append(
                f(array_of_x[i]) * initialization_A(i, delta, array_of_x, x) + f(array_of_x[i + 1])
                * initialization_B(i, delta, array_of_x, x) + intialization_C_D(
                    initialization_A(i, delta, array_of_x, x), delta)
                * wekotr_ksi[i] + intialization_C_D(initialization_B(i, delta, array_of_x, x), delta) * wekotr_ksi[
                    i + 1])
            roznica_interpolacji.append(abs((f(x) - interpolacja[-1])))
    return interpolacja, roznica_interpolacji


def graphics(arrays_random_x, res1, res2, res3, f_y, N1, N2, N3, i):
    plt.grid()
    plt.plot(arrays_random_x, f_y(arrays_random_x), 'g', label="funkcja")
    plt.plot(arrays_random_x, res1, 'b', label="interpolacja n = " + N1.__str__())
    plt.plot(arrays_random_x, res2, 'r', label="interpolacja n = " + N2.__str__())
    plt.plot(arrays_random_x, res3, 'm', label="interpolacja n = " + N3.__str__())

    plt.legend()
    plt.savefig("plot" + i.__str__() + ".svg")
    plt.show()


def main_body(N, arrays_random_x, array_of_x, array_of_y):
    wektor_wyrazow_wolnych = []
    A = np.zeros((N - 2, N - 2))
    initialization(N, array_of_x, array_of_y)
    delta = abs(array_of_x[1] - array_of_x[0])
    initialization_tab(N - 2, A)
    initialization_wyrazy_wolne(array_of_y, wektor_wyrazow_wolnych, N, delta)
    wekotr_ksi = np.linalg.solve(A, wektor_wyrazow_wolnych)
    wekotr_ksi = np.concatenate(([0], wekotr_ksi, [0]))
    return cubic_spline_interpolation(array_of_x, f_y, delta, wekotr_ksi, arrays_random_x, N)


N1 = 5
N2 = 10
N3 = 15
arrays_random_x1 = np.linspace(-1.0, 1.0, 100)
arrays_random_x2 = np.linspace(-1.0, 1.0, 100)
arrays_random_x3 = np.linspace(-1.0, 1.0, 100)
arrays_random_x4 = np.linspace(-1.0, 1.0, 100)
array_of_x1 = []
array_of_y1 = []
array_of_x2 = []
array_of_y2 = []
array_of_x3 = []
array_of_y3 = []
result1, roznica1 = main_body(N1, arrays_random_x1, array_of_x1, array_of_y1)
result2, roznica2 = main_body(N2, arrays_random_x2, array_of_x2, array_of_y2)
result3, roznica3 = main_body(N3, arrays_random_x3, array_of_x3, array_of_y3)

plt.title("Cubic Spline Interpolation")
plt.xlabel("x")
plt.ylabel("f")
graphics(arrays_random_x4, result1, result2, result3, f_y, N1, N2, N3, 1)

plt.title("Difference Spline Interpolation")
plt.xlabel("x")
plt.ylabel("|f(x)−s(x)|")
graphics(arrays_random_x4, roznica1, roznica2, roznica3, f_y, N1, N2, N3, 2)


def lang(xs, ys, x):
    y = 0.0

    for k in range(len(xs)):
        t = 1.0
        for j in range(len(xs)):
            if j != k:
                t = t * ((x - xs[j]) / (xs[k] - xs[j]))
        y = y + (t * ys[k])

    return y


def init(f_x, f_y, N, x, y):
    x.clear()
    y.clear()
    for i in range(N):
        x.append(f_x(i, N))
        y.append(f_y(x[i]))


def result(f_x_a, f_y_1, x, y, N):
    init(f_x_a, f_y_1, N, x, y)
    res = lang(x, y, arrays_random_x4)
    print()
    return res


def compare_interpolation(l, res1, res2, N1, i):
    plt.ylim(-1, 3)
    plt.title("Compare Interpolation  n = " + N1.__str__())
    plt.xlabel("x")
    plt.ylabel("f")
    plt.grid()

    plt.plot(arrays_random_x4, f_y(arrays_random_x4), 'b', label="funkcja")
    plt.plot(l, res1, 'r', label="Lagrange'a")
    plt.plot(l, res2, 'g', label="Cubic spline")

    plt.legend()
    plt.savefig("plot" + i.__str__() + ".svg")
    plt.show()


res_compare1 = result(f_x, f_y, array_of_x2, array_of_y2, N2)
compare_interpolation(arrays_random_x4, res_compare1, result2, N2, 3)

res_compare2 = result(f_x, f_y, array_of_x3, array_of_y3, N3)
compare_interpolation(arrays_random_x4, res_compare2, result3, N3, 4)
