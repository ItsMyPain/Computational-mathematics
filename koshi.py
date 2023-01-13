import numpy as np
import matplotlib.pyplot as plt

a = 0
b = np.pi
h = 1e-1


def f(x, y):
    return x * y


def k1(fn, x, y):
    return fn(x, y)


def k2(fn, x, y, _h):
    return fn(x + _h / 2, y + _h * k1(fn, x, y) / 2)


def k3(fn, x, y, _h):
    return fn(x + _h / 2, y + _h * k2(fn, x, y, _h) / 2)


def k4(fn, x, y, _h):
    return fn(x + _h, y + _h * k3(fn, x, y, _h))


def yi1(fn, x, yi, _h):
    return yi + h * (k1(fn, x, yi) + 2 * k2(fn, x, yi, _h) + 2 * k3(fn, x, yi, _h) + k4(fn, x, yi, _h)) / 6


def main():
    X = np.linspace(0, 1, 20)
    Y = np.array([0])
    for i in range(len(X) - 1):
        Y = np.append(Y, yi1(f, X[i], Y[i], h))

    plt.plot(X, Y)
    plt.show()


main()
