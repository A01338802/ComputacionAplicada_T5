import numpy as np
import math
from random import random
from random import gauss
from matplotlib import pyplot as plt
from matplotlib import cm
from mpl_toolkits.mplot3d import Axes3D


def f(x1, x2, x3):
    f = x1 + 2 * x2 + x2 * x3 - x1 ** 2 - x2 ** 2 - x3 ** 2
    return f


def evol(u, v, w):
    plt.figure(3)
    plt.plot(u)
    plt.plot(v)
    plt.plot(w)
    plt.legend(('x1', 'x2', 'x3'))
    plt.ylim([-2, 2])
    plt.show()

def path3d(u, v, w):
    plt.figure(1)
    ax = plt.axes(projection='3d')  # ax definition
    ax.plot3D(u, v, w, 'red')
    # labeling
    ax.set_xlabel("x1")
    ax.set_ylabel("x2")
    ax.set_zlabel("x3")
    plt.title('Función Objetivo')

def mutation(x, s):
    xn = x + s * gauss(0, 1)
    while xn < -2 or xn > 2:
        xn = x + s * gauss(0, 1)
    return xn


def sigma(s, g, m):
    ps = m / g
    c = 0.817
    if g % 20 == 0:
        # if True:
        if ps > 0.2:
            s = s / c
        elif ps < 0.2:
            s = s * c
        else:
            s = s
    else:
        s = s
    return s


def main():
    xmin = -2
    gmax = 100000
    m = 0
    x1 = 4 * random() + xmin
    x2 = 4 * random() + xmin
    x3 = 4 * random() + xmin
    xz = [round(x1, 6), round(x2, 6), round(x3, 6)]
    print("x1_0,x2_0,x3_0: ", xz)
    padre = f(x1, x2, x3)
    s = 1
    u = [x1]
    v = [x2]
    w = [x3]

    for g in range(1, gmax):
        x1_n = mutation(x1, s)
        x2_n = mutation(x2, s)
        x3_n = mutation(x3, s)
        hijo = f(x1_n, x2_n, x3_n)
        if hijo > padre:
            x1 = x1_n
            x2 = x2_n
            x3 = x3_n
            m += 1  # mutación exitosa
            padre = f(x1, x2, x3)
        else:
            x1 = x1
            x2 = x2
            x3 = x3
            m = m
        s = sigma(s, g, m)
        u.append(x1)
        v.append(x2)
        w.append(x3)

    xzf = [round(x1, 6), round(x2, 6), round(x3, 6)]
    print("xf,yf: ", xzf)
    evol(u, v, w)
    path3d(u, v, w)


main()