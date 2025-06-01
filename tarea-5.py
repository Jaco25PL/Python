# Implementar un refactoring del programa que lee los archivos de precios y compras y lista los datos de las compras más los totales, para que sea ejecutado con cualquier archivo de precios y compras en formato csv

# El programa debe:
# 	- si no se encuentra el precio de un artículo, indicarlo expresamente y no devolver un total.
# 	- En el caso de que una línea venga mal formateada, o con datos faltantes, avisar que se descarta dicha línea, tanto en el archivo de precios como en el de compras.
# 	- Implementar una clase compras, que soporte impresión (que tenga el método _str_)
# 	- si los archivos no están en el directorio actual, o tienen error de apertura o lectura el programa debe dar un error controlado. 
#  	- La lectura de ambos archivos, así como la impresión del resultado debe hacerse con funciones, se espera un cuerpo principal del programa de este tipo:

# 	precios = leer_precios("precios.csv")
# 	compras = leer_compras("compras.csv", precios)
# 	total = 0
# 	articulos = 0
# 	for compra in compras:
# 		print(compra)
# 		total = total + compra.total
# 		articulos = articulos + compra.cantidad
# 	print(f"total de compras {total} de {articulos} artículos")

class Compra:
    # constructor que inicializa una compra con producto, cantidad y precio opcional
    def __init__(self, producto, cantidad, precio_unitario=None):
        self.producto = producto
        self.cantidad = int(cantidad)
        self.precio_unitario = precio_unitario

        # calculamos el total multiplicando cantidad por precio, si no hay precio el total es 0
        if self.precio_unitario is not None:
            self.total = self.cantidad * self.precio_unitario
        else:
            self.total = 0

    # funcion que define como se muestra la compra cuando se imprime
    def __str__(self):
        if self.precio_unitario is not None:
            return f"Producto: {self.producto}, Cantidad: {self.cantidad}, Precio Unitario: ${self.precio_unitario:.2f}, Subtotal: ${self.total:.2f}"
        else:
            return f"Producto: {self.producto}, Cantidad: {self.cantidad} - (Precio no encontrado, este artículo no suma al total general)"

# funcion que lee el archivo de precios y devuelve un diccionario
def leer_precios(nombre_archivo):
    precios = {}
    try:
        # abrir archivo y lee linea por linea
        with open(nombre_archivo, 'r') as archivo:
            for numero_linea, linea in enumerate(archivo, 1):
                linea_limpia = linea.strip()
                
                if not linea_limpia: # salta lineas vacias
                    continue
                
                # separa la linea por comas
                partes = linea_limpia.split(',')
                # verifica que tenga exactamente 2 partes (producto y precio)
                if len(partes) == 2:
                    producto = partes[0].strip()
                    precio_str = partes[1].strip()
                    
                    # verifica que el nombre del producto no este vacio
                    if not producto:
                        print(f"Advertencia: Línea {numero_linea} en {nombre_archivo} descartada - nombre de producto vacío: '{linea_limpia}'")
                        continue
                        
                    try:
                        precio = float(precio_str)
                        precios[producto] = precio
                    except ValueError:
                        # si no se puede convertir a numero, descarta la linea
                        print(f"Advertencia: Línea {numero_linea} en {nombre_archivo} descartada - precio inválido '{precio_str}': '{linea_limpia}'")
                else:
                    # si no tiene exactamente 2 partes, descarta la linea
                    print(f"Advertencia: Línea {numero_linea} en {nombre_archivo} descartada - formato incorrecto (esperado: producto,precio): '{linea_limpia}'")
                    
    except FileNotFoundError:
        print(f"Error controlado: El archivo {nombre_archivo} no se encontró en el directorio actual.")
        return None
    except PermissionError:
        print(f"Error controlado: No se tienen permisos para leer el archivo {nombre_archivo}.")
        return None
    except Exception as e:
        print(f"Error controlado: Error inesperado al leer {nombre_archivo}: {e}")
        return None
    
    return precios

# funcion que lee el archivo de compras y devuelve una lista de objetos compra
def leer_compras(nombre_archivo_compras, dict_precios):
    lista_de_compras = []
    
    # si no se pudieron cargar los precios, no se pueden procesar compras
    if dict_precios is None:
        print("No se pueden procesar las compras porque hubo un error al cargar los precios.")
        return lista_de_compras

    try:
        # leer linea por linea del archivo de compras
        with open(nombre_archivo_compras, 'r') as archivo:
            for numero_linea, linea in enumerate(archivo, 1):
                linea_limpia = linea.strip()
                
                if not linea_limpia: # salta lineas vacias
                    continue

                # separar la linea por comas
                partes = linea_limpia.split(',')

                if len(partes) == 2:
                    producto_nombre = partes[0].strip()
                    cantidad_str = partes[1].strip()

                    # verifica que el nombre del producto no este vacio
                    if not producto_nombre:
                        print(f"Advertencia: Línea {numero_linea} en {nombre_archivo_compras} descartada - nombre de producto vacío: '{linea_limpia}'")
                        continue
                        
                    try:
                        # convierte la cantidad a numero entero
                        cantidad = int(cantidad_str)

                        if cantidad <= 0:
                            print(f"Advertencia: Línea {numero_linea} en {nombre_archivo_compras} descartada - cantidad debe ser positiva '{cantidad_str}': '{linea_limpia}'")
                            continue
                            
                        # busca el precio del producto en el diccionario
                        precio_unit = dict_precios.get(producto_nombre)
                        
                        # si no se encuentra el precio, muestra una advertencia
                        if precio_unit is None:
                            print(f"Advertencia: Para la compra '{producto_nombre}' (cantidad: {cantidad}) no se encontró precio en la lista. Este artículo no sumará al total.")
                        
                        # crear un objeto Compra y agregarlo a la lista
                        compra = Compra(producto_nombre, cantidad, precio_unit)
                        lista_de_compras.append(compra)
                        
                    except ValueError:
                        # si no se puede convertir la cantidad a entero, descarta la linea
                        print(f"Advertencia: Línea {numero_linea} en {nombre_archivo_compras} descartada - cantidad inválida '{cantidad_str}': '{linea_limpia}'")
                else:
                    # si no tiene exactamente 2 partes, descarta la linea
                    print(f"Advertencia: Línea {numero_linea} en {nombre_archivo_compras} descartada - formato incorrecto (esperado: producto,cantidad): '{linea_limpia}'")
                    
    except FileNotFoundError:
        print(f"Error controlado: El archivo {nombre_archivo_compras} no se encontró en el directorio actual.")
    except PermissionError:
        print(f"Error controlado: No se tienen permisos para leer el archivo {nombre_archivo_compras}.")
    except Exception as e:
        print(f"Error controlado: Error inesperado al leer {nombre_archivo_compras}: {e}")
        
    return lista_de_compras

# programa principal
if __name__ == "__main__":
    precios = leer_precios("precios.csv")
    compras = leer_compras("compras.csv", precios)
    total = 0
    articulos = 0
    for compra in compras:
        print(compra)
        total = total + compra.total
        articulos = articulos + compra.cantidad
    print(f"total de compras {total} de {articulos} artículos")

