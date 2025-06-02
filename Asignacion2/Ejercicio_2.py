"""
N.- 02) En clase se encontró que dado un x entre 0 y 1 y un entero β mayor que 1,
se puede generar recursivamente b₁, b₂, b₃, ... por:

        c₀ = x
        b₁ = (β * c₀)ₑ,       c₁ = (β * c₀)ₓ
        b₂ = (β * c₁)ₑ,       c₂ = (β * c₁)ₓ
        b₃ = (β * c₂)ₑ,       c₃ = (β * c₂)ₓ
        ...

Entonces:
        x = (.b₁b₂b₃...) = Σ (k=1 hasta ∞) de bₖ * β⁻ᵏ

(a) Realice un programa que implemente este algoritmo.
(b) Si x = (0.345)₁₀ utilice el programa para obtener su representación en binario.
"""

from decimal import Decimal, getcontext

# Configura la precisión decimal a 4 dígitos

getcontext().prec = 4

# Función que genera la sucesión b y c, y escribe los resultados en un archivo
# La sucesión se construye de forma recursiva usando:
#   b[i] = parte entera de (beta * c[i])
#   c[i+1] = parte fraccionaria de (beta * c[i])
# Además, calcula y guarda x usando la función calc_x en cada iteración

def sucesion(x, beta, n, resultado_final):
    b = [x]
    c = [x]
    for i in range(n):
        b_i = Decimal(beta * c[i]) ** 2 # Esta implementación eleva al cuadrado
        c_i = Decimal(beta * c[i]) - int(beta * c[i]) # Parte fraccionaria
        b.append(b_i)
        c.append(c_i)
        resultado_x = calc_x(b, beta)
        resultado_final.write(f"x = {x:.4f}, beta = {beta}, n = {i+1}, Resultado x = {resultado_x:.4f}\n")
    return b

# Función que evalúa la suma infinita truncada: 
#   x ≈ Σ (k = 1 hasta n) de b[k] * beta^(-k)

def calc_x(b, beta):
    x = Decimal(0)
    for k in range(len(b)):
        x += b[k] * Decimal(beta) ** -k
    return x

# Función auxiliar que solicita valores al usuario y valida condiciones impuestas

def solicitar_valor(mensaje, condicion):
    while True:
        valor = Decimal(input(mensaje))
        if condicion(valor):
            return valor
        else:
            print(f"El valor no cumple con la condición requerida.")

# Solicita los valores de x, beta y número de iteraciones, asegurando que cumplan las condiciones del problema

x = solicitar_valor("Ingrese el valor de x (entre 0 y 1): ", lambda valor: 0 <= valor <= 1)
beta = solicitar_valor("Ingrese el valor de beta (mayor que 1 y no negativo): ", lambda valor: valor > 1)
n = int(solicitar_valor("Ingrese el número de iteraciones (n mayor que 1 y no negativo): ", lambda valor: valor > 1))

# Abre el archivo 'resultado_ejercicio2a.txt' para guardar los resultados del proceso de conversión.
# En este bloque se realiza lo siguiente:
# 1. Se escribe una cabecera informativa en el archivo.
# 2. Se llama a la función 'sucesion' para generar las listas de valores b y c a lo largo de 'n' iteraciones,
#    registrando en el archivo el valor aproximado de x en cada paso.
# 3. Se toma el último valor generado de la sucesión como la mejor aproximación de x.
# 4. Se imprime ese valor con 4 cifras decimales en consola.
# 5. Se convierte ese valor aproximado de x a binario (usando su parte entera) y se muestra también por consola.

with open('resultado_ejercicio2a.txt', 'w') as resultado_final:
    resultado_final.write("Resultados para x, beta y n:\n")
    b = sucesion(x, beta, n, resultado_final)
    resultado_x = b[-1]  # Último valor calculado
    print(f"El valor de x es aproximadamente: {resultado_x:.4f}")
    x_binario = bin(int(resultado_x)) 
    print(f"El valor de x en binario: {x_binario}")

# Abre el archivo 'resultado_ejercicio2b.txt' 
with open('resultado_ejercicio2b.txt', 'w') as resultado_binario:
    resultado_binario.write(f"El valor de x en binario: {x_binario}\n")
