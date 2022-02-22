import numpy
import numpy as np
from numpy import sin


def simpson_integration_modified(my_func, a, b, n):
    # Szerokość pojedynczego przedziału
    delta_x = (b - a) / n
    total = my_func(a) + my_func(b)
    subtotal_sum_1 = 0
    subtotal_sum_2 = 0
    # pierwsza suma, pamiętamy że n = 2N
    for i in range(0, n, 2):
        x = a + i * delta_x
        subtotal_sum_1 += my_func(x)
    # druga suma, pamiętamy że n = 2N
    for i in range(1, n - 1, 2):
        x = a + i * delta_x
        subtotal_sum_2 += my_func(x)
    return delta_x * (total + 4 * subtotal_sum_1 + 2 * subtotal_sum_2) / 3


def simpson_integration_modified1(my_func, a, b, n):
    # Szerokość pojedynczego przedziału
    delta_x = (b - a) / n
    total = my_func(a) + my_func(b)
    subtotal_sum_1 = 0
    subtotal_sum_2 = 0
    # x = np.array(n / 2)
    # pierwsza suma, pamiętamy że n = 2N
    for i in range(0, n, 2):
        x = a + i * delta_x
        # x[i / 2] = a + i * delta_x
        subtotal_sum_1 += my_func(x[i / 2])
    # druga suma, pamiętamy że n = 2N
    for i in range(1, n - 1, 2):
        x = a + i * delta_x
        subtotal_sum_2 += my_func(x[i / 2])
    return delta_x * (total + 4 * subtotal_sum_1 + 2 * subtotal_sum_2) / 3


# Wywołujemy naszą funkcję całkującą, przekazując wzór całkowanej funkcji jako lambdę
integral = simpson_integration_modified(lambda x: x ** 3, 0.0, 1.0, 10**5)

print(integral)


def simpson_double_integration_first(my_func, y, a, b, n, index):
    f1 = my_func(a, y)
    f2 = my_func(b, y)
    delta_x = (b - a) / n
    subtotal_sum_1 = 0
    for i in range(index - 1, (n - 2) / 2):
        x = a + i * delta_x
        subtotal_sum_1 = my_func
