import numpy as np
import scipy as sc


def f_y(x):
    return 1 / (1 + 25 * x ** 2)


def f_x(i, n):
    return -1 + 2 * i / (n + 1)


N = 10
x = np.zeros(N + 1)
y = np.zeros(N + 1)

for i in range(0, N + 1):
    # x.append(f_x(i, N))
    # y.append(f_y(x[i]))
    x[i] = f_x(i, N)
    y[i] = f_y(x[i])

# 1
# print(x)
# print(y)
a = np.zeros(N + 1)
for i in range(0, N + 1):
    a[i] = y[i]

# print(len(x), len(y), len(a))

# 2
b = np.zeros(N)
d = np.zeros(N)

# 3
h = np.zeros(N)
for i in range(0, N - 1):
    h[i] = x[i + 1] - x[i]

# 4
alpha = np.zeros(N)
for i in range(1, N - 1):
    alpha[i] = (3 * (a[i + 1] - a[i])) / h[i] - (3 * (a[i] - a[i - 1])) / h[i - 1]

# 5
c = np.zeros(N + 1)
l = np.zeros(N + 1)
m = np.zeros(N + 1)
z = np.zeros(N + 1)

# 6
l[0] = 1
m[0] = z[0] = 0

# 7
for i in range(1, N - 1):
    l[i] = 2 * (x[i + 1] - x[i - 1]) - h[i - 1] * m[i - 1]
    m[i] = h[i] / l[i]
    z[i] = (alpha[i] - h[i - 1] * z[i - 1]) / l[i]

# 8
l[N] = 1
z[N] = c[N] = 0

# 9
for j in range(N - 1, 0):
    c[j] = z[j] - m[j] * c[j + 1]
    b[j] = (a[j + 1] - a[j]) / h[j] - (h[j] * (c[j + 1] + 2 * c[j])) / 3
    d[j] = (c[j + 1] - c[j]) / 3 * h[j]

print(a, b, c, d, x)
