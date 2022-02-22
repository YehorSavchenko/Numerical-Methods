import matplotlib.pyplot as plt
import numpy as np


def graphic(h, blad, graphic_title, legend_title, color):
    plt.title(graphic_title)
    plt.xlabel("log h")
    plt.ylabel("log E(h)")
    plt.xscale("log")
    plt.yscale("log")
    plt.grid()
    plt.plot(h, blad, color, label=legend_title)
    plt.legend()


def function_a(function, x, h):
    return (function(x + h) - function(x)) / h


def function_b(function, x, h):
    return (function(x + h) - function(x - h)) / (2 * h)


def zachowanie(x, function, function_prim, start, stop, dtype, graphic_title):
    h = np.logspace(start, stop, num=512, base=2, endpoint=False, dtype=dtype)
    blad_a = np.abs(function_a(function, x, h) - function_prim)
    blad_b = np.abs(function_b(function, x, h) - function_prim)
    graphic(h, blad_a, graphic_title, "a", "r")
    graphic(h, blad_b, graphic_title, "b", "g")
    plt.show()


x = 0.3
zachowanie(x, np.cos, -np.sin(x), -20, 0, np.float32, "functions for cos(x) float32")
zachowanie(x, np.cos, -np.sin(x), -32, 0, np.double, "functions for cos(x) double")

zachowanie(x, np.sin, np.cos(x), -20, 0, np.float32, "functions for sin(x) float32 ")
zachowanie(x, np.sin, np.cos(x), -32, 0, np.double, "functions for sin(x) double ")
