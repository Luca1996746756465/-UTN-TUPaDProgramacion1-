#Programa del 0 al 100
for i in range (0,101):
    print(i)

#Programa que solicita un numero entero determina la cantidad de digitos 

num = input("Ingrese un numero: ") 
contador = 0
i = 0

if num[0] == "-":
    i = 1

while i < len(num):
    contador += 1
    i += 1

print(f"El número tiene {contador} dígitos.")


#Suma los números entre 'num' y 'num2', sin incluir los extremos.
num = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

suma = 0

for i in range(num + 1, num2):
    suma += i

print("La suma es:", suma)

# Ejercicio 4: Acumulador con centinela.

suma_total = 0
numero = -1

while numero != 0:
    numero = int(input("Ingrese un número (0 para finalizar): "))
    suma_total = suma_total + numero

print("El total acumulado es:", suma_total)

# Ejercicio 5: Juego de adivinanza (Bucle indeterminado).
import random

secreto = random.randint(0, 9)
intentos = 0
propuesta = -1

while propuesta != secreto:
    propuesta = int(input("Adivina (0-9): "))
    intentos += 1

print(f"Acertaste en {intentos} intentos")


# Ejercicio 6: Secuencia descendente par.
for i in range(100, -1, -2):
    print(i)

# Ejercicio 7: Sumatoria de los primeros 'n' números.
n = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(n + 1):
    suma += i

print(f"La suma total de 0 hasta {n} es: {suma}")


# Ejercicio 8: Clasificación de datos (100 iteraciones).
CANTIDAD = 100 
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(CANTIDAD):
    num = int(input(f"({i+1}/{CANTIDAD}) Ingrese un número: "))
    

    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
        
    if num >= 0:
        positivos += 1
    else:
        negativos += 1

print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")

# Ejercicio 9: Cálculo de media aritmética.
CANTIDAD = 100
suma = 0

for i in range(CANTIDAD):
    num = int(input(f"({i+1}/{CANTIDAD}) Ingrese un número: "))
    suma += num

media = suma / CANTIDAD
print(f"La media de los {CANTIDAD} números es: {media}")

#Punto 10 Programa para invertir los numeros

numero = int(input("Ingrese un número entero: "))
invertido = 0

while numero > 0:
    ultimo_digito = numero % 10
    invertido = (invertido * 10) + ultimo_digito
    numero = numero // 10

print(f"El número invertido es: {invertido}")


