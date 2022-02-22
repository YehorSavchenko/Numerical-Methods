import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse


def f_y(x):
    return 1 / (1 + 25 * x ** 2)


def f_x(i, n):
    return -1 + 2 * i / (n - 1)


def initialization(N):
    res.clear()
    A.clear()
    B.clear()
    x.clear()
    y.clear()
    for i in range(0, N + 1):
        x.append(f_x(i, N))
        y.append(f_y(x[i]))


def initialization_tab(N):
    for i in range(0, N):
        for j in range(0, N):
            if j == i:
                tablica_ch[i][j] = 4
                if j < N - 1 and i < N - 1:
                    tablica_ch[i + 1][j] = 1
                    tablica_ch[i][j + 1] = 1
    # A0 = np.linspace(4, 4, N - 2)
    # A1 = np.ones(N - 3)
    # diagonale = [A1, A0, A1]
    # tablica_ch = scipy.sparse.diags(diagonale, [-1, 0, 1], format='csc')


def wyrazyWolne():
    for i in range(0, N - 1):
        wektor_wyrazow.append(
            (y[i - 1] - 2 * y[i] + y[i + 1]) * (6 /(delta ** 2))
        )


def initialization_A_B():
    for i in range(1, N + 1):
        A.append(
            (y[i] - y[i - 1]) /
            delta - delta / 6 * (wekotr_ksi[i] - wekotr_ksi[i - 1])
        )
        B.append(
            y[i - 1] - wekotr_ksi[i - 1] * delta ** 2 / 6
        )


def cubic_spline_interpolation(x_new):
    i = 1
    if x_new + delta > 1:
        i = len(x) - 2
    else:
        while x_new >= x[i + 1]:
            i += 1
    return wekotr_ksi[i - 1] * (x[i] - x_new) ** 3 / (6 * delta) + \
           wekotr_ksi[i] * (x_new - x[i - 1]) ** 3 / (6 * delta) + \
           A[i - 1] * (x_new - x[i - 1]) + B[i - 1]


def graphics(l, res, f_y, N1, i):
    # plt.ylim(0, 1.5)
    # plt.xlim(-1, 1)
    plt.title("Cubic Spline Interpolation")
    plt.xlabel("x")
    plt.ylabel("f")
    plt.grid()
    # rysujemy wynik interpolacji
    plt.plot(l, res, 'r', label="interpolacja n = " + N1.__str__())
    # a powinno to wyglądać tak
    # plt.plot(l, f_y(l), 'g', label="funkcja")

    plt.legend()
    plt.savefig("plot" + i.__str__() + ".svg")
    plt.show()


N = 100
x = []
y = []
wektor_wyrazow = []
tablica_ch = np.zeros((N - 1, N - 1))
A = []
B = []
res = []

initialization(N)
initialization_tab(N-1)
delta = abs(x[1] - x[0])
wyrazyWolne()
wekotr_ksi = np.linalg.solve(tablica_ch, wektor_wyrazow)
wekotr_ksi = np.concatenate(([0], wekotr_ksi, [0]))
initialization_A_B()
x_new = np.arange(-1.0, 1.0, 0.1)
for i in range(len(x_new)):
    res.append(f_y(x_new[i])-cubic_spline_interpolation(x_new[i]))

print(res)
graphics(x_new, res, f_y, N, 1)

# s = scipy.interpolate.CubicSpline

#
# N = 50
# x = []
# y = []
# wektor_wyrazow = []
# tablica_ch = np.zeros((N - 1, N - 1))
# A = []
# B = []
# res = []
#
# initialization(N)
# initialization_tab(N - 1)
# delta = abs(x[1] - x[0])
# wyrazyWolne()
# wekotr_ksi = np.linalg.solve(tablica_ch, wektor_wyrazow)
# wekotr_ksi = np.concatenate(([0], wekotr_ksi, [0]))
# initialization_A_B()
# x_new = np.arange(-1.0, 1.0, 0.1)
# for i in range(len(x_new)):
#     res.append(cubic_spline_interpolation(x_new[i]))
# graphics(x_new, res, f_y, N, 2)


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


def compare_interpolation(l, res1, res2, N1, i):
    plt.ylim(-1, 3)
    plt.title("Compare Interpolation  n = " + N1.__str__())
    plt.xlabel("x")
    plt.ylabel("f")
    plt.grid()
    # rysujemy wynik interpolacji
    plt.plot(l, res1, 'r', label="Lagrange'a")
    plt.plot(l, res2, 'g', label="Cubic spline")

    plt.legend()
    plt.savefig("plot" + i.__str__() + ".svg")
    plt.show()


res1 = []
res1 = result(f_x, f_y, x, y, N)
compare_interpolation(x_new, res1, res, N, 3)
