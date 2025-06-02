"""
N.-02) En clases se encontró que, cuando la fuerza de resistencia del viento es 
directamente proporcional al cuadrado de la velocidad (Fd = c * v^2), 
las ecuaciones para calcular la velocidad en función del tiempo, tanto 
analítica como de forma aproximada, son:

    Solución analítica:
    v(t) = sqrt((g * m) / c) * tanh(sqrt((g * c) / m) * t

    Aproximación numérica:
    v(t_{i+1}) = v(t_i) + [g - (c / m) * v(t_i)^2] * (t_{i+1} - t_i)

Escriba un programa para obtener las velocidades en un rango de tiempo 
de 0 a 49 segundos, utilizando tanto la solución analítica como la aproximación. 
Utilice un valor de gravedad g = 9.8 m/s² y un coeficiente de resistencia 
c = 0.2 kg/s. Emplee un tamaño de paso (diferencia de tiempo) de dos segundos.

Haga una gráfica de velocidad contra tiempo y compare entre la solución 
analítica y la aproximación.
"""

import numpy as np
import matplotlib.pyplot as plt

# Esta función solicita un valor numérico al usuario, 
# valida que cumpla con una condición dada, y 
# maneja errores de tipo si el dato ingresado no es un número.

def solicitar_valor(mensaje, condicion):
    while True:
        valor_str = input(mensaje)
        try:
            valor = float(valor_str)
            if condicion(valor):
                return valor
            else:
                print("El valor no cumple con la condición requerida.")
        except ValueError:
            print("El valor ingresado no es un número válido.")

# Se solicitan al usuario los valores de masa (m), gravedad (g)
# y coeficiente de resistencia (c), asegurando que sean positivos.

m = solicitar_valor("Ingrese el valor de la masa (debe ser positiva, ejemplo: 68.1): ", lambda valor: valor > 0)
g = solicitar_valor("Ingrese el valor de la gravedad (debe ser positiva, ejemplo: 9.8): ", lambda valor: valor > 0)
c = solicitar_valor("Ingrese el valor de la constante (debe ser positiva, ejemplo: 0.2): ", lambda valor: valor > 0)

# Se define el tamaño del paso (2 segundos) y 
# se genera un arreglo de tiempos desde 0 hasta 49 segundos.
dt = 2
valores_t = np.arange(0, 50, dt)

# Se inicializa la velocidad para la fórmula numérica y 
# se crean listas para almacenar los resultados de ambas fórmulas.

valor_actual_formula4 = 0
resultado_formula3 = []
resultado_formula4 = []

# Se calcula la velocidad en cada instante de tiempo utilizando:
# - solución analítica con resistencia cuadrática
# - aproximación numérica por pasos
# Los resultados se guardan en un archivo de texto.

with open('resultados_de_cv^2.txt', 'w') as file:
    file.write(f"Valores constantes:\n")
    file.write(f"m = {m} kg\n")
    file.write(f"g = {g} m/s^2\n")
    file.write(f"c = {c} kg/s\n")
    file.write("\nTiempo (t)   Velocidad Formula 3   Velocidad Formula 4\n")

    for t in valores_t:
        # Solución analítica con tanh
        velocidad_3 = np.sqrt((m * g) / c) * np.tanh(np.sqrt((g * c / m) * t))
        resultado_formula3.append((t, velocidad_3))

        # Aproximación numérica basada en diferencias finitas
        velocidad_4 = valor_actual_formula4 + (g - (c / m) * (valor_actual_formula4) ** 2) * (t - (t - dt))
        resultado_formula4.append((t, velocidad_4))

        file.write(f"{t:.2f}          {velocidad_3:.4f}               {velocidad_4:.4f}\n")
        valor_actual_formula4 = velocidad_4

print("Resultados guardados en 'resultados_de_cv^2.txt'")

# Se extraen los valores de tiempo y velocidad desde las listas 
# para graficar los resultados.

valores_t = [result[0] for result in resultado_formula3]
velocidad_formula3 = [result[1] for result in resultado_formula3]
velocidad_formula4 = [result[1] for result in resultado_formula4]

# Se grafican los resultados de ambas fórmulas, se añaden etiquetas, 
# título, leyenda y cuadrícula. Luego, se guarda la gráfica como imagen PNG 
# y se muestra en pantalla.

plt.plot(valores_t, velocidad_formula3, label='Metodo matemático')
plt.plot(valores_t, velocidad_formula4, label='Aproximación')
plt.xlabel('Tiempo (t)')
plt.ylabel('Velocidad (v)')
plt.title('Gráfica cv^2')
plt.legend()
plt.grid(True)
plt.savefig('grafica_cv^2.png')
print("Gráfica guardada como 'grafica_cv^2.png'")
plt.show()
