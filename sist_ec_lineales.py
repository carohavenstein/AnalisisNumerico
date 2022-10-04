import numpy as np


# Metodo de eliminacion Gaussiana:
# paso 1: tranformar matriz extendida A|B en triangular sup -> triangular_sup(matriz)
# paso 2: sustitucion hacia atras
# controlar haciendo A * X obtenidas

def triangular_sup(matriz_a_triangular):
    
    matriz = np.copy(matriz_a_triangular)
    shape = matriz.shape
    for i in range(shape[0]-1):
        a = matriz[i][i]
        for j in range(i+1, shape[0]):
            n = matriz[j][i]
            m = n/a
            matriz[j] -= matriz[i] * m

    print("Matriz triangular sup: ")
    print(matriz)

    return matriz


def sustitucion_hacia_atras(triangulada):
    shape = triangulada.shape
    m = shape[0]
    n = shape[1]

    #incognitas
    x = np.zeros(n)
    
    """
        print("x", x) 
        print("shape: ", shape)
        print("m: ", m)
        print("n: ", n)
    """

    for i in range(m-1, -1, -1):
        b = triangulada[i][m-1]
        suma = 0
        for j in range(i+1, n):
            suma += triangulada[i][j]*x[j]
        
        x[i] = (triangulada[i][n-1]-suma)/triangulada[i][i]
    
    x = np.delete(x, n-1)
    print("x: ", x)
    return x


def control_eliminacion_gauss(A, B, respuestas):
    #al evaluar a con x(respuestas) obtenidas deberia dar parecido a b
    evaluacion = A@respuestas
    print("A*X = ", evaluacion)
    print("B: ", B)



if __name__=="__main__":

    A = np.array([
        [3, -0.1, -0.2],
        [0.1, 7, -0.3],
        [0.3, -0.2, 10]
    ], dtype=np.longdouble)

    B = [
        7.85, 19.30, 71.40
    ]

    ab = np.array([
        [3, -0.1, -0.2, 7.85],
        [0.1, 7, -0.3, 19.30],
        [0.3, -0.2, 10, 71.40]
    ], dtype=np.longdouble)

    triangulada = triangular_sup(ab)
    respuestas = sustitucion_hacia_atras(triangulada)
    control_eliminacion_gauss(A, B, respuestas)