# Ecuación de la parábola: y(x) = ax^2 + bx + c

# Parámetros
a = float(input("Introduce el valor de a: "))
b = float(input("Introduce el valor de b: "))
c = float(input("Introduce el valor de c: "))
x = float(input("Introduce el valor de x: "))

# Función para calcular y(x) según la ecuación de la parábola
def parabola(a, b, c, x):
    return a * x**2 + b * x + c

# Cálculo de y(x)
y_x = parabola(a, b, c, x)
print(f"El valor de y({x}) es {y_x:.2f}")