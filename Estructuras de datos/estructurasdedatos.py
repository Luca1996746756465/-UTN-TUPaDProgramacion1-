precios_frutas = {"Banana": 1200, "Ananá": 2500, "Melón": 3000, "Uva": 1450}

# Añadimos los nuevos productos con sus precios
precios_frutas["Naranja"] = 1200
precios_frutas["Manzana"] = 1500
precios_frutas["Pera"] = 2300

print(precios_frutas)


#Ejercicio 2

precios_frutas["Banana"]=1300
precios_frutas["Uva"]=1800
precios_frutas["Pera"]=2000
print(precios_frutas)

#Ejercicio 3

listas_fruta= list(precios_frutas.keys())
print(precios_frutas)

#Ejercicio 4 
contactos={}

for i in range(5):
    nombre=input(f"Ingrese el nombre del contacto{i+1}")
    telefono=input(f"Ingrese el numero de telefono {nombre}")
    contactos[nombre]= telefono 

busqueda=input("Ingrese el nombre del contacto que desee consultar")
if busqueda in contactos:
    print(f"el numero de {busqueda} es: {contactos[busqueda]}")
else:
    print("El contacto no existe en la agenda")

#Ejercicio 5 
frase=input("Ingrese una frase")

palabras = frase.split()

palabras_unicas=set(palabras)

recuento={}

for palabra in palabras:
    if palabra in recuento:
        recuento[palabra] += 1
    else:
        recuento[palabra] = 1

print("palabras unicas:" ,palabras_unicas)
print("Recuentro:" , recuento)

#Ejercicio 6
alumnos = {}

for i in range(3):
    nombre = input(f"Nombre del alumno {i + 1}: ")
    nota1 = float(input("Nota 1: "))
    nota2 = float(input("Nota 2: "))
    nota3 = float(input("Nota 3: "))
    alumnos[nombre] = (nota1, nota2, nota3)

print(" Promedios")
for nombre, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"{nombre}: {promedio:.2f}")

#Ejercicio 7
parcial_1 = {101, 102, 103, 104, 105}
parcial_2 = {103, 104, 106, 107}

ambos= parcial_1 & parcial_2

solo_uno= parcial_1 ^ parcial_2

al_menosuno= parcial_1 | parcial_2

print("Aprobaron ambos:", ambos)
print("Aprobaron solo uno",solo_uno)
print("Almenos aprobaron uno:",al_menosuno)

#Ejercicio 8
stock = {"Manzanas": 50, "Pera": 30, "Banana": 20}

producto = input("Ingrese el nombre del producto a consultar/gestionar: ")

if producto in stock:
    print(f"El stock actual de {producto} es: {stock[producto]}")
    agregar = input("¿Desea agregar unidades a este producto? (si/no): ")
    if agregar.lower() == "si":
        cantidad = int(input("Ingrese la cantidad a sumar: "))
        stock[producto] += cantidad
        print(f"Nuevo stock de {producto}: {stock[producto]}")
else:
    print(f"El producto '{producto}' no existe.")
    agregar_nuevo = input("¿Desea agregarlo al inventario? (si/no): ")
    if agregar_nuevo.lower() == "si":
        cantidad = int(input("Ingrese el stock inicial: "))
        stock[producto] = cantidad
        print(f"Producto {producto} agregado con {cantidad} unidades.")

#Ejercicio 9
agenda = {
    ("Lunes", "10:00"): "Reunión",
    ("Martes", "15:00"): "Clase de inglés",
    ("Miercoles", "18:00"): "Gimnasio",
    ("Jueves", "19:00"): "Hora de Jugar",
    ("viernes", "14:00"): "Estudio",
    }

dia=input("Ingrese el dia a consultar:").lower()
hora=input("Ingrese la hora a consultar:")

clave_busqueda=(dia,hora)

if clave_busqueda in agenda:
    print(f"Actividad programada {agenda[clave_busqueda]}")
else:
    print("No hay ninguna actividad programada para ese dia y hora")
#Ejercicio 10 
original = {"Argentina": "Buenos Aires", "Chile": "Santiago", "Uruguay": "Montevideo"}

invertido = {}
for pais, capital in original.items():
    invertido[capital] = pais

print("Diccionario original:", original)
print("Diccionario invertido:", invertido)