'''
N.- 02) Localice la primera raíz no trivial de sen 𝑥 = 𝑥^2, donde 𝑥 está en radianes. 
Usando unmétodo gráfico y el método de bisección con un intervalo inicial de 0.5 a 1. 
Haga el cálculo hasta que 𝜀𝑎 sea menor que 𝜀𝑠 = 0.0001%.

'''

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os
import sympy as sp

#  Función a realizar
obtener_funcion = input("Ingrese la función en términos de 'x' (Ejemplo: sin(x) - x**2): ")
x = sp.symbols('x')
funcion = sp.lambdify(x, obtener_funcion, 'numpy')

# Método de bisección
def biseccion():
    # Solicito al usuario los valores iniciales y la tolerancia
    xl = float(input("Ingrese el valor inicial (xl = 0.5): "))
    xu = float(input("Ingrese el valor final (xu = 1): "))
    tol = float(input("Ingrese la tolerancia (0.0001): "))

    # Guardo los valores iniciales
    m1 = xl
    m = xu
    k = 0
    # Lista para almacenar los valores de la raíz en cada iteración
    raices = []
    # Lista para almacenar las imágenes de las iteraciones
    frames = []

    x_vals = np.linspace(xl, xu, 100)
    y_vals = funcion(x_vals)
    # Verifico que haya un cambio de signo para que pueda encontrarse una raíz en ese intervalo
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
        img_filename = f'iteracion_{k}.png'
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
    frames[0].save('Eje_2.gif', save_all=True, append_images=frames[1:], duration=500, loop=0)

    # Cada iteración se guarda en 'Ejercicio_2.txt'
    with open('Eje_2.txt', 'w') as file:
        for i, raiz in enumerate(raices):
            file.write(f"Iteración {i + 1}: {raiz:.6f}\n")

    # Se elimina cada imagen para dejar solo el GIF
    for img_filename in os.listdir():
        if img_filename.startswith('iteracion_'):
            os.remove(img_filename)

# Llamada a la función sin argumentos
biseccion()
