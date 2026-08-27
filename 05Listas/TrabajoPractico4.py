#1 Promedio de notas 
notas = [8.5, 7.0, 9.5, 4.0, 6.5, 10.0, 5.5, 8.0, 3.5, 9.0]
print("Notas de los estudiantes:")
for nota in notas:
    print(nota, end=" | ")
print("\n")

suma_notas = 0
nota_max = notas[0]
nota_min = notas[0]

for nota in notas:
    suma_notas += nota
    if nota > nota_max:
        nota_max = nota
    if nota < nota_min:
        nota_min = nota

promedio = suma_notas / len(notas)

print(f"Promedio general: {promedio:.2f}")
print(f"Nota más alta: {nota_max}")
print(f"Nota más baja: {nota_min}")

#2 Lista de productos para eliminar
productos = []
for i in range(5):
    prod = input(f"Ingrese el producto {i+1}: ")
    productos.append(prod)

productos_ordenados = sorted(productos)

print("\nLista ordenada alfabéticamente:")
for p in productos_ordenados:
    print(f"- {p}")
eliminar = input("\n¿Qué producto desea eliminar?: ")

if eliminar in productos:
    productos.remove(eliminar)
    print("\nLista actualizada:")
    for p in productos:
        print(f"- {p}")
else:
    print("El producto no se encuentra en la lista.")
#3 Lista con numeros ramdom 
import random

numeros_azar = []
for _ in range(15):
    numeros_azar.append(random.randint(1, 100))

pares = []
impares = []

for num in numeros_azar:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)
print("Lista original:")
for n in numeros_azar: print(n, end=" ")

print("\n\nLista de Pares:")
for p in pares: print(p, end=" ")
print(f"\nCantidad de pares: {len(pares)}")

print("\nLista de Impares:")
for imp in impares: print(imp, end=" ")
print(f"\nCantidad de impares: {len(impares)}")

#4 remover datos de la lista 
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
sin_repetidos = []

for elemento in datos:
    if elemento not in sin_repetidos:
        sin_repetidos.append(elemento)

print("Lista sin elementos repetidos:")
for elemento in sin_repetidos:
    print(elemento, end=" ")
print()

#5 Lista de alumnos que puede eliminar y agregar estudiantes
estudiantes = ["Ana", "Bruno", "Carlos", "Diana", "Emiliano", "Fiona", "Gabriel", "Julia"]

print("Lista actual de estudiantes:")
for est in estudiantes: print(f"• {est}")

opcion = input("\n¿Desea [A]gregar o [E]liminar un estudiante? (A/E): ").upper()

if opcion == "A":
    nuevo = input("Ingrese el nombre del nuevo estudiante: ")
    estudiantes.append(nuevo)
elif opcion == "E":
    eliminar = input("Ingrese el nombre del estudiante a eliminar: ")
    if eliminar in estudiantes:
        estudiantes.remove(eliminar)
    else:
        print("El estudiante no estaba en la lista.")
else:
    print("Opción no válida.")

print("\nLista final actualizada:")
for est in estudiantes: print(f"• {est}")


# 6 Rotacion
lista_numeros = [10, 20, 30, 40, 50, 60, 70]

print("Lista original:")
for n in lista_numeros: print(n, end=" ")
print()

ultimo = lista_numeros[-1]

for i in range(len(lista_numeros) - 1, 0, -1):
    lista_numeros[i] = lista_numeros[i - 1]

lista_numeros[0] = ultimo

print("Lista rotada a la derecha:")
for n in lista_numeros: print(n, end=" ")
print()

# 7 registros de la temperatura en la semana 

temperaturas = [
    [12, 22],  # Lunes
    [14, 25],  # Martes
    [15, 28],  # Miércoles
    [10, 19],  # Jueves
    [11, 24],  # Viernes
    [13, 26],  # Sábado
    [16, 29]   # Domingo
]
dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]

suma_min = 0
suma_max = 0
max_amplitud = 0
dia_max_amplitud = ""

for i in range(len(temperaturas)):
    minima = temperaturas[i][0]
    maxima = temperaturas[i][1]
    
    suma_min += minima
    suma_max += maxima
    
    amplitud = maxima - minima
    if amplitud > max_amplitud:
        max_amplitud = amplitud
        dia_max_amplitud = dias[i]

promedio_min = suma_min / 7
promedio_max = suma_max / 7

print(f"Promedio de temperaturas Mínimas: {promedio_min:.2f}°C")
print(f"Promedio de temperaturas Máximas: {promedio_max:.2f}°C")
print(f"La mayor amplitud térmica fue de {max_amplitud}°C el día {dia_max_amplitud}.")


#8 Notas de los estudiantes para ver cuanto te sacaste 
notas_matriz = [
    [8, 7, 9],  # Estudiante 1
    [6, 5, 7],  # Estudiante 2
    [9, 10, 8], # Estudiante 3
    [4, 6, 5],  # Estudiante 4
    [7, 8, 8]   # Estudiante 5
]

for i in range(5):
    suma_estudiante = 0
    for j in range(3):
        suma_estudiante += notas_matriz[i][j]
    promedio_est = suma_estudiante / 3
    print(f"Promedio del Estudiante {i+1}: {promedio_est:.2f}")

print("-" * 30)
for j in range(3):
    suma_materia = 0
    for i in range(5):
        suma_materia += notas_matriz[i][j]
    promedio_mat = suma_materia / 5
    print(f"Promedio de la Materia {j+1}: {promedio_mat:.2f}")
    # Ta-te-ti
    tablero = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
]

def mostrar_tablero(t):
    print("\nTablero actual:")
    for fila in t:
        for casilla in fila:
            print(casilla, end=" ")
        print()
    print()

jugador_actual = "X"

for jugada in range(6):
    mostrar_tablero(tablero)
    print(f"Turno del Jugador [{jugador_actual}]")
    

    fila = int(input("Ingrese fila (1, 2, 3): ")) - 1
    columna = int(input("Ingrese columna (1, 2, 3): ")) - 1
    
    if 0 <= fila <= 2 and 0 <= columna <= 2 and tablero[fila][columna] == "-":
        tablero[fila][columna] = jugador_actual
        
        jugador_actual = "O" if jugador_actual == "X" else "X"
    else:
        print("Posición inválida u ocupada. Pierde el turno por distraído.")

mostrar_tablero(tablero)
print("Fin de las jugadas de prueba.")

# 10 Total de ventas del mes de una tienda de electronica (en comentarios puse algunos productos para identificar)
ventas = [
    [10, 15, 20, 12, 18, 25, 30],  # Producto 1 ejemplo: Playstation 5
    [5,  8,  12, 6,  10, 15, 20],  # Producto 2 ejemplo: Xbox series x
    [22, 25, 28, 30, 35, 40, 50],  # Producto 3 ejemplo: Nintendo Switch 2
    [15, 12, 10, 14, 11, 18, 22]   # Producto 4 ejemplo: Steam deck
]

dias = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
totales_por_producto = [0, 0, 0, 0]
totales_por_dia = [0, 0, 0, 0, 0, 0, 0]


for i in range(4): 
    for j in range(7): 
        totales_por_producto[i] += ventas[i][j]
        totales_por_dia[j] += ventas[i][j]


print("Total vendido por producto en la semana:")
for i in range(4):
    print(f"Producto {i+1}: {totales_por_producto[i]} unidades")

print("-" * 40)

max_ventas_dia = totales_por_dia[0]
indice_dia_max = 0
for j in range(7):
    if totales_por_dia[j] > max_ventas_dia:
        max_ventas_dia = totales_por_dia[j]
        indice_dia_max = j

print(f"El día con mayores ventas totales fue el {dias[indice_dia_max]} con {max_ventas_dia} unidades.")

max_ventas_prod = totales_por_producto[0]
indice_prod_max = 0
for i in range(4):
    if totales_por_producto[i] > max_ventas_prod:
        max_ventas_prod = totales_por_producto[i]
        indice_prod_max = i

print(f"El producto más vendido en la semana fue el Producto {indice_prod_max+1} con {max_ventas_prod} unidades.")