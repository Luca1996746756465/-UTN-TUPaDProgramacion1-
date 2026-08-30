#Ejercicio 1 
multiplos=(list(range(0,101,4)))
print(f"La lista de multiplos de 4:{multiplos}")

#Ejercicio 2 
Mejores_Videojuegos=["Sonic Unleashed","Persona5royal","Megamanx5","Trails in the sky","Kingdom hearts 3"]

print(f"El penultimo de la lista es:{Mejores_Videojuegos[-2]}")

#Ejercicio 3
Juegos=[]

Juegos.append("Sonic")
Juegos.append("Mario")
Juegos.append("Megaman")

print(f"La lsita con elementos es:{Juegos}")

#Ejercicio 4
animales = ["perro", "gato", "conejo", "pez"]

animales[1]="loro"
animales[3]="Oso"

print(f"La lista actualizada es:{animales}")

#Explicacion del ejercicio 5 es que busca el numero mas alto en la lista y con el remove lo saca para mostrar la lista restante 

#Ejercicio 6

Numeros=list(range(10,31,5))

print(f"La lista completa es:{Numeros}")

print(f"Los dos primeros numeros son: {Numeros[:2]}")

#Ejercicio 7 
autos = ["sedan", "polo", "suran", "gol"]

autos[1]="motos"
autos[2]="Barco"

print(f"La lista actualizada:{autos}")

#Ejercicio 8

numeros = []

numeros.append(5*2)
numeros.append(10*2)
numeros.append(15*2)
print(f"La lista de dobles:{numeros}")

#Ejercicio 9

compras=[["Pan","Leche"],["Arroz","Fideos","Salsa"],["Agua"]]

compras[2].append("Jugo")

compras[1][1]="Tallarines"

compras[0].remove("Pan")
print(f"La lista de compras acutalizada: {compras}")

