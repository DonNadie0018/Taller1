#Ecuación de la distancia en función del tiempo para un objeto en caída libre
import math

# Parámetros
g = 9.8  # Aceleración debida a la gravedad (m/s^2)

# Función para calcular la distancia
def distancia_caida_libre(t):
    return 0.5 * g * t**2

# Ejemplo de uso
tiempo = float(input("Introduce el tiempo en segundos: "))
distancia = distancia_caida_libre(tiempo)
print(f"La distancia recorrida por el objeto es {distancia:.2f} metros.")


#Explicación:
#La función distancia_caida_libre(t) toma el tiempo 
#𝑡
#t como argumento y calcula la distancia recorrida usando la fórmula de la caída libre.
#El usuario ingresa el valor del tiempo, y el código imprime la distancia en metros.
