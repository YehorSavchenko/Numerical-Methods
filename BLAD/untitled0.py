# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import numpy as np
import random


def funkcja1(h, fun, x):
    return (fun(x + h) - fun(x)) / h


def funkcja2(h, fun, x):
    return (fun(x + h) - fun(x - h)) / (2 * h)


def blad1(h, fun, x, pochodna_fun):
    return


def blad2(h, fun, x, pochodna_fun):
    return np.abs(funkcja2(h, fun, x) - pochodna_fun)


def grafik(h, bl, title):
    plt.title(title)
    plt.xlabel("log(h)")
    plt.ylabel("log(E(h))")
    plt.grid()
    plt.plot(h, bl)
    # plt.xscale("log")
    # plt.yscale("log")
    plt.savefig(title + ".png")
    plt.show()


x = 0.3
h = np.linspace(1.0, 10, dtype=np.double)
function = np.cos
dx_function = -np.sin(x)
first_template = (function(x + h) - function(x)) / h



# x = 0.3
# d = random.uniform(x, x + 2)
# fun = np.cos
# pochodna1_fun = -np.sin(x)
# pochodna2_fun = -np.cos(x)
#
# h = np.linspace(0.000000001, 1000, 10000, dtype=np.double)
# ff = fun(x+h)*(1+0.5)
# f = fun(x)*(1+0.5)
# blad3 = (np.abs(pochodna2_fun) * h) / 2 + ((np.abs(pochodna1_fun) * 2) / h) * 1000
#  bl1 = np.abs(funkcja1(h, fun, x) - pochodna1_fun)
# bl1 = np.abs((ff-f)/h - pochodna1_fun)
# grafik(-np.log(h), np.log(bl1), "double_wykres_funkcja1")

# h = np.linspace(0.0000000000000000000000001, 100, 100000, dtype=np.float)
# bl = np.abs(blad1(h, fun, x, pochodna_fun))
# grafik(h, bl, "float_wykres_funkcja1")
#
# h = np.linspace(0.0000000000000000000000001, 100, 10000, dtype=np.double)
# bl = np.abs(blad2(h, fun, x, pochodna_fun))
# grafik(h, bl, "double_wykres_funkcja2")
#
# h = np.linspace(0.0000000000000000000000001, 100, 10000, dtype=np.float)
# bl = np.abs(blad2(h, fun, x, pochodna_fun))
# grafik(h, bl, "float_wykres_funkcja2")
