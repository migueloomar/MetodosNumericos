'''
N.- 04) Utilice la iteración simple de punto fijo para localizar la raíz de 
𝑓(𝑥) = 2 sin(√𝑥) − 𝑥.
Haga una elección inicial de 𝑥0 = 0.5 e itere hasta que 𝜀𝑎 ≤ 0.0001%.
'''

import numpy as np
import matplotlib.pyplot as plt
from PIL import Image
import os
import sympy as sp

# Definir la variable simbólica
x = sp.symbols('x')

#  función f(x)
obtener_funcion = input("Ingrese la función en términos de 'x' para f(x) (ejemplo: 2*sin(sqrt(x)) - x ): ")
guarda_obtener_funcion = sp.sympify(obtener_funcion)
f = sp.lambdify(x, guarda_obtener_funcion, 'numpy')

# como el ejercicio nos brinda f(x) necesitamos pasar la funcion a g(x), devolviendo una nueva funcion
def generar_g(f):
    def g(x):
        return f(x) + x
    return g

# Función de punto fijo
def punto_fijo():
    # solicito los datos necesarios como valor inicial, num de iteraciones y la tolerancia
    x0 = float(input("Ingrese el valor inicial (x0 = 0.5): "))
    n = int(input("Ingrese el número máximo de iteraciones (100): "))
    tol = float(input("Ingrese la tolerancia (0.0001): "))

    # g llama a generar_g(x)
    g = generar_g(f)

    resultados = [x0]
    # Lista para almacenar las imágenes de las iteraciones
    frames = []

    x_vals = np.linspace(0, 2, 1000)
    y_f = f(x_vals)
    y_g = g(x_vals)

    for k in range(n):
        x1 = g(x0)
        resultados.append(x1)

        plt.plot(x_vals, y_f, label='f(x)')
        plt.plot(x_vals, y_g, label='g(x)')
        plt.axhline(y=0, color='black', linewidth=0.5, linestyle='--', label='y=0')
        plt.scatter(x1, 0, color='r', marker='o', label='Punto fijo')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Gráficas de f(x) y g(x)')
        plt.legend()

        # Guardar el gráfico actual como una imagen
        img_filename = f'Iteracion_{k}.png'
        plt.savefig(img_filename)
        frames.append(Image.open(img_filename))
        plt.close()

        # Obtener el punto fijo
        if abs(x1 - x0) <= tol:
            print(f'x{k+1} = {x1} es el punto fijo')
            break
        x0 = x1

    # Todas las imágenes se convierten en un GIF
    frames[0].save('Eje_4.gif', save_all=True, append_images=frames[1:], duration=500, loop=0)

    # Cada iteración se guarda en 'Ejercicio_4.txt'
    with open('Eje_4.txt', 'w') as file:
        for i, resultado in enumerate(resultados):
            file.write(f"Iteración {i + 1}: {resultado:.6f}\n")

    # Eliminar cada imagen para dejar solo el GIF
    for img_filename in os.listdir():
        if img_filename.startswith('Iteracion_'):
            os.remove(img_filename)

# Llamada a la función sin argumentos
punto_fijo()
