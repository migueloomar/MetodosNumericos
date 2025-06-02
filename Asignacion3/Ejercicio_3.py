"""
N.-03) Desarrolle un programa amigable para el usuario, en cualquier lenguaje de alto nivel 
o macros que elija, para realizar la descomposición LU de Gauss ([A] = [L][U]) y pruébelo 
con el siguiente sistema:

    x_1 +  2x_2 -  x_3 =  2
    5x_1 + 2x_2 +  2x_3 =  9
   -3x_1 + 5x_2 -  x_3 =  1
"""

from decimal import Decimal, getcontext
import numpy as np

# Establece precisión decimal de 4 dígitos

getcontext().prec = 4

# Función: decomposicion_de_gauss(A)
# Realiza la descomposición LU sin pivoteo

def decomposicion_de_gauss(A):
    n = len(A)                      # Tamaño de la matriz
    L = np.eye(n, dtype=Decimal)    # Inicializa L como la matriz identidad
    U = A.copy()                    # Copia de A para trabajar como matriz U            

    # Archivo para guardar el desarrollo del proceso
    with open('resultados_3.txt', 'w') as file:
        file.write("Matriz A:\n")
        file.write(str(A))
        file.write("\n\nDescomposición de Gauss:\n")

        # Eliminación de Gauss: convierte A en una matriz triangular superior U
        # y construye la matriz L con los factores de eliminación
        for k in range(n):
            for j in range(k+1, n):
                factor = U[j, k] / U[k, k]      # Cálculo del factor de eliminación
                L[j, k] = factor                # Asigna el factor a la posición correspondiente en L
                U[j, k:] -= factor * U[k, k:]   # Operación de eliminación sobre U
            
            # Guarda los pasos intermedios en el archivo
            file.write(f"\nPaso {k + 1}:\n")
            file.write(f"\nMatriz L:\n{L}\n")
            file.write(f"\nMatriz U:\n{U}\n")

    return L, U # Devuelve las matrices L y U

# Función: solucion(L, U, b)
# Resuelve el sistema Ax = b usando la factorización LU

def solucion(L, U, b):
    n = len(b)                          # Tamaño del sistema
    y = np.zeros(n, dtype=Decimal)      # Vector auxiliar para Ly = b
    final = np.zeros(n, dtype=Decimal)  # Vector solución final para Ux = y

    # Sustitución hacia adelante (Ly = b)
    for i in range(n):
        y[i] = b[i] - np.dot(L[i, :i], y[:i])

    # Sustitución hacia atrás (Ux = y)
    for i in range(n-1, -1, -1):
        final[i] = (y[i] - np.dot(U[i, i+1:], final[i+1:])) / U[i, i]

    return final                        # Retorna la solución del sistema

# Entrada de datos desde el usuario
# Solicita el tamaño de la matriz cuadrada

n = int(input("Ingrese el tamaño de la matriz cuadrada (Escriba solo el número, ejemplo: 3): "))

# Entrada de la matriz A

print("Ingrese la matriz A:")
A = np.zeros((n, n), dtype=Decimal)
for i in range(n):
    for j in range(n):
        A[i, j] = Decimal(input(f"A[{i+1},{j+1}]: "))

# Entrada del vector b

print("\nIngrese el vector b:")
b = np.zeros(n, dtype=Decimal)
for i in range(n):
    b[i] = Decimal(input(f"b[{i+1}]: "))

# Ejecución de la descomposición y resolución

L, U = decomposicion_de_gauss(A)    # Obtención de matrices L y U
final = solucion(L, U, b)           # Solución del sistema usando LU

# Guarda el resultado final en el archivo

with open('resultados_3.txt', 'a') as file:
    file.write("\n\nSolución del sistema:\n")
    file.write(str(final))

print("Resultados guardados en 'resultados_3.txt'")
