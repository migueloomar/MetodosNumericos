"""
N.-01) En clases encontramos que, para un paracaidista con una masa de m = 68.1 kg 
que salta de un globo aerostático fijo y con un coeficiente de resistencia 
igual a c = 12.5 kg/s, la ecuación que relaciona la velocidad con el tiempo, 
encontrada de forma analítica, es:

    v(t) = (gm/c) * (1 - e^(-(c/m)t))

y la forma aproximada para encontrar la velocidad en función del tiempo es:

    v(t_{i+1}) = v(t_i) + [g - (c/m)v(t_i)] * (t_{i+1} - t_i)

Escriba un programa para obtener las velocidades en un rango de tiempo 
de 0 a 49 segundos, tanto para la solución analítica como para la aproximación. 
Utilice el valor de la gravedad g = 9.8 m/s². Emplee un tamaño de paso 
(diferencia de tiempo) de dos segundos.

Haga una gráfica de velocidad contra tiempo y compare entre la solución 
analítica y la aproximación.
"""

from decimal import Decimal, getcontext
import numpy as np
import matplotlib.pyplot as plt

# Establece la precisión decimal a 4 dígitos
getcontext().prec = 4

# Función para solicitar al usuario un valor decimal que cumpla una condición específica
def solicitar_valor(mensaje, condicion):
    while True:
        valor = Decimal(input(mensaje))
        if condicion(valor):
            return valor
        else:
            print("El valor no cumple con la condición requerida.")

# Se solicitan al usuario los valores de masa (m), gravedad (g)
# y coeficiente de resistencia (c), asegurando que sean positivos.

m = solicitar_valor("Ingrese el valor de la masa (debe ser positiva, ejemplo: 68.1): ", lambda valor: valor > 0)
g = solicitar_valor("Ingrese el valor de la gravedad (debe ser positiva, ejemplo: 9.8): ", lambda valor: valor > 0)
c = solicitar_valor("Ingrese el valor de la constante (debe ser positiva, ejemplo: 12.5): ", lambda valor: valor > 0)

# Se define el tamaño del paso (2 segundos) y 
# se genera un arreglo de tiempos desde 0 hasta 49 segundos.

dt = Decimal('2.0')
valores_t = [Decimal(i) for i in np.arange(0, 50, dt)]

# Se inicializa la velocidad para la fórmula numérica y 
# se crean listas para almacenar los resultados de ambas fórmulas.

valor_actual_formula = Decimal('0')
resultado_formula1 = []
resultado_formula2 = []

# Calcula las velocidades y guarda los resultados en un archivo de texto
with open('resultados_de_cv.txt', 'w') as file:
    file.write("Valores constantes:\n")
    file.write(f"m = {m} kg\n")
    file.write(f"g = {g} m/s^2\n")
    file.write(f"c = {c} kg/s\n")
    file.write("\nTiempo (t)   Velocidad Formula 1   Velocidad Formula 2\n")

    for t in valores_t:
        # Fórmula analítica
        velocidad_1 = ((m * g) / c) * (1 - Decimal(np.exp(-(c / m) * t)))
        resultado_formula1.append((t, velocidad_1))

        # Fórmula numérica (Euler)
        velocidad_2 = valor_actual_formula + (g - ((c / m) * valor_actual_formula)) * dt
        resultado_formula2.append((t, velocidad_2))

        file.write(f"{t:.2f}          {velocidad_1:.4f}               {velocidad_2:.4f}\n")
        valor_actual_formula = velocidad_2

print("Resultados y constantes guardados en 'resultados_de_cv.txt'")

# Se extraen los valores de tiempo y velocidad desde las listas 
# para graficar los resultados.

valores_t = [float(result[0]) for result in resultado_formula1]
velocidad_formula1 = [float(result[1]) for result in resultado_formula1]
velocidad_formula2 = [float(result[1]) for result in resultado_formula2]

# Se grafican los resultados de ambas fórmulas, se añaden etiquetas, 
# título, leyenda y cuadrícula. Luego, se guarda la gráfica como imagen PNG 
# y se muestra en pantalla.
plt.plot(valores_t, velocidad_formula1, label='Solución analítica')
plt.plot(valores_t, velocidad_formula2, label='Aproximación numérica')
plt.xlabel('Tiempo (t) [s]')
plt.ylabel('Velocidad (v) [m/s]')
plt.title('Comparación entre solución analítica y aproximación numérica')
plt.legend()
plt.grid(True)
plt.savefig('grafica_cv.png')
plt.show()
