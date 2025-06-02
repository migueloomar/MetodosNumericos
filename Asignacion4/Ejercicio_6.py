'''
N.- 06) Determine la menor raíz positiva de 𝑓(𝑥) = 8 sin(𝑥) 𝑒^{−𝑥} − 1. Usando un método
gráfico y empleando el método de Newton-Raphson. Haga el cálculo hasta que 𝜀𝑎 sea menor
que 𝜀𝑠 = 0.0001%.
'''


import sympy as sp
import matplotlib.pyplot as plt
from PIL import Image
import os
import numpy as np

# Definir la variable simbólica
x = sp.symbols('x')

# f(x)
obtener_funcion = input("Ingrese la función en términos de 'x' para f(x) (Ejemplo: 8*sin(x)*exp(-x) - 1 ): ")
expresion_funcion = sp.sympify(obtener_funcion)
f = sp.lambdify(x, expresion_funcion, 'numpy')

# Derivada de f(x)
obtener_derivada = input("Ingrese la derivada de la función en términos de 'x' para f'(x) (Ejemplo: 8*cos(x)*exp(-x) - 8*sin(x)*exp(-x) ): ")
expresion_derivada = sp.sympify(obtener_derivada)
f_prima = sp.lambdify(x, expresion_derivada, 'numpy')

# Método de Newton-Raphson
def NewtonRaphson():
    # Solicitar al usuario el punto inicial y la tolerancia
    x0 = float(input("Ingrese el punto inicial (x0 = 0.5): "))
    tol = float(input("Ingrese la tolerancia (tol = 0.0001): "))

    x_vals = []

    for k in range(100):
        x_anterior = x0
        x0 = x0 - f(x0) / f_prima(x0)
        e = abs((x0 - x_anterior) / x0)

        x_vals.append(x0)

        # Crear una gráfica para cada iteración
        x_range = np.linspace(min(x_vals) - 1, max(x_vals) + 1, 1000)
        plt.plot(x_range, f(x_range), label='f(x)', linewidth=2)
        plt.plot(x_range, f_prima(x_range), label="f'(x)", linestyle='dashed', linewidth=2)
        plt.scatter(x_vals, [f(val) for val in x_vals], color='red', marker='o', label='Puntos de Newton-Raphson', zorder=5)
        plt.axhline(y=0, color='black', linewidth=0.5, linestyle='--', label='y=0')
        plt.xlabel('x')
        plt.ylabel('y')
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

    # Resto del código de guardado y limpieza
    frames = [Image.open(f'Iteracion_{i + 1}.png') for i in range(len(x_vals))]
    frames[0].save('Eje_6.gif', save_all=True, append_images=frames[1:], duration=500, loop=0)

    # Limpiar archivos temporales (imágenes PNG)
    for img_filename in os.listdir():
        if img_filename.startswith('Iteracion_'):
            os.remove(img_filename)

    # Guardar los resultados en un archivo de texto
    with open('Eje_6.txt', 'w') as file:
        for i, val in enumerate(x_vals):
            file.write(f"Iteración {i + 1}: {val:.6f}\n")

# Llamada a la función NewtonRaphson
NewtonRaphson()
