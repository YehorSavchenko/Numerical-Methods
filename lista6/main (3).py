import math
import numpy as np
import time


def integrateNC(a, b, f, eps):
    N = 2
    integral = 0
    newIntegral = 1 + eps
    while abs(newIntegral - integral)>eps:
        sumParzyst = 0
        sumNieParzyst = 0
        WIDTH = (b - a)/N
        integral = newIntegral
        for i in range(0, N, 2):
            x = a + WIDTH*i
            sumParzyst += f(x)
            if i < N-1:
                x1 = a + WIDTH*(i+1)
                sumNieParzyst += f(x1)
        newIntegral = WIDTH/3*(f(a)+f(b)+2*sumParzyst+4*sumNieParzyst)
        N *= 2
    return newIntegral


def trapezoid(a, b, N, f):
    WIDTH = (b-a)/N
    integral = 0
    for i in range(1, N, 1):
        x = a + i*WIDTH
        integral += f(x)
    integral = (integral + 1/2*(f(a)+f(b)))*WIDTH
    return integral


def integrateRomberg(a, b, f, eps):
    tablica = np.zeros((30, 30))
    tablica[0][0] = (b-a)/2*(f(b)+f(a))
    iterationNum = 1
    while abs(tablica[iterationNum-1][iterationNum-1]-tablica[iterationNum-2][iterationNum-2]) > eps:
        # print(iterationNum)
        tablica[0][iterationNum] = trapezoid(a, b, pow(2, iterationNum), f)
        for i in range(1, iterationNum+1, 1):
            tablica[i][iterationNum] = (pow(4, iterationNum)*tablica[i-1][iterationNum]-tablica[i-1][iterationNum-1])/(pow(4, iterationNum)-1)
        iterationNum += 1
    return tablica[iterationNum-1][iterationNum-1]

def g():
    return

start = time.time()
print('Metoda Newtona-Cotesa:\t', integrateNC(0, 1, lambda x: math.sin(x), math.pow(10, -10)))
# print('Trapezoid:\t', trapezoid(0, 1, pow(2, 10), lambda x: math.sin(x)))
print('Rosberg:\t', integrateRomberg(0, 1, lambda x: math.sin(x), math.pow(10, -10)))
print('Czas programy:\t', time.time() - start)

