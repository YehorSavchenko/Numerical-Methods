import numpy as np
import math
import matplotlib.pyplot as plt
from scipy import interpolate


def cubic_interp1d(x0, x, y):
    """
    Interpolate a 1-D function using cubic splines.
      x0 : a float or an 1d-array
      x : (N,) array_like
          A 1-D array of real/complex values.
      y : (N,) array_like
          A 1-D array of real values. The length of y along the
          interpolation axis must be equal to the length of x.

    Implement a trick to generate at first step the cholesky matrice L of
    the tridiagonal matrice A (thus L is a bidiagonal matrice that
    can be solved in two distinct loops).

    additional ref: www.math.uh.edu/~jingqiu/math4364/spline.pdf 
    """
    size = len(x)

    xdiff = np.diff(x)
    ydiff = np.diff(y)

    # allocate buffer matrices
    Li = np.empty(size)
    Li_1 = np.empty(size - 1)
    z = np.empty(size)

    # fill diagonals Li and Li-1 and solve [L][y] = [B]
    Li[0] = math.sqrt(2 * xdiff[0])
    Li_1[0] = 0.0
    B0 = 0.0  # natural boundary
    z[0] = B0 / Li[0]

    for i in range(1, size - 1, 1):
        Li_1[i] = xdiff[i - 1] / Li[i - 1]
        Li[i] = math.sqrt(2 * (xdiff[i - 1] + xdiff[i]) - Li_1[i - 1] * Li_1[i - 1])
        Bi = 6 * (ydiff[i] / xdiff[i] - ydiff[i - 1] / xdiff[i - 1])
        z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    i = size - 1
    Li_1[i - 1] = xdiff[-1] / Li[i - 1]
    Li[i] = math.sqrt(2 * xdiff[-1] - Li_1[i - 1] * Li_1[i - 1])
    Bi = 0.0  # natural boundary
    z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    # solve [L.T][x] = [y]
    i = size - 1
    z[i] = z[i] / Li[i]
    for i in range(size - 2, -1, -1):
        z[i] = (z[i] - Li_1[i - 1] * z[i + 1]) / Li[i]

    # find index
    index = x.searchsorted(x0)
    np.clip(index, 1, size - 1, index)

    xi1, xi0 = x[index], x[index - 1]
    yi1, yi0 = y[index], y[index - 1]
    zi1, zi0 = z[index], z[index - 1]
    hi1 = xi1 - xi0

    # calculate cubic
    f0 = zi0 / (6 * hi1) * (xi1 - x0) ** 3 + \
         zi1 / (6 * hi1) * (x0 - xi0) ** 3 + \
         (yi1 / hi1 - zi1 * hi1 / 6) * (x0 - xi0) + \
         (yi0 / hi1 - zi0 * hi1 / 6) * (xi1 - x0)
    return f0


def f_y_1(x):
    return 1 / (1 + 25 * x ** 2)


def f_x_a(i, n):
    return -1 + (2 * i) / n


def init(f_x, f_y, N, x1, y1):
    x1.clear()
    y1.clear()
    for i in range(N):
        x1.append(f_x(i, N))
        y1.append(f_y(x[i]))


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    N = 5
    N1 = 5
    x1 = []
    y1 = []
    x = np.array(N)
    y = np.array(N)
    for i in range(0, N+1):
        print(i)
        x1.append(f_x_a(i, N))
        y1.append(f_y_1(x1[i]))
    x = np.array(x1)
    y = np.array(y1)

    print(x)
    print(y)

    plt.scatter(x, y)
    # x_new = np.linspace(-1, 1, N1)
    x_new = np.arange(-1.0, 1.0, 0.1)

    f = interpolate.CubicSpline(x, y)
    # plt.plot(x_new, f(x_new), 'r')
    # a powinno to wyglądać tak
    plt.xlim(-1, 1)
    plt.ylim(-1, 2)
    plt.plot(x_new, f_y_1(x_new), 'r')
    plt.plot(x_new, cubic_interp1d(x_new, x, y), 'g')
    plt.show()
