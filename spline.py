import numpy as np
from math import sqrt, factorial


def cubic_spline(_x, _y, x_new):
    if len(_y) != len(_x):
        raise Exception('x and y of different lengths')

    N = len(_x)
    xdiff = np.diff(_x)
    ydiff = np.diff(_y)

    Li = np.empty(N)
    Li_1 = np.empty(N - 1)
    z = np.empty(N)

    Li[0] = sqrt(2 * xdiff[0])
    Li_1[0] = 0.0
    B0 = 0.0
    z[0] = B0 / Li[0]

    for i in range(1, N - 1, 1):
        Li_1[i] = xdiff[i - 1] / Li[i - 1]
        Li[i] = sqrt(2 * (xdiff[i - 1] + xdiff[i]) - Li_1[i - 1] * Li_1[i - 1])
        Bi = 6 * (ydiff[i] / xdiff[i] - ydiff[i - 1] / xdiff[i - 1])
        z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    i = N - 1
    Li_1[i - 1] = xdiff[-1] / Li[i - 1]
    Li[i] = sqrt(2 * xdiff[-1] - Li_1[i - 1] * Li_1[i - 1])
    Bi = 0.0
    z[i] = (Bi - Li_1[i - 1] * z[i - 1]) / Li[i]

    i = N - 1
    z[i] = z[i] / Li[i]
    for i in range(N - 2, -1, -1):
        z[i] = (z[i] - Li_1[i - 1] * z[i + 1]) / Li[i]

    index = _x.searchsorted(x_new)
    xi1, xi0 = _x[index], _x[index - 1]
    yi1, yi0 = _y[index], _y[index - 1]
    zi1, zi0 = z[index], z[index - 1]
    hi1 = xi1 - xi0

    f0 = zi0 / (6 * hi1) * (xi1 - x_new) ** 3 + zi1 / (6 * hi1) * (x_new - xi0) ** 3 + (yi1 / hi1 - zi1 * hi1 / 6) * (
            x_new - xi0) + (yi0 / hi1 - zi0 * hi1 / 6) * (xi1 - x_new)
    return f0


def error(_f_4, x, x_new):
    pr = ((x_new - x[-1]) * (x_new - x[-2])) ** 2
    _R = _f_4 * pr / factorial(4)
    return _R


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    """
    Начальные данные
    """
    f_4 = 0.1
    data_y = np.array([0.00, 0.033, 0.067, 0.100, 0.133, 0.166, 0.199, 0.231, 0.264, 0.296, 0.327])
    data_x = np.linspace(0, 1, 11)
    x0 = 0.95
    print(f'y = {data_y}\nx = {data_x}')

    """
    Расчёт значения интерполяции с помощью кубических сплайнов для x0 = 0.95
    """
    y0 = cubic_spline(data_x, data_y, x0)
    print(f'x0 = {x0}\ny0 = {y0}')

    """
    Расчёт значений интерполяции с помощью кубических сплайнов в большом количестве точек, чтобы увидеть график
    """
    x_pol = np.linspace(min(data_x), max(data_x), 100)
    y_pol = cubic_spline(data_x, data_y, x_pol)

    """
    Расчёт ошибки вычислений
    |R(0.95)| = f_4 * (0.95 - x[n])^2 (0.95 - x[n-1])^2} / 4!
    """
    R = error(f_4, data_x, x0)
    print(f'R({x0}) = {R}')

    plt.scatter(data_x, data_y)
    plt.scatter(x0, y0)
    plt.scatter(x_pol, y_pol, s=1)
    plt.grid()
    plt.show()
