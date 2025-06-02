'''
n. 01) Desarrolle, depure y pruebe un programa amigable para el usuario en cualquier lenguaje de
alto nivel o de macros de su predilección, para implementar el método de la interpolación de
Lagrange. Pruébelo en el siguiente problema. Suponga que se tiene un instrumento para medir la
velocidad de un paracaidista. Los datos obtenidos en una prueba particular son

Tiempo   Velocidad media
1           800
3           2310
5           3090
7           3940
13          4755

Estime la velocidad del paracaidista en t = 10 s.

'''

import numpy as np
import sympy
import matplotlib.pyplot as plt
from PIL import Image
import os

# Datos de entrada
tiempo = np.array([1, 3, 5, 7, 13])
velocidad = np.array([800, 2310, 3090, 3940, 4755])

# Símbolo simbólico x
x = sympy.symbols('x')

# Número de puntos
n = len(tiempo)

# Inicializar polinomio
polinomio = 0

# Calcular polinomio de Lagrange
for i in range(n):
    numerador = 1
    denominador = 1

    for j in range(n):
        if j != i:
            numerador *= (x - tiempo[j])
            denominador *= (tiempo[i] - tiempo[j])

    Li = numerador / denominador
    polinomio += Li * velocidad[i]

# Convertir el polinomio a una función que pueda evaluarse numéricamente
polinomio_func = sympy.lambdify(x, polinomio, 'numpy')

# Crear un archivo de texto para guardar los resultados
with open('Ejercicio_1_paracaidista.txt', 'w') as file:
    file.write("Tiempo (s)  Velocidad (m/s)\n")

    # Imprimir y escribir en el archivo para cada segundo
    for t in range(1, 5):
        v = polinomio_func(t)
        file.write(f"{t}           {v}\n")
        print(f"Tiempo: {t} s, Velocidad: {v} m/s")

# Crear un directorio para guardar las imágenes temporales
if not os.path.exists('Ejercicio1_pngtemporales'):
    os.makedirs('Ejercicio1_pngtemporales')

# Guardar la gráfica en formato PNG para cada segundo
for t in range(1, 14):
    plt.scatter(tiempo, velocidad, color='red', label='Puntos dados')
    # plt.plot(tiempo, velocidad, linestyle='--', color='gray', label='Línea original')
    plt.scatter(t, polinomio_func(t), color='blue', label='Punto interpolado')
    
    # Genera puntos para la gráfica 
    x_vals = np.linspace(min(tiempo), max(tiempo), 1000) 
    y_vals = polinomio_func(x_vals)
    
    plt.plot(x_vals, y_vals, label='Interpolación de Lagrange ')

    plt.xlabel('Tiempo (s)')
    plt.ylabel('Velocidad (m/s)')
    plt.title(f'Interpolación de Lagrange para t = {t} s')
    plt.legend()
    plt.savefig(f'Ejercicio1_pngtemporales/Iteracion_{t}.png')
    plt.close()

# Combinar las imágenes en un archivo GIF
# Muestra todos los frames de 1 al 13
frames = [Image.open(f'Ejercicio1_pngtemporales/Iteracion_{i}.png') for i in range(1, 5)]
frames[0].save('Ejercicio_1_Paracaidista.gif', save_all=True, append_images=frames[1:], duration=1500, loop=0)

# Limpiar archivos temporales (imágenes PNG)
for img_filename in os.listdir('Ejercicio1_pngtemporales'):
    img_path = os.path.join('Ejercicio1_pngtemporales', img_filename)
    os.remove(img_path)

# Eliminar el directorio temporal
os.rmdir('Ejercicio1_pngtemporales')

# Estimar la velocidad en t = 10 s
t_estimado = 4
velocidad_estimada = polinomio_func(t_estimado)
print(f"Estimación de la velocidad en t = {t_estimado} s: {velocidad_estimada} m/s")
