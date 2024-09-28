import math

# Parámetros
T_a = float(input("Introduce la temperatura ambiente (°C): "))
T_0 = float(input("Introduce la temperatura inicial (°C): "))
k = float(input("Introduce la constante de enfriamiento: "))
t = float(input("Introduce el tiempo en minutos: "))

# Función para calcular la temperatura según la ley de enfriamiento de Newton
def temperatura_enfriamiento(T_a, T_0, k, t):
    return T_a + (T_0 - T_a) * math.exp(-k * t)

# Cálculo de la temperatura
T_t = temperatura_enfriamiento(T_a, T_0, k, t)
print(f"La temperatura después de {t} minutos es {T_t:.2f} °C.")


#Explicación:
#La función temperatura_enfriamiento() implementa la fórmula de la ley de enfriamiento de Newton.
#El usuario ingresa la temperatura inicial, la temperatura ambiente, la constante de enfriamiento y el tiempo.
#Luego, el código calcula la temperatura del objeto en ese momento.