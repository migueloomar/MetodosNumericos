"""
N.-01) En el programa desarrollado para calcular la velocidad en función del tiempo 
para un paracaidista (con fuerza de arrastre Fd = c * v), considerando una masa 
m = 68.1 kg y un coeficiente de resistencia c = 12.5 kg/s, se utilizó la siguiente 
ecuación aproximada:

    v(t) = v(t) + [g - (c / m) * v(t)] * Δt

Incorpore adecuaciones al programa para calcular los errores relativos: 
el error relativo aproximado (ea) y el error relativo verdadero (es). 
Utilice aritmética de 4 dígitos de precisión y finalice el programa cuando 
|ea| < es = 0.05 %.
"""

import numpy as np
import matplotlib.pyplot as plt
from decimal import Decimal, getcontext

# Configura la precisión decimal a 4 dígitos
# Función para solicitar un valor decimal que cumpla con una condición específica

getcontext().prec = 4

def solicitar_valor(mensaje, condicion):
    while True:
        valor = Decimal(input(mensaje))
        if condicion(valor):
            return valor
        else:
            print(f"El valor no cumple con la condición requerida.")

# Solicita al usuario los valores de masa (m), gravedad (g) y coeficiente de fricción (c)

m = solicitar_valor("Ingrese el valor de la masa (debe ser positiva, ejemplo: 68.1): ", lambda valor: valor > 0)
g = solicitar_valor("Ingrese el valor de la gravedad (debe ser positiva, ejemplo: 9.8): ", lambda valor: valor > 0)
c = solicitar_valor("Ingrese el valor de la constante (debe ser positiva, ejemplo: 12.5): ", lambda valor: valor > 0)

# Define el tamaño del paso temporal (Δt) como 2 segundos
# Genera los valores de tiempo t desde 0 hasta 48 con incrementos de 2 segundos

dt = Decimal('2.0')
valores_t = np.arange(0, 50, dt)

# Inicializa la velocidad inicial para el método de aproximación (fórmula 2)
# Listas para almacenar los resultados de ambas fórmulas

valor_actual_formula2 = Decimal('0')
resultado_formula1 = []
resultado_formula2 = []

# Este bloque abre un archivo de texto para registrar los resultados del cálculo de velocidades
# usando dos métodos: la solución analítica y la aproximación numérica. También calcula el error
# relativo verdadero (comparado con la solución exacta) y el error relativo aproximado (comparado
# con el valor anterior) en cada paso. El programa se detiene automáticamente si el error
# aproximado cae por debajo del umbral del 0.05%.

with open('resultados_ejercicio1.txt', 'w') as file:
    file.write("Valores constantes: \n")
    file.write(f"m = {m} kg\n")
    file.write(f"g = {g} m/s^2\n")
    file.write(f"c = {c} kg/s\n")
    file.write("\nTiempo (t)   Velocidad Formula1   Velocidad Formula2   Error Relativo Verdadero   Error Relativo Aproximado\n")
    # Error relativo deseado (0.05% en forma decimal)
    error_relativo_deseado = Decimal('0.0005') 
    
    for t in valores_t:
        # Fórmula 1: v(t) = (mg/c) * (1 - e^(-(c/m)t))
        velocidad_1 = ((m * g) / c) * (1 - Decimal(np.exp(-c / m * t)))
        resultado_formula1.append((t, velocidad_1))
        
        # Fórmula 2: v(t_{i+1}) = v(t_i) + [g - (c/m)v(t_i)] * (t_{i+1} - t_i)
        velocidad_2 = valor_actual_formula2 + (g - (c / m) * valor_actual_formula2) * (t - (t - dt))
        resultado_formula2.append((t, velocidad_2))
        
        # Calcula errores relativos
        # Si la velocidad analítica es cero, se evita la división por cero
        if velocidad_1 == Decimal('0'):
            error_verdadero = Decimal('0')
        else:
            error_verdadero = abs(velocidad_1 - velocidad_2) / abs(velocidad_1)
        error_aproximado = abs(velocidad_2 - valor_actual_formula2) / abs(velocidad_2)
        
        file.write(f"{t:.2f}          {velocidad_1:.4f}               {velocidad_2:.4f}               {error_verdadero:.4f}               {error_aproximado:.4f}\n")
        valor_actual_formula2 = velocidad_2
        
        # Detiene la simulación si el error relativo aproximado es suficientemente pequeño
        if abs(error_aproximado) < error_relativo_deseado:
            break

print("Resultados guardados en 'resultados_ejercicio1.txt'")

# Extrae valores numéricos para graficar

valores_t = [float(result[0]) for result in resultado_formula1]
velocidad_formula1 = [float(result[1]) for result in resultado_formula1]
velocidad_formula2 = [float(result[1]) for result in resultado_formula2]

# Genera la gráfica de velocidad contra tiempo

plt.plot(valores_t, velocidad_formula1, label='Metodo matemático')
plt.plot(valores_t, velocidad_formula2, label='Aproximación')
plt.xlabel('Tiempo (t)')
plt.ylabel('Velocidad (v)')
plt.title('Gráfica cv')
plt.legend()
plt.grid(True)

# Guarda la gráfica como imagen PNG
# Se muestra en pantalla

plt.savefig('grafica_cv.png')
print("Gráfica guardada como 'grafica_cv.png'")
plt.show()







