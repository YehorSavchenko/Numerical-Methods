import numpy as np
import matplotlib.pyplot as plt
import scipy.sparse
from scipy.sparse.linalg import spsolve


def f(x):
    return 1 / (1 + 25 * x * x)


def wielomian(stopien):
    punkty_i = []
    tabx = np.linspace(-1, 1, 256)
    y = []
    b = np.arange(stopien - 2, dtype=float)

    interpolacja = []
    for i in tabx:
        y.append(f(i))
    for i in range(stopien):
        punkty_i.append(-1 + 2 * (i / (stopien-1)))
    h = punkty_i[1] - punkty_i[0]
    A0 = np.linspace(4, 4, stopien - 2)
    A1 = np.ones(stopien - 3)
    diagonale = [A1, A0, A1]
    A = scipy.sparse.diags(diagonale, [-1, 0, 1], format='csc')
    for i in range(stopien - 2):
        b[i] = (6 / (h ** 2)) * (f(punkty_i[i]) - (2 * f(punkty_i[i + 1])) + f(punkty_i[i + 2]))
    epsilon = spsolve(A, b)
    epsilon = np.insert(epsilon, 0, 0)
    epsilon = np.append(epsilon, 0)
    i = 0
    for j in range(stopien - 1):
        while (tabx[i] <= punkty_i[j + 1]):
            x = tabx[i]
            A = (punkty_i[j + 1] - x) / (punkty_i[j + 1] - punkty_i[j])
            B = (x - punkty_i[j]) / (punkty_i[j + 1] - punkty_i[j])
            C = (1 / 6) * ((A ** 3) - A) * ((punkty_i[j + 1] - punkty_i[j]) ** 2)
            D = (1 / 6) * ((B ** 3) - B) * ((punkty_i[j + 1] - punkty_i[j]) ** 2)
            i += 1
            wielomian = f(punkty_i[j]) * A + f(punkty_i[j + 1]) * B + C * epsilon[j] + D * epsilon[j + 1]
            interpolacja.append(abs((f(x) - wielomian)))
            if (i >= len(tabx)): break
    return tabx, y, interpolacja


tab = []
tab.extend(wielomian(3))
print(tab[2])
# tab.extend(wielomian(10))
# tab.extend(wielomian(16))
plt.plot(tab[0],tab[1],'r',label="f(x)")
# plt.yscale("log")
# print(tab[0],tab[2])
plt.plot(tab[0], tab[2], 'b', label="w19")
# plt.plot(tab[0],tab[5],'g',label="w10")
# plt.plot(tab[0],tab[8],'y',label="w16")
plt.legend(loc="upper left")
plt.ylabel('|f(x)-S(x)|')
plt.xlabel('x')
# plt.savefig("log2.svg")
plt.show()
