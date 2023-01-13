from math import factorial

import numpy as np


def coefficients(_x, _y):
    if len(_y) != len(_x):
        raise Exception('x and y of different lengths')

    N = len(_y)
    data = np.zeros((N, N))
    data[:, 0] = _y

    for j in range(1, N):
        for i in range(N - j):
            data[i][j] = (data[i + 1][j - 1] - data[i][j - 1]) / (_x[i + j] - _x[i])

    return data


def newton_poly(x, y, new_x):
    _coefficients = coefficients(x, y)
    p = _coefficients[0]
    for i in range(len(x)):
        for j in range(i):
            p[i] *= new_x - x[j]
    return sum(p)


def newton_many(new_x):
    return newton_poly(data_x, data_y, new_x)


def error(_f_11, x):
    apl = np.linspace(min(x), max(x), 20 * len(data_x))
    pr = np.linspace(0, 100, 20 * len(data_x))
    for i in x:
        pr = pr * abs(apl - i)
    _R = _f_11 * max(pr) / factorial(len(x))
    return _R


if __name__ == '__main__':
    import matplotlib.pyplot as plt

    """
    Начальные данные
    """
    f_11 = 1e-6
    data_y = np.array([0.00, 0.033, 0.067, 0.100, 0.133, 0.166, 0.199, 0.231, 0.264, 0.296, 0.327])
    data_x = np.linspace(0, 1, 11)
    x0 = 0.95
    print(f'y = {data_y}\nx = {data_x}')

    """
    Расчёт значения интерполяции с помощью полинома Ньютона для x0 = 0.95
    """
    y0 = newton_poly(data_x, data_y, x0)
    print(f'x0 = {x0}\ny0 = {y0}')

    """
    Расчёт значений интерполяции с помощью полинома Ньютона в большом количестве точек, чтобы увидеть график
    """
    x_pol = np.linspace(min(data_x), max(data_x), 10 * len(data_x))
    y_pol = list(map(newton_many, x_pol))

    """
    Расчёт ошибки вычислений
    |R(0.95)| = f_11 * П(0.95 - x[i]) / 11!
    """
    R = error(f_11, data_x)
    print(f'R({x0}) = {R}')

    plt.scatter(data_x, data_y)
    plt.scatter(x0, y0)
    plt.scatter(x_pol, y_pol, s=1)
    plt.grid()
    plt.show()
