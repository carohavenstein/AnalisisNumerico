import numpy as np


# Metodo de eliminacion Gaussiana:
# paso 1: tranformar matriz extendida A|B en triangular sup -> triangular_sup(matriz)
# paso 2: sustitucion hacia atras

def triangular_sup(matriz_a_triangular):
    """
    A | B
    recibe matriz extendida A|B
    la transforma en triangular sup
    """
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


def sustitucion_hacia_atras():
    pass



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