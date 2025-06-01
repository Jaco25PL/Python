# Entregar por mail a pcgarcia@windowslive.com

# Entregar antes del 21/4

# Solicitar por teclado los datos de:
#  - año de nacimiento
#  - año de ingreso al trabajo
#  - sueldo
#  - monto pedido
#  - cantidad de cuotas

# Ud está evaluando un crédito para el solicitante, y debe aplicar estas reglas.

# NO se presta mas de 10 veces el sueldo
# NO se presta a menores de edad
# NO se presta a personas con menos de dos años de antigüedad laboral.

# Si el préstamo de hasta 3 veces el sueldo, se puede dar en hasta 3 cuotas.
# Si el préstamo es hasta 5 veces el sueldo, se puede dar en hasta 10 cuotas.
# Si el préstamos es de 5 a 10 veces el sueldo, se puede dar en hasta 20 cuotas y debe ser en al menos 10 cuotas.


# Imprimir, dada la cantidad de cuotas, el monto de la cuota con un interés total de 3% del monto por cantidad de cuotas.

print("Bienvenido al sistema de evaluación de créditos")

# Solicitar datos al usuario
anio_nacimiento = int(input("Ingrese su año de nacimiento: "))
anio_ingreso = int(input("Ingrese su año de ingreso al trabajo: "))
sueldo = float(input("Ingrese su sueldo mensual: "))
monto_pedido = float(input("Ingrese el monto del préstamo solicitado: "))
cantidad_cuotas = int(input("Ingrese la cantidad de cuotas deseadas: "))

# Calcular edad y antigüedad laboral
edad = 2023 - anio_nacimiento
antiguedad_laboral = 2023 - anio_ingreso

# Validar reglas básicas
if edad < 18:
    print("No se presta a menores de edad.")
elif antiguedad_laboral < 2:
    print("No se presta a personas con menos de dos años de antigüedad laboral.")
elif monto_pedido > 10 * sueldo:
    print("No se presta más de 10 veces el sueldo.")
else:
    # Determinar si el préstamo es válido según las reglas de cuotas
    if monto_pedido <= 3 * sueldo and cantidad_cuotas <= 3:
        valido = True
    elif monto_pedido <= 5 * sueldo and cantidad_cuotas <= 10:
        valido = True
    elif 5 * sueldo < monto_pedido <= 10 * sueldo and 10 <= cantidad_cuotas <= 20:
        valido = True
    else:
        valido = False

    if valido:
        # Calcular monto de la cuota con interés
        interes_total = monto_pedido * 0.03
        monto_total = monto_pedido + interes_total
        monto_cuota = monto_total / cantidad_cuotas
        print(f"Préstamo aprobado. El monto de cada cuota será de: ${monto_cuota:.2f}")
    else:
        print("La cantidad de cuotas no cumple con las reglas del préstamo.")