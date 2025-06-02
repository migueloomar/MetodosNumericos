'''
N.- 01) Determine las raíces reales de 
f(x) = -25 + 82x - 90x^2 + 44x^3 - 8x^4 + 0.7x^5
Usando un método gráfico y desarrollando un programa amigable para el usuario para el
método de bisección y úselo para localizar la raíz más grande con 𝜀_𝑠 = 0.0001%. Utilice como
valores iniciales x_l = 0.5 y x_u = 1.0.

'''

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image 
import os
import sympy as sp

# Solicita al usuario la función f(x) en notación de Python
obtener_funcion = input("Ingrese la función en términos de 'x' (ejemplo: -25 + 82*x - 90*x**2 + 44*x**3 - 8*x**4 + 0.7*x**5 ): ")
x = sp.symbols('x')                                     # Define la variable simbólica
funcion = sp.lambdify(x, obtener_funcion, 'numpy')      # Convierte la cadena de texto a una función evaluable numéricamente con numpy


# Método de Bisección

def biseccion():

    # Solicita los extremos del intervalo [xl, xu] y la tolerancia
    xl = float(input("Ingrese el valor inicial (xl = 0.5): "))
    xu = float(input("Ingrese el valor final (xu = 1): "))
    tol = float(input("Ingrese la tolerancia (0.0001): "))

    # Variables auxiliares para comparar convergencia
    m1 = xl
    m = xu
    k = 0   # Contador de iteraciones

    # Listas para guardar raíces y fotogramas
    raices = []
    frames = []

    # Prepara los datos para graficar la función
    x_vals = np.linspace(xl, xu, 100)
    y_vals = funcion(x_vals)

    # Verifica la condición de cambio de signo (f(xl) * f(xu) < 0)
    if funcion(xl) * funcion(xu) > 0:
        print('La función no cambia de signo en el intervalo dado.')
        return
    
    # Bucle de iteración del método de bisección
    while abs(m1 - m) > tol:
        m1 = m
        m = (xl + xu) / 2       # punto medio

        # Gráfico de la iteración actual
        plt.plot(x_vals, y_vals, label='Función')
        plt.axvline(x=xl, color='r', linestyle='--', label='Intervalo [xl, m]')
        plt.axvline(x=xu, color='g', linestyle='--', label='Intervalo [m, xu]')
        plt.title(f'Bisección - Iteración {k + 1}')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.legend()

        # Guarda el gráfico actual como imagen PNG
        img_filename = f'Iteracion_{k}.png'
        plt.savefig(img_filename)
        frames.append(Image.open(img_filename))
        plt.close()

        k += 1              # Aumenta el contador de iteraciones

        # Determina en qué subintervalo continuar (cambio de signo)
        if funcion(xl) * funcion(m) < 0:
            xu = m
        if funcion(m) * funcion(xu) < 0:
            xl = m

        raices.append(m)    # Almacena el valor de la raíz aproximada


    # Generación del GIF con todas las iteraciones
    frames[0].save('Eje_1.gif', save_all=True, append_images=frames[1:], duration=500, loop=0)

    # Guardado de iteraciones en archivo de texto
    with open('Eje_1.txt', 'w') as file:
        for i, raiz in enumerate(raices):
            file.write(f"Iteración {i + 1}: {raiz:.6f}\n")

    # Limpieza: elimina imágenes PNG generadas
    for img_filename in os.listdir():
        if img_filename.startswith('Iteracion_'):
            os.remove(img_filename)

# Ejecución del método
biseccion()
