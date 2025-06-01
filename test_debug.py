import sys
sys.path.append('.')

# Importar las funciones
exec(open('tarea-5.py').read())

print("=== PROBANDO LECTURA DE PRECIOS ===")
precios = leer_precios("precios.csv")
print(f"Precios cargados: {precios}")

print("\n=== PROBANDO LECTURA DE COMPRAS CON ERRORES ===")
compras = leer_compras("compras_con_errores.csv", precios)
print(f"Numero de compras procesadas: {len(compras)}")

print("\n=== DETALLE DE CADA COMPRA ===")
total = 0
articulos = 0
for i, compra in enumerate(compras):
    print(f"Compra {i+1}: {compra}")
    total += compra.total
    articulos += compra.cantidad

print(f"\nTotal: {total}, Articulos: {articulos}")
