# ==========================================
# TRABAJO PRÁCTICO 4: ESTRUCTURAS REPETITIVAS
# ==========================================

# Ejercicio 1: Secuencia de 0 a 100 en orden creciente.
# Se utiliza range(0, 101) para incluir el número 100 en el bucle.
for i in range(0, 101):
    print(i)


# Ejercicio 2: Contador de dígitos de un número entero.
# Se solicita el número como string para evaluar el signo negativo si existiera
# y contar iterativamente sus caracteres numéricos.
num = input("Ingrese un número entero: ") 
contador = 0
i = 0

# Si tiene signo negativo, omitimos el primer carácter para no contarlo como dígito
if num[0] == "-":
    i = 1

while i < len(num):
    contador += 1
    i += 1

print(f"El número tiene {contador} dígitos.")


# Ejercicio 3: Suma de enteros entre dos valores excluyendo extremos.
# Se utiliza un rango que inicia en (num + 1) y termina antes de num2.
num = int(input("Primer número: "))
num2 = int(input("Segundo número: "))

suma = 0
for i in range(num + 1, num2):
    suma += i

print("La suma es:", suma)


# Ejercicio 4: Acumulador con valor centinela (0).
# Se utiliza un ciclo while indeterminado que acumula los ingresos hasta que se digita 0.
suma_total = 0
numero = -1

while numero != 0:
    numero = int(input("Ingrese un número (0 para finalizar): "))
    suma_total += numero

print("El total acumulado es:", suma_total)


# Ejercicio 5: Juego de adivinanza.
# Genera un número aleatorio entre 0 y 9 y evalúa los intentos requeridos.
import random

secreto = random.randint(0, 9)
intentos = 0
propuesta = -1

while propuesta != secreto:
    propuesta = int(input("Adivina el número (0-9): "))
    intentos += 1

print(f"¡Acertaste! Necesitaste {intentos} intentos.")


# Ejercicio 6: Secuencia descendente de números pares de 100 a 0.
# El paso -2 en range() decrementa de a dos unidades por iteración.
for i in range(100, -1, -2):
    print(i)


# Ejercicio 7: Sumatoria de 0 hasta un entero positivo n.
n = int(input("Ingrese un número entero positivo: "))
suma = 0

for i in range(n + 1):
    suma += i

print(f"La suma total de 0 hasta {n} es: {suma}")


# Ejercicio 8: Clasificación de 100 números (pares, impares, positivos, negativos).
# Modificando la variable constante CANTIDAD se puede adaptar la escala del proceso.
CANTIDAD = 100 
pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(CANTIDAD):
    num = int(input(f"({i+1}/{CANTIDAD}) Ingrese un número: "))
    
    # Evaluación de paridad mediante el operador módulo %
    if num % 2 == 0:
        pares += 1
    else:
        impares += 1
        
    # Evaluación de signo
    if num >= 0:
        positivos += 1
    else:
        negativos += 1

print(f"Pares: {pares}, Impares: {impares}, Positivos: {positivos}, Negativos: {negativos}")


# Ejercicio 9: Cálculo de media aritmética sobre 100 valores.
CANTIDAD = 100
suma = 0

for i in range(CANTIDAD):
    num = int(input(f"({i+1}/{CANTIDAD}) Ingrese un número: "))
    suma += num

media = suma / CANTIDAD
print(f"La media de los {CANTIDAD} números es: {media}")


# Ejercicio 10: Inversión de dígitos mediante operaciones aritméticas.
# Se extrae el último dígito con el módulo (% 10) y se desplaza el resultado con (// 10).
numero = int(input("Ingrese un número entero positivo: "))
invertido = 0

while numero > 0:
    ultimo_digito = numero % 10
    invertido = (invertido * 10) + ultimo_digito
    numero = numero // 10

print(f"El número invertido es: {invertido}")