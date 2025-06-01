
# calcular perimetro y area de un circulo
# Calcular el volumen de una esfera

# Perimetro = 2 * pi * radio
# Area = pi * radio^2
# Volumen = 4/3 * pi * radio^3

import math

print("Calculo de perimetro, area y volumn de un circulo")

radio = float(input("Ingrese el radio del circulo: "))

perimetro = 2 * math.pi * radio
area = math.pi * radio**2
volumen = 4/3 * math.pi * radio**3

print("El perimetro del circulo es: ", perimetro.__round__(2))
print("El area del circulo es: ", area.__round__(2))
print("El volumen de la esfera es: ", volumen.__round__(2))

# Fin del programa