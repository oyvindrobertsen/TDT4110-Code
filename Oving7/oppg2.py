from math import exp

def expfunc(x):
    return exp(-x**2)

def simpson(func, a, b, h):

    n = float(b - a) / h
    S = func(a)

    for i in range(1, h, 2):
        x = a + n * i
        S += 4 * func(x)

    for i in range(2, h-1, 2):
        x = a + n * i
        S += 2 * func(x)

    S += func(b)
    F = n * S / 3

    return F

def simpson_error(func, a, b, error):
    i = 1
    while abs(simpson(func, a, b, 2**i) - simpson(func, a, b, 2**(i+1))) > error:
        i += 1

    return simpson(func, a, b, 2**i)

def main():
    print(simpson(expfunc, 0, 1, 1000))
    print(simpson_error(expfunc, 0, 1, 0.00000001))

main()
