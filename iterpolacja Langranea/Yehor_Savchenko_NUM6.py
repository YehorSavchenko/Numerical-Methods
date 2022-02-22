import math
import numpy as np
import matplotlib.pyplot as plt


def f_y_1(x):
    return 1 / (1 + 25 * x ** 2)


def f_y_2(x):
    return 1 / (1 + x ** 2)


def f_x_a(i, n):
    return -1 + 2 * i / (n + 1)


def f_x_b(i, n):
    return math.cos(((2 * i + 1) / (2 * (n + 1))) * math.pi)


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
    res = lang(x, y, x_new)
    print()
    return res


def graphics(l, res1, res2, res3, f_y, N1, N2, N3, i, fun):
    plt.ylim(-1, 3)
    plt.title("Interpolacja Lagrange'a")
    plt.xlabel("x")
    plt.ylabel("f")
    plt.grid()
    # rysujemy wynik interpolacji
    plt.plot(l, res1, 'r', label="interpolacja n = " + N1.__str__())
    plt.plot(l, res2, 'b', label="interpolacja n = " + N2.__str__())
    plt.plot(l, res3, 'm', label="interpolacja n = " + N3.__str__())
    # a powinno to wyglądać tak
    plt.plot(l, f_y(l), 'g', label="funkcja" + fun)

    plt.legend()
    plt.savefig("plot" + i.__str__() + ".svg")
    plt.show()


N1 = 5
N2 = 50
N3 = 100
x = []
y = []
res1 = []
res2 = []
res3 = []
x_new = np.arange(-1.0, 1.0, 0.1)

res1 = result(f_x_a, f_y_1, x, y, N1)
res2 = result(f_x_a, f_y_1, x, y, N2)
res3 = result(f_x_a, f_y_1, x, y, N3)
graphics(x_new, res1, res2, res3, f_y_1, N1, N2, N3, 1, "f_y_1")

res1 = result(f_x_a, f_y_2, x, y, N1)
res2 = result(f_x_a, f_y_2, x, y, N2)
res3 = result(f_x_a, f_y_2, x, y, N3)
graphics(x_new, res1, res2, res3, f_y_2, N1, N2, N3, 2, "f_y_2")

res1 = result(f_x_b, f_y_1, x, y, N1)
res2 = result(f_x_b, f_y_1, x, y, N2)
res3 = result(f_x_b, f_y_1, x, y, N3)
graphics(x_new, res1, res2, res3, f_y_1, N1, N2, N3, 3, "f_y_1")

res1 = result(f_x_b, f_y_2, x, y, N1)
res2 = result(f_x_b, f_y_2, x, y, N2)
res3 = result(f_x_b, f_y_2, x, y, N3)
graphics(x_new, res1, res2, res3, f_y_2, N1, N2, N3, 4, "f_y_2")
