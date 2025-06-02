'''
N.-05) Desarrolle un programa amigable para el usuario, en cualquier lenguaje de alto nivel 
o de macros que escoja, para implementar la técnica iterativa de Jacobi. 
Pruebe el programa con el siguiente sistema (cuya solución es x_1 = 1, x_2 = 2, x_3 = -1, x_4 = 1). 
Utilice como criterio de paro un número máximo de iteraciones:

    10x_1 -  x_2   +  2x_3          =  6
    -x_1  + 11x_2  -  x_3   + 3x_4  =  25
    2x_1  -  x_2   + 10x_3  - x_4   = -11
             3x_2  -  x_3   + 8x_4  =  15
'''

import numpy as np
from decimal import Decimal, getcontext
import csv

# Aritmetica de 4 dígitos
getcontext().prec = 4

# Función: CondicionNecesaria(A)
# Verifica si la matriz A es diagonalmente dominante
def CondicionNecesaria(A):
      
    n = A.shape[0]      # n obtiene el numero de filas de [A]  
    
    # Verifica fila por fila si cumple con la condición:
    # |a_ii| > suma de |a_ij| para j ≠ i

    for i in range(n):
        diagonal = abs(A[i, i])                         # Valor absoluto del elemento diagonal
        diagonalnt = sum(map(abs, A[i, :])) - diagonal  # Suma de la fila menos el diagonal
        if diagonal <= diagonalnt:
            return False                                # Si no cumple, retorna False
    return True                                         # Si todas las filas cumplen, retorna True

# Función: jacobi(A, b, x0, max_iter, tol)
# Implementa el método iterativo de Jacobi

def jacobi(A, b, x0, max_iter, tol=Decimal('1e-4')):
    # Verifica condición de convergencia (diagonal dominante)
    if not CondicionNecesaria(A):
        print("La matriz no es diagonalmente dominante. La convergencia no está garantizada.")
        return None

    diagonal = np.diag(A)                           # Extrae la diagonal de A
    matriz_no_diagonal = A - np.diagflat(diagonal)  # Resta la diagonal de A para obtener la parte no diagonal
    solucion_actual = x0                            # Inicializa con la solución inicial proporcionada (x0)


    # Ciclo de iteraciones
    for i in range(max_iter):

        # Aplica la fórmula de Jacobi para obtener nueva solución
        solucion_nueva = (b - np.dot(matriz_no_diagonal, solucion_actual)) / diagonal
        
        # Condición de paro si el cambio es menor que la tolerancia
        if all(abs(solucion_nueva - solucion_actual) < tol):
            return solucion_nueva
        
        # Actualiza la solución para la siguiente iteración
        solucion_actual = solucion_nueva

    return solucion_actual      # Retorna la última solución (aunque no haya convergido)

# Entrada de datos por el usuario
# Solicita el tamaño de la matriz cuadrada

n = int(input("Ingrese el tamaño de la matriz cuadrada (Escriba solo el número, ejemplo: 3): "))

# Entrada de la matriz A

print("Ingrese la matriz A:")
A = np.zeros((n, n), dtype=Decimal)
for i in range(n):
    for j in range(n):
        A[i, j] = Decimal(input(f"A[{i+1},{j+1}]: "))

# Entrada del vector b

print("Ingrese el vector b:")
b = np.zeros(n, dtype=Decimal)
for i in range(n):
    b[i] = Decimal(input(f"b[{i+1}]: "))

# Vector inicial x0 con ceros
x0 = np.zeros(n, dtype=Decimal)

# Número máximo de iteraciones
max_iter = 1000

# Ejecuta el método de Jacobi
Vector_solucion_inicial = jacobi(A, b, x0, max_iter)

# Guardado de resultados en archivo CSV
csv_file = "resultados_5.csv"

# comprueba que el vector solucion inicial no sea none, 
# si lo es se crea y completa los resultados en el csv

if Vector_solucion_inicial is not None:
    with open(csv_file , 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Variable", "Valor"])
        for i, val in enumerate(Vector_solucion_inicial):
            csv_writer.writerow([f'x_{i + 1}', f'{val:.4f}'])

        csv_writer.writerow([])  

        # Escribe la matriz A
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["Matriz A"])
        for i in range(n):
            csv_writer.writerow([str(valor) for valor in A[i]])

        # Escribe el vector b                
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(["\nVector b"])
        csv_writer.writerow([str(valor) for valor in b])

        csv_writer.writerow([])  
        

    print("Resultados guardados en 'resultados_5.csv'.")
else:
    print("No se pudo encontrar una solución válida.")
