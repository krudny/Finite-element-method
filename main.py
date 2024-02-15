from math import sqrt
import numpy as np
from matplotlib import pyplot as plot

def integral(f, a, b):
    width = (b - a) / 1000
    result = 0.0

    for i in range(1000):
        x = a + i * width + width / 2
        result += f(x) * width

    return result

def E(x): 
    if 0 <= x <= 1: return 2
    elif 1 < x <= 2: return 6
    else: return 0

def x_i(i, n): 
    return 2.0 * i / n

def e_i(i, x, n):
    h = 2/n
    if h*(i-1) <= x <= h*i:
        return x/h - i + 1
    elif h*i < x <= h*(i+1):
        return (-1)*x/h + i + 1
    return 0

def e_i_d(i, x, n):
    if x_i(i - 1, n) <= x <= x_i(i, n):
        return n / 2
    if x_i(i, n) < x < x_i(i + 1, n):
        return -1 * n / 2
    return 0

def l_v(i, x, n): 
    return -14 * e_i(i, 0, n)

def B_w_v(i, j, n): 
    f1 = lambda x: E(x) * e_i_d(i, x, n) * e_i_d(j, x, n)
    f2 = lambda x: E(x) * e_i_d(i, x, n) * e_i_d(j, x, n)

    return -2 * e_i(i, 0, n) * e_i(j, 0, n) + integral(f1, 0, 1) + integral(f2, 1, 2)

def u(alphas, x, n):
    result = 0
    for i in range(len(alphas)):
        result += alphas[i] * e_i(i, x, n)

    return result + 3

def main():
    n = int(input("Podaj n: "))
    A = []
    B = []

    for i in range(n): 
        A.append([])
        for j in range(n):
            A[i].append(B_w_v(j, i, n))

    for i in range(n):
        B.append(l_v(i, x_i(i, n), n))

    solution = np.linalg.solve(np.array(A), np.array(B))

    values = [u(solution, x_i(i, 100), n) for i in range(101)]

    x = np.linspace(0, 2, 101)
    plot.plot(x, values)
    plot.title("Wykres przybliżonej funkcji y = u(x)")
    plot.savefig("u(x).pdf")
    plot.show()

main()