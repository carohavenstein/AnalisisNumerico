import math
import numpy as np


# Metodo de Biseccion
def biseccion(a, b, programmed_error, f):

    print("Metodo de biseccion: ")

    c = (a + b) / 2
    error = programmed_error + 1

    print('a', 'b', 'c', 'f(a)', 'f(c)', 'f(a)*f(c) > 0', 'Error')
    print(a, b, c, f(a), f(c), f(a) * f(c) > 0, '-')

    if f(a) * f(c) < 0:
        b = c
    else:
        a = c

    c_prev = c

    while programmed_error < error:
        
        c = (a + b) / 2
        error = abs(c - c_prev)
        c_prev = c
        
        print(a, b, c, f(a), f(c), f(a) * f(c) > 0, error)

        if f(a) * f(c) < 0:
            b = c
        else:
            a = c

    print("Raiz biseccion: ", c)


# Metodo del punto fijo
def punto_fijo(a, b, programmed_error, g):

    print("Metodo del punto fijo: ")
    
    #para obtener g(x), f(x)=0 y despejo x o sumo x a ambos lados
    #verificar que g(x) converge:
        # g(a) esta en [a,b] y g(b) esta en [a, b]
        # |g'(E)| <= 1  con E perteneciente a [a, b] y que maximice g'

    x = a
    g_x = g(x)
    print('xi', 'g(xi)', '|E|')
    print(x, g_x, '-')
    error = abs(b - a)
    while programmed_error < error:
        x_prev = x
        x = g_x
        g_x = g(x)
        error = abs(x - x_prev)
        print(x, g_x, error)

    print("Raiz punto fijo: ", x)


# Metodo de Newton Raphson
def newton_raphson(a, programmed_error, f, f_prime):
    
    print("Metodo de Newton Raphson: ")

    xi = a
    i = 0
    error = programmed_error + 1

    print('i', 'xi', 'f(xi)', "f'(xi)", '|E|')
    print(i, xi, f(xi), f_prime(xi), '-')

    while programmed_error <= error:
        x_next = xi - (f(xi) / f_prime(xi))
        error = abs(x_next - xi)
        xi = x_next
        f_xi = f(xi)
        f_prime_xi = f_prime(xi)
        i += 1
        print(i, xi, f(xi), f_prime(xi), error)

    print("Raiz Newton Raphson: ", xi)


# Metodo de la secante
def secante(a, b, programmed_error, f):

    print("Metodo de la secante: ")

    x_prev = a
    xi = b
    i = 0
    error = programmed_error + 1

    print('i', 'xi', 'f(xi)', '|E|')
    print(i, x_prev, f(x_prev), '-')
    i += 1
    print(i, xi, f(xi), '-')

    while programmed_error <= error:
        x_next = xi - (f(xi) * (x_prev - xi)) / (f(x_prev) - f(xi))
        error = abs(x_next - xi)
        x_prev = xi
        xi = x_next
        f_xi = f(xi)
        i += 1
        print(i, xi, f(xi), error)

    print("Raiz secante: ", xi)


if __name__=="__main__":
    
    def f(x):
        return (math.e ** (- x)) - x


    def g(x):
        return math.e ** (- x)


    def f_prime(x):
        return (-math.e ** (-x)) - 1    

    a = float(input('Insert a: '))
    b = float(input('Insert b: '))
    programmed_error = float(input('Insert programmed error: '))

    biseccion(a, b, programmed_error, f)
    punto_fijo(a, b, programmed_error, g)
    newton_raphson(a, programmed_error, f, f_prime)
    secante(a, b, programmed_error, f)

    