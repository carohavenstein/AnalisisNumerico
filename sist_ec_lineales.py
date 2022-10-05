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


def control(A, B, respuestas):
    #al multiplicar a con x(respuestas obtenidas) deberia dar parecido a b
    multiplicacion = A@respuestas
    print("A*X = ", multiplicacion)
    print("B: ", B)


# Método de Gauss-Seidel
def gauss_seidel(A, B, error_programado):
    shape = A.shape
    m = shape[0]
    n = shape[1]

    for i in range(m):
        if A[i][i] == 0:
            print("Error: El elemento A[{}][{}] = 0".format(i, i))
            return None
    
    print('No hay elementos nulos en la diagonal principal')

    #incognitas
    x_anterior = np.zeros(n)

    x = [float("inf")] * m
    contador = 0

    while np.any(np.abs((x - x_anterior)) > error_programado):
        print('error ciclo {}: {}'.format(contador, np.abs((x - x_anterior))))
        for i in range(m):
            x[i] = x_anterior[i]
            suma = sum(A[i][j]*x_anterior[j] for j in range(m) if j != i)
            x_anterior[i] = (B[i]- suma)/A[i][i]
        print('x ciclo {}: {}'.format(contador, x))
        contador += 1
    
    print('error ciclo {}: {}'.format(contador, np.abs((x - x_anterior))))

# Metodo de LU
def lu(a, b):
    n = a.shape[0]
    u = np.copy(a)
    l = np.identity(n)
    for i in range(n):
        for j in range(i+1, n):
            l[j][i] = u[j][i] / u[i][i]
            u[j] -= u[i] * l[j][i]
    
    print('L: {}'.format(l))
    print('U: {}'.format(u))

    # L * y = b -> sustitucion hacia adelante
    lb = np.c_[l, b]
    n = lb.shape[0]
    m = lb.shape[1]
    y = np.zeros(n)
    for i in range(n):
        b = lb[i][m-1]
        s = sum([lb[i][j] * y[j] for j in range(n)])
        y[i] = (b - s) / lb[i][i]
    print('y: ', y)

    # U * x = y -> sustitucion hacia atras
    uy = np.c_[u, y]
    x = sustitucion_hacia_atras(uy)

    # verifico resultados obtenidos
    control(a, B, x)


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
    """
    triangulada = triangular_sup(ab)
    respuestas = sustitucion_hacia_atras(triangulada)
    control(A, B, respuestas)

    error_programado = 0.001
    gauss_seidel(A, B, error_programado)
    """
    lu(A, B)