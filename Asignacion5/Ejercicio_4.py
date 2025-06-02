'''
n. 04) Desarrolle, depure y pruebe un programa amigable para el usuario en cualquier lenguaje de
alto nivel o de macros de su predilección, para implementar el método de trazadores cúbicos para
interpolar los siguientes datos:

𝑥       0.0     0.6     1.5     1.7     1.9     2.1     2.3     2.6     2.8     3.0     3.6
𝑓(𝑥)    -0.80  -0.34    0.59    0.59    0.23    0.1     0.28    1.03    1.50    1.44    0.74

Muestre la gráfica que ajusta los datos y los polinomios de cada intervalo.

'''

import numpy as np
import matplotlib.pyplot as plt

# Función para calcular coeficientes de trazadores cúbicos
def tridiag(x, y):
    # Obtengo la cantidad de puntos
    n = len(x)
    
    # Calculo las diferencias entre puntos adyacentes
    h = np.diff(x)
    
    # Calculo los coeficientes alpha para el sistema tridiagonal
    alpha = [0] + [3/h[i] * (y[i+1] - y[i]) - 3/h[i-1] * (y[i] - y[i-1]) for i in range(1, n-1)]
    
    # Inicializo las matrices tridiagonales
    l, u, z = [0]*n, [0]*n, [0]*n
    
    # Primeros valores de las matrices
    l[0] = 1
    u[0] = 0
    z[0] = 0
    
    # Lleno las matrices tridiagonales
    for i in range(1, n-1):
        l[i] = 2 * (x[i+1] - x[i-1]) - h[i-1] * u[i-1]
        u[i] = h[i] / l[i]
        z[i] = (alpha[i] - h[i-1] * z[i-1]) / l[i]
    
    # Últimos valores de las matrices
    l[n-1] = 1
    z[n-1] = 0
    
    # Inicializo los vectores c, b, y d
    c, b, d = [0]*n, [0]*n, [0]*n
    
    # Calculo los coeficientes c, b, y d mediante sustitución hacia atrás
    for j in range(n-2, -1, -1):
        c[j] = z[j] - u[j] * c[j+1]
        b[j] = (y[j+1] - y[j]) / h[j] - h[j] * (c[j+1] + 2*c[j]) / 3
        d[j] = (c[j+1] - c[j]) / (3 * h[j])
    
    # Devuelvo los resultados
    return y, b, c, d


# Defino la función de interpolación cúbica
def spline_cubico(x, y, xu):
    # Obtengo los coeficientes de los trazadores cúbicos
    y, b, c, d = tridiag(x, y)
    n = len(x)
    
    # Itero sobre los segmentos para encontrar el resultado de la interpolación
    for i in range(n-1):
        if x[i] <= xu <= x[i+1]:
            dx = xu - x[i]
            result = y[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3
            return result
    return None

# Datos de entrada
x_valor = np.array([0.0, 0.6, 1.5, 1.7, 1.9, 2.1, 2.3, 2.6, 2.8, 3.0, 3.6])
y_valor = np.array([-0.80, -0.34, 0.59, 0.59, 0.23, 0.1, 0.28, 1.03, 1.50, 1.44, 0.74])

# Puntos para graficar la interpolación
curva_de_interpolacion_x = np.linspace(min(x_valor), max(x_valor), 1000)
curva_de_interpolacion_y = [spline_cubico(x_valor, y_valor, xi) for xi in curva_de_interpolacion_x]

# Graficar los puntos dados y la interpolación
plt.scatter(x_valor, y_valor, color='red', label='Datos')

# Etiquetar cada punto con su valor de f(x)
for i, (x, y) in enumerate(zip(x_valor, y_valor)):
    plt.text(x, y, f'{y:.2f}', fontsize=8, ha='right', va='bottom')

plt.plot(curva_de_interpolacion_x, curva_de_interpolacion_y, label='Interpolación cúbica')
plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación mediante trazadores cúbicos')
plt.savefig(f'Ejercicio_4_Resultados.png')
plt.legend()
plt.grid(True)
plt.show()
