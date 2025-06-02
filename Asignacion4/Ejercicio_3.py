'''
N.- 03) Determine la raíz real de ln 𝑥^2 = 0.7. Usando un método gráfico y empleando el
método de bisección con los valores iniciales 𝑥𝑙 = 0.5 y 𝑥𝑢 = 2. Haga el cálculo hasta que 𝜀𝑎
sea menor que 𝜀𝑠 = 0.0001%
'''

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image 
import os
import sympy as sp

# Solicitar al usuario la función
obtener_funcion = input("Ingrese la función en términos de 'x' (ejemplo: log(x**2) - 0.7 ): ")
x = sp.symbols('x')
funcion = sp.lambdify(x, obtener_funcion, 'numpy')

# método de bisección
def biseccion():
    # Solicitar al usuario los valores iniciales y la tolerancia
    xl = float(input("Ingrese el valor inicial (xl = 0.5): "))
    xu = float(input("Ingrese el valor final (xu = 2): "))
    tol = float(input("Ingrese la tolerancia (0.0001): "))

    # Se almacenan los valores iniciales
    m1 = xl
    m = xu
    k = 0
    # Lista para almacenar los valores de la raíz en cada iteración
    raices = []
    # Lista para almacenar las imágenes de las iteraciones
    frames = []

    x_vals = np.linspace(xl, xu, 100)
    y_vals = funcion(x_vals)
    # Verifica que se tenga el mismo signo para que pueda encontrar una raíz en ese intervalo
    if funcion(xl) * funcion(xu) > 0:
        print('La función no cambia de signo en el intervalo dado.')
        return
    # Se ejecuta mientras los extremos absolutos del intervalo sean mayores que la tolerancia
    while abs(m1 - m) > tol:
        m1 = m
        # Se calcula el punto medio
        m = (xl + xu) / 2

        plt.plot(x_vals, y_vals, label='Función')
        plt.axvline(x=xl, color='r', linestyle='--', label='Intervalo [xl, m]')
        plt.axvline(x=xu, color='g', linestyle='--', label='Intervalo [m, xu]')
        plt.title(f'Bisección - Iteración {k + 1}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()

        # Guarda el gráfico actual como una imagen
        img_filename = f'Iteracion_{k}.png'
        plt.savefig(img_filename)
        frames.append(Image.open(img_filename))
        plt.close()

        k += 1
        # Comprueba los cambios de signos
        if funcion(xl) * funcion(m) < 0:
            xu = m
        if funcion(m) * funcion(xu) < 0:
            xl = m

        raices.append(m)

    # Todas las imágenes se convierten en un GIF
    frames[0].save('Eje_3.gif', save_all=True, append_images=frames[1:], duration=500, loop=0)

    # Cada iteración se guarda en 'ejercicio_1.txt'
    with open('Eje_3.txt', 'w') as file:
        for i, raiz in enumerate(raices):
            file.write(f"Iteración {i + 1}: {raiz:.6f}\n")

    # Se elimina cada imagen para dejar solo el GIF
    for img_filename in os.listdir():
        if img_filename.startswith('Iteracion_'):
            os.remove(img_filename)

# Llamada a la función sin argumentos
biseccion()
