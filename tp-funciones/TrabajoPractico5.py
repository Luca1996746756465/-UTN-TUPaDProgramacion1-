import math

# ==============================================================================
# Consigna 1: Crear una función llamada imprimir_hola_mundo que imprima por 
# pantalla el mensaje: “Hola Mundo!”. Llamar a esta función desde el programa principal.
# ==============================================================================
# Explicación: Definimos una función simple sin parámetros que ejecuta un print. 
# Luego la invocamos desde el programa principal para ejecutarla.
def hola_mundo():
    print("Hola Mundo")

hola_mundo()


# ==============================================================================
# Consigna 2: Crear una función llamada saludar_usuario(nombre) que reciba como 
# parámetro un nombre y devuelva un saludo personalizado. Por ejemplo, si se llama 
# con saludar_usuario("Marcos"), deberá devolver: “Hola Marcos!”. Llamar a esta 
# función desde el programa principal solicitando el nombre al usuario.
# ==============================================================================
# Explicación: Recibe variables por parámetro (nombre y edad) y las usa para 
# formatear un texto personalizado mediante f-strings.
def saludar_usuario(nombre, edad):
    print(f"Hola {nombre}, tiene {edad} años")

nombre_usuario = input("Ingrese su nombre: ")
edad_usuario = int(input("Ingrese su edad: "))

saludar_usuario(nombre_usuario, edad_usuario)


# ==============================================================================
# Consigna 3: Crear una función llamada informacion_personal(nombre, apellido, 
# edad, residencia) que reciba cuatro parámetros e imprima: “Soy [nombre] [apellido], 
# tengo [edad] años y vivo en [residencia]”. Pedir los datos al usuario y llamar 
# a esta función con los valores ingresados.
# ==============================================================================
# Explicación: Muestra cómo pasar múltiples argumentos (4 parámetros) a una función 
# para procesar e imprimir un conjunto completo de datos personales.
def saludar_usuario(nombre, apellido, edad, residencia):
    print(f"Hola {nombre} {apellido}, tiene {edad} años y vives en {residencia}")

nombre_usuario = input("Ingrese su nombre: ")
appellido_usuario = input("Ingrese su apellido: ")
edad_usuario = int(input("Ingrese su edad: "))
residencia_usuario = input("Ingrese su residencia: ")

saludar_usuario(nombre_usuario, appellido_usuario, edad_usuario, residencia_usuario)


# ==============================================================================
# Consigna 4: Crear dos funciones: calcular_area_circulo(radio) que reciba el radio 
# como parámetro y devuelva el área del círculo. calcular_perimetro_circulo(radio) 
# que reciba el radio como parámetro y devuelva el perímetro del círculo. Solicitar 
# el radio al usuario y llamar ambas funciones para mostrar los resultados.
# ==============================================================================
# Explicación: Importa la librería math para obtener el valor preciso de pi (math.pi). 
# Las funciones devuelven el resultado con 'return' y se formatea la salida a 2 decimales (:.2f).
def calcular_area_circulo(radio):
    return math.pi * (radio**2)

def calcular_perimetro_circulo(radio):
    return 2 * math.pi * radio

radio_ingresado = float(input("Ingrese el numero del radio: "))

area = calcular_area_circulo(radio_ingresado)
perimetro = calcular_perimetro_circulo(radio_ingresado)

print(f"El área del círculo es: {area:.2f}")
print(f"El perimetro del círculo es: {perimetro:.2f}")


# ==============================================================================
# Consigna 5: Crear una función llamada segundos_a_horas(segundos) que reciba una 
# cantidad de segundos como parámetro y devuelva la cantidad de horas correspondientes. 
# Solicitar al usuario los segundos y mostrar el resultado usando esta función.
# ==============================================================================
# Explicación: Realiza una conversión matemática básica dividiendo los segundos 
# ingresados entre 3600 (cantidad de segundos en una hora) y retorna la cifra final.
def segundos_a_horas(segundos):
    return segundos / 3600

segundos_ingresados = float(input("Ingresá la cantidad de segundos: "))
horas = segundos_a_horas(segundos_ingresados)

print(f"{segundos_ingresados} segundos equivalen a {horas:.2f} horas.\n")


# ==============================================================================
# Consigna 6: Crear una función llamada tabla_multiplicar(numero) que reciba un 
# número como parámetro e imprima la tabla de multiplicar de ese número del 1 al 10. 
# Pedir al usuario el número y llamar a la función.
# ==============================================================================
# Explicación: Emplea un bucle 'for' junto a range(1, 11) para iterar del 1 al 10, 
# multiplicando en cada vuelta el parámetro recibido por la variable del contador.
def tabla_de_multiplicar(numero):
    print(f"Tabla de multiplicar del {numero}")
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero*i}")

num_tabla = int(input("Ingrese un numero para multiplicar: "))
tabla_de_multiplicar(num_tabla)
print()


# ==============================================================================
# Consigna 7: Crear una función llamada operaciones_basicas(a, b) que reciba dos 
# números como parámetros y devuelva una tupla con el resultado de sumarlos, 
# restarlos, multiplicarlos y dividirlos. Mostrar los resultados de forma clara.
# ==============================================================================
# Explicación: Calcula las 4 operaciones aritméticas fundamentales e incluye una 
# condición de seguridad (if b != 0) para evitar colapsos por división entre cero. 
# Devuelve múltiples valores empaquetados dentro de una tupla.
def operaciones_basicas(a, b):
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    if b != 0:
        division = a / b
    else:
        print("No se puede dividir por 0")
        division = None
    return (suma, resta, multiplicacion, division)

numero1 = int(input("Ingrese el primer numero: "))
numero2 = int(input("Ingrese el numero dos: "))

s, r, m, d = operaciones_basicas(numero1, numero2)

print(f"La suma de los dos numeros es: {s}")
print(f"El resultado de la resta de los dos numeros es: {r}")
print(f"La multiplicacion de los dos numeros es: {m}")
print(f"El resultado de la division de los dos numeros es: {d}")


# ==============================================================================
# Consigna 8: Crear una función llamada calcular_imc(peso, altura) que reciba el 
# peso en kilogramos y la altura en metros, y devuelva el índice de masa corporal (IMC). 
# Solicitar al usuario los datos y llamar a la función para mostrar el resultado con dos decimales.
# ==============================================================================
# Explicación: Aplica la fórmula del Índice de Masa Corporal (peso / altura^2) 
# haciendo uso del operador potencia (**).
def calcular_imc(peso, altura):
    return peso / (altura**2)

peso_usuario = float(input("Ingrese su peso: "))
altura_usuario = float(input("Ingrese su altura: "))

imc = calcular_imc(peso_usuario, altura_usuario)

print(f"Tu indice de masa muscular es: {imc:.2f}")


# ==============================================================================
# Consigna 9: Crear una función llamada celsius_a_fahrenheit(celsius) que reciba 
# una temperatura en grados Celsius y devuelva su equivalente en Fahrenheit. 
# Pedir al usuario la temperatura en Celsius y mostrar el resultado usando la función.
# ==============================================================================
# Explicación: Toma un valor de temperatura decimal y realiza la fórmula de 
# conversión estándar ((Celsius * 9/5) + 32) devolviendo la equivalencia.
def celsius_a_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32

temp_celsius = float(input("Ingrese la temperatura en grados celsius: "))
temp_fahrenheit = celsius_a_fahrenheit(temp_celsius)

print(f"{temp_celsius}°C es equivalente a {temp_fahrenheit:.2f}°F")


# ==============================================================================
# Consigna 10: Crear una función llamada calcular_promedio(a, b, c) que reciba 
# tres números como parámetros y devuelva el promedio de ellos. Solicitar los 
# números al usuario y mostrar el resultado usando esta función.
# ==============================================================================
# Explicación: Suma los tres parámetros numéricos encerrados en paréntesis para 
# dar prioridad matemática a la suma y luego los divide por la cantidad total (3).
def promedio_estudiante(a, b, c):
    return (a + b + c) / 3

nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

promedio = promedio_estudiante(nota1, nota2, nota3)

print(f"El promedio final es: {promedio:.2f}")