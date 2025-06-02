import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve

def splines_cubicos(x, y):
    n = len(x) - 1
    h = np.diff(x)
    
    # Construir matriz tridiagonal A
    A = np.zeros((n+1, n+1))
    for i in range(1, n):
        A[i, i-1:i+2] = [h[i-1], 2*(h[i-1] + h[i]), h[i]]
    
    # Condiciones de frontera naturales (segundas derivadas en los extremos son cero)
    A[0, 0] = 1  # Primera condición (Las segundas derivadas en los nodos extremos son cero)
    A[-1, -1] = 1  # Segunda condición (Las segundas derivadas en los nodos extremos son cero)
    
    # Construir el vector b
    b = np.zeros(n+1)
    for i in range(1, n):
        b[i] = 3 * (y[i+1] - y[i]) / h[i] - 3 * (y[i] - y[i-1]) / h[i-1]
    
    # Resolver el sistema de ecuaciones lineales
    c = solve(A, b)
    
    # Calcular los coeficientes a, b, d
    a = y[:-1]
    b = (y[1:] - y[:-1]) / h - h * (c[:-1] + 2 * c[1:]) / 3
    
    # Ajustar la longitud de c para que coincida con h
    c = c[:-1]
    
    # Corregir el cálculo de d
    d = np.zeros_like(c)
    d = (c[1:] - c[:-1]) / (3 * h[1:])

    
    return a, b, c, d

def evaluar_spline(x, a, b, c, d, x_eval):
    # Encontrar el índice del intervalo en el que se encuentra x_eval
    idx = np.searchsorted(x, x_eval) - 1
    idx = np.clip(idx, 0, len(x)-2)
    
    # Evaluar el spline cúbico en x_eval
    dx = x_eval - x[idx]
    resultado = a[idx] + b[idx] * dx + c[idx] * dx**2 + d[idx] * dx**3
    
    return resultado

def plot_interpolacion(x, y, a, b, c, d):
    x_vals = np.linspace(min(x), max(x), 1000)
    y_vals = [evaluar_spline(x, a, b, c, d, x_val) for x_val in x_vals]
    
    plt.scatter(x, y, color='red', label='Puntos dados')
    plt.plot(x_vals, y_vals, label='Interpolación con Splines Cúbicos')
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Interpolación con Splines Cúbicos')
    plt.legend()
    plt.show()

def main():
    # Datos de entrada
    x = np.array([3.0, 4.5, 7.0, 9.0])
    y = np.array([2.5, 1.0, 2.5, 0.5])
    
    # Calcular coeficientes del spline cúbico
    a, b, c, d = splines_cubicos(x, y)
    
    # Graficar la interpolación
    plot_interpolacion(x, y, a, b, c, d)

if __name__ == "__main__":
    main()
