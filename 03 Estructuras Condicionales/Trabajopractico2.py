# Ejercicio 1 - Mayor de edad
Edad= int(input("Ingrese su edad"))

if Edad >= 18:
    print("Eres mayor de edad")
else:
    print("Sos menor todavia")

# Ejercicio 2 - Nota aprobada o desaprobada
Calificacion= int(input("¿Que calificacion obtuvo?"))

if Calificacion >= 6:
    print("Aprobaste")
else:
    print("Desaprobaste")


# Ejercicio 3 - Número par 

numero = int(input("Ingrese un número par: "))

while numero % 2 != 0:
    print("Por favor, ingrese un número par")
    numero = int(input("Ingrese un número par: "))

print("Ha ingresado un número par")

# Ejercicio 4 - Categoría por edad
edad = int(input("Ingresa tu edad: "))

if edad < 12:
    print("Niño/a")
elif edad >= 12 and edad < 18:
    print("Adolescente")
elif edad >= 18 and edad < 30:
    print("Adulto/a joven")
else:
    print("Adulto/a")

# Ejercicio 5 - Validar contraseña
contraseña = input("Ingresa una contraseña: ")

while len(contraseña) < 8 or len(contraseña) > 14:
    print("Por favor, ingrese una contraseña de entre 8 y 14 caracteres")
    contraseña = input("Ingresa una contraseña: ")

print("Ha ingresado una contraseña correcta")




# Ejercicio 6 - Media, mediana y moda
from statistics import mode, median, mean
import random

numeros_aleatorios = [random.randint(1, 100) for i in range(50)]

moda = mode(numeros_aleatorios)
mediana = median(numeros_aleatorios)
media = mean(numeros_aleatorios)

print("Moda:", moda)
print("Mediana:", mediana)
print("Media:", media)

if media > mediana and mediana > moda:
    print("Sesgo positivo")
elif media < mediana and mediana < moda:
    print("Sesgo negativo")
else:
    print("Sin sesgo")


# Ejercicio 7 - Frase que termina en vocal
frase = input("Ingresa una frase o palabra: ")

if frase[-1] == "a" or frase[-1] == "e" or frase[-1] == "i" or frase[-1] == "o" or frase[-1] == "u":
    print(frase + "!")
else:
    print(frase)


# Ejercicio 8 - Formato del nombre
nombre = input("Ingresa tu nombre: ")
opcion = int(input("Elige una opción (1, 2 o 3): "))

if opcion == 1:
    print(nombre.upper())
elif opcion == 2:
    print(nombre.lower())
elif opcion == 3:
    print(nombre.title())
else:
    print("Opción inválida")

# Ejercicio 9 - Escala de Richter

magnitud = float(input("Ingresa la magnitud del terremoto: "))

if magnitud < 3:
    print("Muy leve")
elif magnitud >= 3 and magnitud < 4:
    print("Leve")
elif magnitud >= 4 and magnitud < 5:
    print("Moderado")
elif magnitud >= 5 and magnitud < 6:
    print("Fuerte")
elif magnitud >= 6 and magnitud < 7:
    print("Muy Fuerte")
else:
    print("Extremo")

# Ejercicio 10 - Estaciones del año

hemisferio = input("Ingresa hemisferio (N/S): ")
mes = int(input("Ingresa el mes: "))
dia = int(input("Ingresa el día: "))

if (mes == 12 and dia >= 21) or (mes <= 3 and (mes < 3 or dia <= 20)):
    if hemisferio == "N":
        print("Invierno")
    else:
        print("Verano")

elif (mes == 3 and dia >= 21) or (mes <= 6 and (mes < 6 or dia <= 20)):
    if hemisferio == "N":
        print("Primavera")
    else:
        print("Otoño")

elif (mes == 6 and dia >= 21) or (mes <= 9 and (mes < 9 or dia <= 20)):
    if hemisferio == "N":
        print("Verano")
    else:
        print("Invierno")

else:
    if hemisferio == "N":
        print("Otoño")
    else:
        print("Primavera")