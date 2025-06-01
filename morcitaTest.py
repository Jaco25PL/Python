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

Año = int(input("Ingrese año de nacimiento: "))
AñoDeIngresoTrabajo = int(input("Ingrese año de ingreso al trabajo: "))
sueldo = int(input("Ingrese sueldo: "))
MontoSolicitado = int(input("Ingrese monto solicitado: "))
Cuotas = int(input("Ingrese cantidad de cuotas: "))

print("Calculando...")

año_actual = 2025

edad = año_actual - Año
if edad < 18:
    print("No se puede otorgar el préstamo: El solicitante es menor de edad")
else:
    #Antiguedad laboral
    antiguedad = año_actual - AñoDeIngresoTrabajo
    if antiguedad < 2:
        print("No se puede otorgar el préstamo: El solicitante tiene menos de 2 años de antigüedad laboral")
    else:
        #Monto solicitado
        relacion_monto_sueldo = MontoSolicitado / sueldo
        if relacion_monto_sueldo > 10:
            print("No se puede otorgar el préstamo: El monto solicitado supera 10 veces el sueldo")
        else:
            #Cuotas según el monto
            es_aprobado = False
            if relacion_monto_sueldo <= 3:
                if Cuotas <= 3:
                    es_aprobado = True
                else:
                    print(f"Para préstamos de hasta 3 sueldos, el máximo de cuotas es 3.")
            elif relacion_monto_sueldo <= 5:
                if Cuotas <= 10:
                    es_aprobado = True
                else:
                    print(f"Para préstamos de hasta 5 sueldos, el máximo de cuotas es 10.")
            else:  #relacion monto sueldo entre 5 y 10
                if 10 <= Cuotas <= 20:
                    es_aprobado = True
                else:
                    print(f"Para préstamos entre 5 y 10 sueldos, las cuotas deben estar entre 10 y 20.")

            if es_aprobado:
                #Cálculo del interés total: 3% del monto por cantidad de cuotas
                interes_total = MontoSolicitado * 0.03 * Cuotas
                monto_total = MontoSolicitado + interes_total
                valor_cuota = monto_total / Cuotas
                
                print("")
                print("¡PRÉSTAMO APROBADO!")
                print(f"Monto solicitado: ${MontoSolicitado}")
                print(f"Interés total: ${interes_total:.2f} (3% mensual)")
                print(f"Monto total a pagar: ${monto_total:.2f}")
                print(f"Cantidad de cuotas: {Cuotas}")
                print(f"Valor de cada cuota: ${valor_cuota:.2f}")
            else:
                print("El préstamo no ha sido aprobado por incumplimiento de las condiciones.")
