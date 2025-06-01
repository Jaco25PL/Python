## Implementar un refactoring del programa que lee los archivos de precios y compras y lista los datos de las compras más los totales, para que sea ejecutado con cualquier archivo de precios y compras en formato csv
 
# El programa debe:
 	- si no se encuentra el precio de un artículo, indicarlo expresamente y no devolver un total.
 	- En el caso de que una línea venga mal formateada, o con datos faltantes, avisar que se descarta dicha línea, tanto en el archivo de precios como en el de compras.
 	- Implementar una clase compras, que soporte impresión (que tenga el método _str_)
 	- si los archivos no están en el directorio actual, o tienen error de apertura o lectura el programa debe dar un error controlado. 
  	- La lectura de ambos archivos, así como la impresión del resultado debe hacerse con funciones, se espera un cuerpo principal del programa de este tipo:
 	```precios = leer_precios("precios.csv")
 	compras = leer_compras("compras.csv", precios)
 	total = 0
 	articulos = 0
 	for compra in compras:
 		print(compra)
 		total = total + compra.total
 		articulos = articulos + compra.cantidad
 	print(f"total de compras {total} de {articulos} artículos")```

