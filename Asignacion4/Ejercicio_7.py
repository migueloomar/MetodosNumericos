'''
N 07) Desarrolle un programa amigable para el usuario para el método de la secante, para
determinar la raíz de 𝑓(𝑥) = 𝑒^{−𝑥} − 𝑥. 
Comience con los valores iniciales 𝑥_{−1} = 0 y 𝑥_0 = 1.0.
Haga el cálculo hasta que 𝜀𝑎 sea menor que 𝜀𝑠 = 0.0001%. 

'''

import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
import os

# El usuario ingresa la función que va a usar
def ObtenerFuncion():
    instruccion = input("Ingresa la función f(x). (Ejemplo:  exp(-x) - x ) : ")
    return lambda x: eval(instruccion.replace('exp', 'np.exp'))

funcion = ObtenerFuncion()

# Puntos iniciales ingresados por el usuario
xn_anterior = float(input("Ingresa el valor inicial (x_-1 = 0): "))
xn = float(input("Ingresa el valor inicial (x_0 = 1): "))

tol = float(input("Ingresa la tolerancia (tol = 0.0001): "))
itermax = int(input("Ingresa el número máximo de iteraciones (itermax = 100): "))

x_values = [xn_anterior, xn]
y_values = [funcion(xn_anterior), funcion(xn)]

x = np.linspace(min(xn_anterior, xn) - 1, max(xn_anterior, xn) + 1, 400)  # Valores de x para graficar la función
y = funcion(x)  # Valores de f(x) correspondientes

# Lista para almacenar los valores de la raíz en cada iteración
raices = []

# Lista para almacenar los cuadros de las iteraciones
frames = []

iter = 0

while iter < itermax:
    x_raiz = xn - ((xn - xn_anterior) / (funcion(xn) - funcion(xn_anterior))) * funcion(xn)
    x_values.append(x_raiz)
    y_values.append(funcion(x_raiz))

    # Almacenar la raíz en la lista
    raices.append(x_raiz)

    # Crear la gráfica sin el cambio de color
    plt.plot(x_values, y_values, marker='o', linestyle='-', label='Aproximación de la raíz')
    plt.plot(x, y, label='f(x)')
    plt.title("Aproximación de la raíz por el método de la secante (Iteración {})".format(iter + 1))
    plt.xlabel("x")
    plt.ylabel("f(x)")
    plt.grid(True)
    plt.legend()

    # Agrega el valor de x_raiz a la imagen
    #plt.text(0.5, 0.9, f'x_raiz = {x_raiz:.6f}', transform=plt.gca().transAxes, fontsize=10, color='blue')

    # Guarda la gráfica como una imagen
    img_filename = "iteracion_{}.png".format(iter)
    plt.savefig(img_filename)
    frames.append(Image.open(img_filename))

    # Limpia la gráfica actual
    plt.clf()

    # Calcula el error relativo porcentual aproximado (epsilon_a)
    if iter > 0:
        epsilon_a = abs((x_raiz - xn) / x_raiz) * 100
        if epsilon_a < tol:
            break

    xn_anterior = xn
    xn = x_raiz
    iter += 1

print("Resultado:", x_raiz)

# Todas las imagenes se convierten en un GIF
frames[0].save('Eje_7.gif', save_all=True, append_images=frames[1:], duration=500, loop=0)

# Cada iteracion se guarda en 'ejercicio_7.txt'
with open('Eje_7.txt', 'w') as file:
    for i, raiz in enumerate(raices):
        file.write(f"Iteracion {i + 1}: {raiz:.6f}\n")

# Se elimina cada imagen para dejar solo el GIF
for img_filename in os.listdir():
    if img_filename.startswith('iteracion_'):
        os.remove(img_filename)
