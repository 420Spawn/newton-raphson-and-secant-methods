# Sitara Alayev 321967556
# Michael Fuks 304677438

import math


def samesign(a, b):
    return a * b > 0


def newtonRaphson(low, high, epsilon=0.0001):
    iteration = 0
    step = 1
    while low < high:
        if samesign(low, low + step):
            low += step
        else:
            x = low
            h = func(x) / derivFunc(x)
            while abs(h) > epsilon:
                h = func(x) / derivFunc(x)
                # x(i+1) = x(i) - f(x) / f'(x)
                x = x - h
                # print("The value of the current guess is : ", "%.4f" % x, 'The current iteration is:', iteration)
                iteration += 1
            low = high

            print("The value of the root is : ", "%.4f" % x, 'The iteration to find the root is:', iteration)


def func(x):
    return x ** 3 - x - 1


# Derivative of the above function
def derivFunc(x):
    return 3 * (x ** 2) - 1


# newtonRaphson(-100,100)

def secant_method(func, lower, upper, tolerance):
    step = 1
    while lower < upper:
        if samesign(lower, lower + step):
            lower += step
        else:
            iterations = 1
            while abs(upper - lower) > tolerance:
                current_iteration_print = "Iteration: {0}".format(iterations)
                next_point = upper - (func(upper) * (upper - lower)) / (func(upper) - func(lower))
                if func(next_point) == 0:
                    print(current_iteration_print + "Found exact solution: {0}".format(next_point))
                    return next_point
                lower = upper
                upper = next_point
                current_iteration_print += ", Current root approximation: {0}".format(next_point)
                iterations = iterations + 1
                # print(current_iteration_print)

            print("Final approximation: {0}".format(next_point), 'The iteration to find the root is:', iterations)
            return next_point


def f2(x):
    return x ** 3 - math.cos(x)


def menu():
    x = input("Please enter which method do you like to use:\n1.Newton Raphson method. \n2.Secant method\n")
    if x == '1':
        newtonRaphson(-100, 100)
    elif x == '2':
        print(secant_method(f2, 0, 1, 0.001))
    else:
        print("Invalid input")


# print(secant_method(f2, 0, 1, 0.001))


menu()
