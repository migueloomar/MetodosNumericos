'''
n. 03) Desarrolle, depure y pruebe un programa amigable para el usuario en cualquier lenguaje de
alto nivel o de macros de su predilección, para implementar el método de trazadores cúbicos para
interpolar los siguientes datos:

𝑥    3.0    4.5    7.0    9.0
𝑓(𝑥) 2.5    1.0    2.5    0.5

Utilizando este programa calcule el resultado para 𝑓(5.2).


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
            respuesta = y[i] + b[i]*dx + c[i]*dx**2 + d[i]*dx**3
            return respuesta
    return None

# Datos de entrada
x_valor = np.array([3.0, 4.5, 7.0, 9.0])
y_valor = np.array([2.5, 1.0, 2.5, 0.5])

# Punto a interpolar
interpolacion_x = 5.2

# Calculo resultado para f(5.2)
respuesta = spline_cubico(x_valor, y_valor, interpolacion_x)

# Imprimo el resultado de la interpolación si está dentro del rango
if respuesta is not None:
    print(f"El resultado de la interpolación para f(5.2) es: {respuesta}")
else:
    print("El valor de interpolacion_x está fuera del rango de interpolación.")

# Puntos para graficar la interpolación
curva_de_interpolacion_x = np.linspace(min(x_valor), max(x_valor), 1000)
curva_de_interpolacion_y = [spline_cubico(x_valor, y_valor, xi) for xi in curva_de_interpolacion_x]

# Graficar los puntos dados y la interpolación
plt.scatter(x_valor, y_valor, color='red', label='Datos')

# Etiquetar cada punto con su valor f(x)
for i, txt in enumerate(y_valor):
    plt.annotate(f'{txt:.2f}', (x_valor[i], y_valor[i]), textcoords="offset points", xytext=(0,10), ha='center')

plt.plot(curva_de_interpolacion_x, curva_de_interpolacion_y, label='Interpolación cúbica')
plt.scatter(interpolacion_x, respuesta, color='orange', label=f'Interpolación en f({interpolacion_x}) = {respuesta}')

# Etiquetar el punto interpolado con su valor f(x)
plt.annotate(f'{respuesta:.2f}', (interpolacion_x, respuesta), textcoords="offset points", xytext=(0,10), ha='center', color='orange')

plt.xlabel('x')
plt.ylabel('f(x)')
plt.title('Interpolación mediante trazadores cúbicos')
plt.savefig(f'Ejercicio_3_Resultados.png')
plt.legend()
plt.grid(True)
plt.show()
