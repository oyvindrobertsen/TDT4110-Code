def polynom(x):
    return (x) ** 5 - 4*(x)**3 + 10*(x)**2 -10

def polynom_derivative(x):
    return 5*x**4 - 12*x**2 + 20*x

def newton(func, deriv, start, threshold, max_iterations):
    x = start
    x_prev = x + (10 * threshold)
    i = 0

    while abs(x - x_prev) > threshold and i < max_iterations:
        #print(i, x)
        i += 1
        x_prev = x
        x = x_prev - (func(x_prev)/deriv(x_prev))

    if abs(x - x_prev) <= threshold:
        return round(x, 6)
    else:
        return False


def main():
    print(newton(polynom, polynom_derivative, 1, 0.000001, 20))
    print(newton(polynom, polynom_derivative, -3, 0.000001, 20))
    print(newton(polynom, polynom_derivative, -1, 0.000001, 20))
    print(newton(polynom, polynom_derivative, 0.01, 0.000001, 20))
    print(newton(polynom, polynom_derivative, -2.08, 0.000001, 20))


main()
