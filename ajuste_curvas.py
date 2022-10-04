import math
import numpy as np
import sympy as sp

# Rgresion lineal por minimos cuadrados
def regresion_lineal_min_cuadrados(xi, yi):
    if len(xi) == len(yi):
        n = len(xi)                               # cantidad de puntos (xi, yi)
        xi_square = []
        xi_yi = []
        for i in range(1, n + 1):
            xi_square.append(xi[i - 1] ** 2)
            xi_yi.append(xi[i - 1] * yi[i - 1])
        print('xi: {}'.format(xi))
        print('yi: {}'.format(yi))
        print('xi square: {}'.format(xi_square))
        print('xiyi: {}'.format(xi_yi))

        print('Sum xi = {}'.format(sum(xi)))
        print('Sum yi = {}'.format(sum(yi)))
        print('Sum xi square = {}'.format(sum(xi_square)))
        print('Sum xiyi = {}'.format(sum(xi_yi)))

        a1 = ((n * sum(xi_yi) - sum(xi) * sum(yi)) / (n * sum(xi_square) - (sum(xi)) ** 2))
        a0 = np.mean(yi) - a1 * np.mean(xi)

        print('a1 = {}'.format(a1))
        print('a0 = {}'.format(a0))

        print('y = {}x + {}'.format(a1, a0))
    else:
        print('Error')


# Modelo exponencial
# y = A.e**(B.x)
def modelo_exp(xi, yi):
    if len(xi) == len(yi):
        n = len(xi)                             # cantidad de puntos (xi, yi)
        ln_yi = []
        xi_square = []
        xi_ln_yi = []
        for i in range(1, n + 1):
            ln_yi.append(np.log(yi[i - 1]))
            xi_square.append(xi[i - 1] ** 2)
            xi_ln_yi.append(xi[i - 1] * ln_yi[i - 1])
        print('xi: {}'.format(xi))
        print('yi: {}'.format(yi))
        print('lnyi: {}'.format(ln_yi))
        print('xi square: {}'.format(xi_square))
        print('xiyi: {}'.format(xi_ln_yi))

        print('Sum xi = {}'.format(sum(xi)))
        print('Sum lnyi = {}'.format(sum(ln_yi)))
        print('Sum xi square = {}'.format(sum(xi_square)))
        print('Sum xilnyi = {}'.format(sum(xi_ln_yi)))

        a1 = ((n * sum(xi_ln_yi) - sum(xi) * sum(ln_yi)) / (n * sum(xi_square) - (sum(xi)) ** 2))
        a0 = np.mean(ln_yi) - a1 * np.mean(xi)

        A = math.e ** a0
        B = a1

        print('a0 = {}'.format(a0))
        print('a1 = B = {}'.format(a1))
        print('A = {}'.format(A))

        print('y = {} . e**{}x'.format(A, B))
    else:
        print('Error')


# Modelo potencial
# y = A.x**B
def modelo_potencial(xi, yi):
    if len(xi) == len(yi):
        n = len(xi)                     # cantidad de puntos (xi, yi)
        log_xi = []
        log_yi = []
        log_xi_square = []
        log_xi_log_yi = []
        for i in range(1, n + 1):
            log_xi.append(math.log10(xi[i - 1]))
            log_yi.append(math.log10(yi[i - 1]))
            log_xi_square.append(log_xi[i - 1] ** 2)
            log_xi_log_yi.append(log_xi[i - 1] * log_yi[i - 1])
        print('xi: {}'.format(xi))
        print('log xi: {}'.format(log_xi))
        print('yi: {}'.format(yi))
        print('log yi: {}'.format(log_yi))
        print('log xi square: {}'.format(log_xi_square))
        print('log xi * log yi: {}'.format(log_xi_log_yi))

        print('Sum log xi = {}'.format(sum(log_xi)))
        print('Sum log yi = {}'.format(sum(log_yi)))
        print('Sum log xi square = {}'.format(sum(log_xi_square)))
        print('Sum log xi * log yi = {}'.format(sum(log_xi_log_yi)))

        a1 = ((n * sum(log_xi_log_yi) - sum(log_xi) * sum(log_yi)) / (n * sum(log_xi_square) - (sum(log_xi)) ** 2))
        a0 = np.mean(log_yi) - a1 * np.mean(log_xi)

        A = 10 ** a0
        B = a1

        print('a0 = {}'.format(a0))
        print('a1 = B = {}'.format(a1))
        print('A = {}'.format(A))

        print('y = {} . x**{}'.format(A, B))
    else:
        print('Error')


# Modelo de crecimiento
# y = A * (x / (b + x))
def modelo_crecimiento(xi, yi):
    if len(xi) == len(yi):
        n = len(xi)                     # cantidad de puntos (xi, yi)
        xi_inv = []
        yi_inv = []
        xi_inv_square = []
        xi_inv_yi_inv = []
        for i in range(1, n + 1):
            xi_inv.append((1 / xi[i - 1]))
            yi_inv.append(1 / (yi[i - 1]))
            xi_inv_square.append(xi_inv[i - 1] ** 2)
            xi_inv_yi_inv.append(xi_inv[i - 1] * yi_inv[i - 1])
        print('xi: {}'.format(xi))
        print('Inverse xi: {}'.format(xi_inv))
        print('yi: {}'.format(yi))
        print('Inverse yi: {}'.format(yi_inv))
        print('Inverse xi square: {}'.format(xi_inv_square))
        print('Inverse xi * inverse yi: {}'.format(xi_inv_yi_inv))

        print('Sum inverse xi = {}'.format(sum(xi_inv)))
        print('Sum inverse yi = {}'.format(sum(yi_inv)))
        print('Sum inverse xi square = {}'.format(sum(xi_inv_square)))
        print('Sum inverse xi * inverse yi = {}'.format(sum(xi_inv_yi_inv)))

        a1 = ((n * sum(xi_inv_yi_inv) - sum(xi_inv) * sum(yi_inv)) / (n * sum(xi_inv_square) - (sum(xi_inv)) ** 2))
        a0 = np.mean(yi_inv) - a1 * np.mean(xi_inv)

        A = 1 / a0
        B = A * a1

        print('a0 = {}'.format(a0))
        print('a1 = {}'.format(a1))
        print('A = {}'.format(A))
        print('B = {}'.format(B))

        print('y = {} . (x / ({} + x))'.format(A, B))
    else:
        print('Error')

"""
# Interpolacion polinomial de Newton
def interpolacion_polinom_newton(xi, yi):
    pass
    for n in range(0, len(xi)):
        if n == 0:
            fn(x) = f(xo)
        if n == 1:
            fn(x) += f[x1,x0](x-x0)
        if n == 2:
            fn(x) += f[x2,x1,x0](x-x0)(x-x1)
"""

# Polinomio de Lagrange
def polinomio_lagrange(x_puntos, y_puntos):
    
    x = sp.Symbol('x')

    n = len(x_puntos)
    p_lagrange = 0              # elemento neutro suma

    for i in range(n):
        li = 1                  #elemento neutro multiplicacion
        for j in range(0, n):   
            if j != i:
                li *= ((x-x_puntos[j])/(x_puntos[i]-x_puntos[j]))
                p_lagrange += li * y_puntos[i]
    
    p_lagrange = sp.simplify(p_lagrange)

    # grado del polinomio de lagrange es la mayor potencia de x
    print("Polinomio Lagrange: ", p_lagrange)
    # evaluar polinomio lagrange en puntos x dados
    

    for i in range(n):
        evaluar = x_puntos[i]
        print("Polinomio Lagrange valuado en ", x_puntos[i], ": ", p_lagrange.subs(x, evaluar))
    

# Trazadoras cúbicas
def trazadora_cubica_natural(x, y, h):

    w = sp.Symbol('w')

    n = len(x)
    print("n:", n)
    alfa = []
    
    # tomo i[0] = 1, mu[0] = 0, z[0] = 0
    i = [1]
    mu = [0]
    z = [0]

    for j in range(1, n-1):
        alfa.append((3/h[j])*(y[j+1]-y[j])-(3/h[j-1])*(y[j]-y[j-1])) 
        i.append(2*(x[j+1]-x[j-1])-h[j-1]*mu[j-1])
        mu.append(h[j]/i[j])
        z.append((alfa[j-1]-h[j-1]*z[j-1])/i[j])

    print("alfa: ", alfa)
    print("I: ", i)
    print("mu: ", mu)
    print("z: ", z)

    # tomo i[n] = 1, z[n] = 0, c[n] = 0
    i.append(1)
    z.append(0)


    c = np.zeros(n)
    b = []
    d = []

    for i in range(n-2, -1, -1):
        c[i] = (z[i]-mu[i]*c[i+1])
        b.append((y[i+1]-y[i])/h[i]-h[i]*(c[i+1]+2*c[i])/3)
        d.append((c[i+1]-c[i])/3*h[i])


    print("c: ", c)
    b = list(reversed(b))
    print("b: ", b)
    d = list(reversed(d))
    print("d: ", d)

    polinomio = 0
    for i in range(n-1):
        polinomio = y[i] + b[i]*(w - x[i]) + c[i]*(w - x[i])**2 + d[i]*(w - x[i])**3
        polinomio = sp.simplify(polinomio)
        print("Polinomio ", i, ": ", polinomio)



if __name__ == '__main__':
    
    xi_lls = [1, 2, 3, 4, 5, 6, 7]
    yi_lls = [0.50, 2.50, 2.00, 4.00, 3.50, 6.00, 5.50]
    regresion_lineal_min_cuadrados(xi_lls, yi_lls)

    xi_exp = [1, 2, 3, 4, 5]
    yi_exp = [0.5, 1.7, 3.4, 5.7, 8.4]
    modelo_exp(xi_exp, yi_exp)
    modelo_potencial(xi_exp, yi_exp)
    modelo_crecimiento(xi_exp, yi_exp)
    
    # para polinomio de lagrange
    x_puntos = [0.00, 1.00, 2.00, 3.00]
    y_puntos = [1.00, 2.7182, 7.3891, 20.0855]
    polinomio_lagrange(x_puntos, y_puntos)

    
    # para trazadora cubica
    x = [0.0, 1.0, 2.0, 3.0]
    y = [1.0, 2.7182, 7.3891, 20.0855]
    h = [1.0, 1.0, 1.0]

    trazadora_cubica_natural(x, y, h)