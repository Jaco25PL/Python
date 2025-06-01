# Dado el archivo precios.csv
# Leer el archivo y cargar cada dato en un diccionario
# Dado el archivo compras.csv
# Leer el archivo y en cada línea listar el producto, la cantidad comprada y multiplicar el producto por el precio obtenido en la lectura del archivo anterior, usando el diccionario
# Listar el total del monto de compras

# en cada archivo el contenido debe ser
# Precios.csv
# Tornillo, 100
# Tuerca, 200
# Arandela, 300

# Compras.csv
# Tornillo, 20
# Tuerca, 30
# Arandela, 40
# Tornillo, 20
# Tuerca, 10
# Arandela, 20

# Leer el archivo precios.csv y cargar cada dato en un diccionario
def cargar_precios():
    precios = {}
    with open('Precios.csv', 'r') as archivo_precios:
        for linea in archivo_precios:
            producto, precio_str = linea.strip().split(',')
            precios[producto] = float(precio_str)
    return precios

# Leer el archivo compras.csv y calcular el total de compras
def calcular_total_compras(precios_dict):
    total_general = 0
    with open('Compras.csv', 'r') as archivo_compras:
        print("\nDetalle de compras:")
        for linea in archivo_compras:
            producto, cantidad_str = linea.strip().split(',')
            cantidad = int(cantidad_str)
            if producto in precios_dict:
                precio_unitario = precios_dict[producto]
                subtotal_producto = precio_unitario * cantidad
                
                print(f"Producto: {producto}, Cantidad: {cantidad}, Precio Unitario: {precio_unitario}, Subtotal: {subtotal_producto}")
                total_general += subtotal_producto
            else:
                print(f"Advertencia: Producto '{producto}' (Cantidad: {cantidad}) no encontrado en la lista de precios. No se sumará al total.")
    return total_general

# Programa
if __name__ == "__main__":
    # 1. Cargar precios desde Precios.csv
    diccionario_precios = cargar_precios()

    # 2. Calcular total de compras y listar cada una
    monto_total_compras = calcular_total_compras(diccionario_precios)

    # 3. Listar el total del monto de compras
    print(f"\nEl monto total de todas las compras es: {monto_total_compras}")