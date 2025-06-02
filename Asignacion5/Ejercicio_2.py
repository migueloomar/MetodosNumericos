'''
n. 02) Desarrolle, depure y pruebe un programa amigable para el usuario en cualquier lenguaje de
alto nivel o de macros de su predilección, para implementar el método de la interpolación de
Lagrange para interpolar los siguientes datos:

x       f(x)
1.6     2.0
2.0     8.0
2.5     14.0
3.2     15.0
4.0     8.0

Muestre la gráfica que ajusta los datos.

'''

import numpy as np
import sympy
import matplotlib.pyplot as plt
from PIL import Image
import os

# Datos de entrada
dato_x = np.array([1.6, 2.0, 2.5, 3.2, 4.0])
funcion_de_x = np.array([2.0, 8.0, 14.0, 15.0, 8.0])

# Símbolo simbólico x
x = sympy.symbols('x')

# Número de puntos
n = len(dato_x)

# Inicializar polinomio
polinomio = 0

# Calcular polinomio de Lagrange
for i in range(n):
    numerador = 1
    denominador = 1

    for j in range(n):
        if j != i:
            numerador *= (x - dato_x[j])
            denominador *= (dato_x[i] - dato_x[j])

    Li = numerador / denominador
    polinomio += Li * funcion_de_x[i]

# Convertir el polinomio a una función que pueda evaluarse numéricamente
polinomio_func = sympy.lambdify(x, polinomio, 'numpy')

# Crear un archivo de texto para guardar los resultados
with open('Ejercicio_2_Resultados.txt', 'w') as file:
    file.write("x  f(x)\n")

    # Imprimir y escribir en el archivo para cada valor de x
    for x_val in dato_x:
        y_val = polinomio_func(x_val)
        file.write(f"{x_val}  {y_val}\n")
        print(f"x: {x_val}, f(x): {y_val}")

# Crear un directorio para guardar las imágenes temporales
if not os.path.exists('Ejercicio2_pngtemporales'):
    os.makedirs('Ejercicio2_pngtemporales')

# Guardar la gráfica en formato PNG para cada valor de x
for x_val in dato_x:
    plt.scatter(dato_x, funcion_de_x, color='red', label='Puntos dados')
    plt.plot(dato_x, funcion_de_x, linestyle='--', color='gray', label='Línea original')
    plt.scatter(x_val, polinomio_func(x_val), color='blue', label='Punto interpolado')

    # Generar puntos para la gráfica
    x_vals = np.linspace(min(dato_x), max(dato_x), 1000)
    y_vals = polinomio_func(x_vals)

    plt.plot(x_vals, y_vals, label='Interpolación de Lagrange')

    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title(f'Interpolación de Lagrange para x = {x_val}')
    plt.legend()
    plt.savefig(f'Ejercicio2_pngtemporales/Iteracion_{x_val}.png')
    plt.close()

# Combinar las imágenes en un archivo GIF
frames = [Image.open(f'Ejercicio2_pngtemporales/Iteracion_{x_val}.png') for x_val in dato_x]
frames[0].save('Ejercicio_2_Resultados.gif', save_all=True, append_images=frames[1:], duration=1500, loop=0)

# Limpiar archivos temporales (imágenes PNG)
for img_filename in os.listdir('Ejercicio2_pngtemporales'):
    img_path = os.path.join('Ejercicio2_pngtemporales', img_filename)
    os.remove(img_path)

# Eliminar el directorio temporal
os.rmdir('Ejercicio2_pngtemporales')
