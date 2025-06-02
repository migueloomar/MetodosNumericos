# Escribe un programa para obtener la solución de un polinomio de un punto, 
# usando el metodo de horner

# Este bloque implementa el método de Horner para evaluar un polinomio 
# en un punto dado. Además, muestra cada paso intermedio de la evaluación 
# y devuelve el resultado final.

def horner(coeficientes, x):
    n = len(coeficientes)
    resultado = coeficientes[0]

    for i in range(1, n):
        resultado = resultado * x + coeficientes[i]
        print(f"b[{i}] = {resultado}")
    return resultado

# Se solicita al usuario la cantidad de coeficientes que tendrá el polinomio.
# Luego, se ingresan uno a uno y se almacenan en una lista.
# El orden ingresado sigue el formato desde el coeficiente de mayor grado
# hasta el término independiente.

num_coeficientes = int(input("Ingrese la cantidad de coeficientes: "))
coeficientes = []

for i in range(num_coeficientes):
    coef = float(input(f"Ingrese el coeficiente a_{num_coeficientes - i - 1}: "))
    coeficientes.append(coef)

# Cada coeficiente ingresado se convierte a su representación binaria
# y se almacena en una nueva lista para fines de visualización.

coeficientes_binarios = [bin(int(coef))[2:] for coef in coeficientes]

# Se solicita al usuario el valor en el cual se desea evaluar el polinomio,
# tanto en su forma decimal como en su equivalente binaria.

valor_x_decimal = float(input("\nIngrese el valor de x en decimal: "))
valor_x_binario = bin(int(valor_x_decimal))[2:]

# Se llama al método de Horner para calcular el valor del polinomio en x.
# El resultado se almacena para ser mostrado al final.

resultado = horner(coeficientes, valor_x_decimal)

# Se construye una representación en forma de cadena del polinomio,
# usando los coeficientes en binario. También se imprime cada coeficiente 
# con su respectivo índice para mayor claridad.

polinomio_str = "p(x) = "
for i, coef in enumerate(coeficientes_binarios[::-1]):
    polinomio_str += f"{coef}x^{num_coeficientes - 1 - i}"
    if i < num_coeficientes - 1:
        polinomio_str += " + "

print("\n" + polinomio_str)
for i, coef in enumerate(coeficientes_binarios):
    print(f"a_{num_coeficientes - 1 - i} = {coef}")

# Se imprime el resultado de evaluar el polinomio en x,
# mostrando tanto la forma decimal como la binaria del resultado.

print(f"\np({valor_x_decimal}) = {resultado}")
print(f"p({valor_x_binario}) = {bin(int(resultado))}")

'''
Ejemplo:
Ingrese la cantidad de coeficientes: 5
Ingrese el coeficiente a_4: 5
Ingrese el coeficiente a_3: 8
Ingrese el coeficiente a_2: 3
Ingrese el coeficiente a_1: 4
Ingrese el coeficiente a_0: 6

Ingrese el valor de x en decimal: 7
b[1] = 43.0
b[2] = 304.0
b[3] = 2132.0
b[4] = 14930.0

p(x) = 110x^4 + 100x^3 + 11x^2 + 1000x^1 + 101x^0  
a_4 = 101
a_3 = 1000
a_2 = 11
a_1 = 100
a_0 = 110

p(7.0) = 14930.0
p(111) = 0b11101001010010

'''
