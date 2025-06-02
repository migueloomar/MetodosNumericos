"""
N.-02) Desarrolle, depure y pruebe un programa en el lenguaje de alto nivel o macros 
que prefiera, para resolver un sistema de ecuaciones mediante eliminación de Gauss 
con pivoteo parcial. Pruebe el programa con el siguiente sistema, cuya solución es:

    x_1 +  2x_2 -  x_3 =  2
    5x_1 + 2x_2 +  2x_3 =  9
   -3x_1 + 5x_2 -  x_3 =  1

"""

import numpy as np
from decimal import Decimal, getcontext

# Se establece la precisión decimal a 4 dígitos significativos

getcontext().prec = 4

# Función principal: eliminación_de_gauss_por_pivote
# - Realiza el pivoteo parcial por filas
# - Aplica eliminación hacia adelante
# - Aplica sustitución hacia atrás
# - Registra cada paso en un archivo

def eliminacion_de_gauss_por_pivote(A, b):
    n = len(b)                                                          # Dimensión del sistema
    x = np.zeros(n, dtype=Decimal)                                      # Vector solución inicializado en ceros

    with open('resultados_2.txt', 'w') as file:
        for k in range(n - 1):                                          # Eliminación hacia adelante con pivoteo parcial
            valor_abs_maximo = np.argmax(np.abs(A[k:, k])) + k          # Selección del pivote (máximo valor absoluto en columna k)
            if k != valor_abs_maximo:                                   # Intercambio de filas en A y b si es necesario
                A[[k, valor_abs_maximo]] = A[[valor_abs_maximo, k]]
                b[k], b[valor_abs_maximo] = b[valor_abs_maximo], b[k]
            
            # Registro del estado actual de A y b
            file.write(f'\nPaso {k + 1}:\n')
            file.write(f'Matriz A:\n{A}\n')
            file.write(f'\nVector b:\n{b}\n')

            # Eliminación hacia adelante (convertir A en triangular superior)
            for i in range(k + 1, n):
                factor = A[i, k] / A[k, k]
                b[i] -= factor * b[k]
                A[i, k:] -= factor * A[k, k:]
                
                # Registro del proceso fila por fila
                file.write(f'\nOperaciones en fila {i}:\n')
                file.write(f'\nMatriz A:\n{A}\n')
                file.write(f'\nVector b:\n{b}\n')

        # Sustitución hacia atrás para resolver el sistema triangular superior
        for k in range(n - 1, -1, -1):
            x[k] = (b[k] - np.sum(A[k, k + 1:] * x[k + 1:])) / A[k, k]
            
            # Registro de cada paso de sustitución
            file.write(f'\nSustitución hacia atrás, paso {n - k}:\n')
            file.write(f'Solución x_{k + 1}: {x[k]}\n')

    return x    # Devuelve el vector de soluciones

# Solicita el tamaño de la matriz cuadrada

n = int(input("Ingrese el tamaño de la matriz cuadrada (Escriba solo el numero, ejemplo: 3): "))

print("Ingrese la matriz A:")   # Entrada de la matriz A
A = np.zeros((n, n), dtype=Decimal)
for i in range(n):
    for j in range(n):
        A[i, j] = Decimal(input(f"A[{i+1},{j+1}]: "))

print("Ingrese el vector b:")   # Entrada del vector b
b = np.zeros(n, dtype=Decimal)
for i in range(n):
    b[i] = Decimal(input(f"b[{i+1}]: "))

# Impresión de la matriz A y vector b
print("Matriz A:")
print(A)
print("Vector b:")
print(b)

# Visualización del sistema de ecuaciones ingresado
print('\nSistema de ecuaciones:')
for i in range(n):
    sistema_ecuaciones = ' + '.join(f'{A[i, j]:.1f}x_{j+1}' for j in range(n))
    sistema_ecuaciones += f' = {b[i]:.1f}'
    print(sistema_ecuaciones)

# Ejecución del método de eliminación de Gauss
Resultado = eliminacion_de_gauss_por_pivote(A, b)

# Imprime las soluciones 
print('\nEl resultado: ', Resultado)
