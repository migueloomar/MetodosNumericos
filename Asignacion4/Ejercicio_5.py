'''
N.- 05) Desarrolle un programa amigable para el usuario para el método de Newton-Raphson,
para determinar una raíz de 𝑓(𝑥) = −𝑥^2 + 1.8𝑥 + 2.5 con el uso de 𝑥_0 = 5. Haga el cálculo
hasta que 𝜀𝑎 sea menor que 𝜀𝑠 = 0.0001%

'''

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

# Función f(x) para el método de Newton-Raphson
obtener_funcion = input("Ingrese la función en términos de 'x' para f(x) (Ejemplo: -x**2 + 1.8*x + 2.5  ): ")
guarda_obtener_funcion = sp.sympify(obtener_funcion)
f = sp.lambdify(x, guarda_obtener_funcion, 'numpy')

# Derivada de f(x)
obtener_funcion_prima = input("Ingrese la derivada de la función en términos de 'x' para f'(x) (Ejemplo: -2*x + 1.8): ")
guarda_obtener_funcion_prima = sp.sympify(obtener_funcion_prima)
f_prima = sp.lambdify(x, guarda_obtener_funcion_prima, 'numpy')

# Método de Newton-Raphson
def NewtonRaphson():
    # Solicitar al usuario el punto inicial y la tolerancia
    x0 = float(input("Ingrese el punto inicial (x0 = 5): "))
    tol = float(input("Ingrese la tolerancia (tol = 0.0001): "))

    x_vals = []

    for k in range(100):
        x_anterior = x0
        x0 = x0 - f(x0) / f_prima(x0)
        e = abs((x0 - x_anterior) / x0)

        x_vals.append(x0)

        # Crear una gráfica para cada iteración
        x_range = np.linspace(min(x_vals) - 1, max(x_vals) + 1, 100)
        plt.plot(x_range, f(x_range), label='f(x)')
        plt.plot(x_range, f_prima(x_range), label="f'(x)", linestyle='dashed', linewidth=2)
        plt.scatter(x_vals, [f(val) for val in x_vals], color='red', label='Puntos de Newton-Raphson')
        plt.xlabel('x')
        plt.ylabel('f(x)')
        plt.title(f'Iteración {k + 1}')
        plt.legend()
        plt.grid(True)
        
        # Guardar la gráfica como una imagen PNG
        img_filename = f'Iteracion_{k + 1}.png'
        plt.savefig(img_filename)
        plt.close()

        # Si el error es menor a la tolerancia, se detiene
        if e < tol:
            break

    # Guardar los resultados en un archivo de texto
    with open('Eje_5.txt', 'w') as file:
        for i, val in enumerate(x_vals):
            file.write(f"Iteración {i + 1}: {val:.6f}\n")

    # Crear un GIF a partir de las imágenes generadas
    frames = []
    for i in range(len(x_vals)):
        img_filename = f'Iteracion_{i + 1}.png'
        frames.append(Image.open(img_filename))

    frames[0].save('Eje_5.gif', save_all=True, append_images=frames[1:], duration=500, loop=0)

    # Limpia archivos temporales (imágenes PNG)
    for img_filename in os.listdir():
        if img_filename.startswith('Iteracion_'):
            os.remove(img_filename)

# Llamada a la función NewtonRaphson
NewtonRaphson()
