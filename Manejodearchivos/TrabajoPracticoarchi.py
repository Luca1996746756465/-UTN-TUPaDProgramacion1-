# ==============================================================================
# ACTIVIDAD 1: Crear el archivo inicial 'productos.txt' si no existe
# ==============================================================================
# El modo 'w' sobrescribe el archivo o lo crea si no existe
with open("productos.txt", "w", encoding="utf-8") as archivo:
    archivo.write("Lapicera,120.5,30\n")
    archivo.write("Cuaderno,450.0,15\n")
    archivo.write("Goma,80.0,50\n")


# ==============================================================================
# ACTIVIDAD 4 y 2: Leer el archivo y cargarlo en una lista de diccionarios
# ==============================================================================
productos = []

# Abrimos en modo lectura 'r'
with open("productos.txt", "r", encoding="utf-8") as archivo:
    for linea in archivo:
        # .strip() elimina saltos de línea (\n) o espacios extra alrededor
        # .split(",") divide la cadena en una lista de strings por la coma
        datos = linea.strip().split(",")

        if len(datos) == 3:  # Validamos que la línea tenga el formato correcto
            nombre = datos[0]
            precio = float(datos[1])
            cantidad = int(datos[2])

            # Creamos el diccionario para cada producto
            prod_dict = {
                "nombre": nombre,
                "precio": precio,
                "cantidad": cantidad,
            }

            # Lo agregamos a nuestra lista en memoria
            productos.append(prod_dict)

# Mostrar los productos leídos formateados (Actividad 2)
print("--- LISTA DE PRODUCTOS ACTUALES ---")
for p in productos:
    print(
        f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}"
    )
print("-" * 35)


# ==============================================================================
# ACTIVIDAD 3: Agregar productos desde teclado sin borrar lo anterior
# ==============================================================================
print("\n--- AGREGAR NUEVO PRODUCTO ---")
nuevo_nombre = input("Ingrese el nombre del nuevo producto: ")
nuevo_precio = float(input("Ingrese el precio: "))
nueva_cantidad = int(input("Ingrese la cantidad: "))

# El modo 'a' (append) agrega líneas al final del archivo sin borrar el contenido previo
with open("productos.txt", "a", encoding="utf-8") as archivo:
    archivo.write(f"{nuevo_nombre},{nuevo_precio},{nueva_cantidad}\n")

# También actualizamos nuestra lista en memoria
productos.append(
    {
        "nombre": nuevo_nombre,
        "precio": nuevo_precio,
        "cantidad": nueva_cantidad,
    }
)
print("¡Producto agregado con éxito!")


# ==============================================================================
# ACTIVIDAD 5: Buscar producto por nombre en la lista de diccionarios
# ==============================================================================
print("\n--- BÚSQUEDA DE PRODUCTO ---")
busqueda = input("Ingrese el nombre del producto a buscar: ")

encontrado = False
for p in productos:
    # Usamos .lower() para comparar sin importar mayúsculas/minúsculas
    if p["nombre"].lower() == busqueda.lower():
        print(
            f"--> ¡ENCONTRADO!: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}"
        )
        encontrado = True
        break

if not encontrado:
    print(f"--> ERROR: El producto '{busqueda}' no existe en el registro.")


# ==============================================================================
# ACTIVIDAD 6: Guardar los productos actualizados desde la lista al archivo
# ==============================================================================
# Si hicimos cambios en la lista 'productos', sobrescribimos el archivo completo
with open("productos.txt", "w", encoding="utf-8") as archivo:
    for p in productos:
        archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")

print(
    "\n--> Archivo 'productos.txt' sincronizado y guardado con éxito final."
)