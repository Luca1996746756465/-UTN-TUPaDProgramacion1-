# Crear un programa que imprima por pantalla el mensaje: “Hola Mundo!”. 
print("Hola Mundo!")
#Crear un programa que pida al usuario su nombre e imprima por pantalla un saludo usando el nombre ingresado.
Nombre = input("¿Cómo te llamas? ")
print("Hola",Nombre)
# 3) Crear un programa que pida al usuario su nombre, apellido, edad y lugar de residencia e imprima por pantalla una oración con los datos ingresados.
Nombre= input("Como te llamas")
Apellido=input("Cual es tu apellido")
Edad= input("Cuantos años tienes")
Residencia= input ("Donde vivis")
print("Soy",Nombre,Apellido, "mi edad es", Edad, "y vivo en ", Residencia)
#Crear un programa que pida al usuario el radio de un círculo e imprima por pantalla su área y su perímetro. 
Radio = int(input("¿Cuál es el radio? "))
Area = 3.14 * Radio**2
Perimetro = 2 * 3.14 * Radio
print("El área es:",Area)
print("El perímetro es:",Perimetro)
#5) Crear un programa que pida al usuario una cantidad de segundos e imprima por pantalla a cuántas horas equivale. 
Segundos = int(input("¿Cuantos segundos quiere agregar? "))
Horas= Segundos / 3600
print("Es quivalente a" ,(Horas),"Horas")
#6) Crear un programa que pida al usuario un número e imprima por pantalla la tabla de multiplicar de dicho número. 
numero = int(input("Ingrese un número: "))

print(numero, "x 1 =", numero * 1)
print(numero, "x 2 =", numero * 2)
print(numero, "x 3 =", numero * 3)
print(numero, "x 4 =", numero * 4)
print(numero, "x 5 =", numero * 5)
print(numero, "x 6 =", numero * 6)
print(numero, "x 7 =", numero * 7)
print(numero, "x 8 =", numero * 8)
print(numero, "x 9 =", numero * 9)
print(numero, "x 10 =", numero * 10)
#7) Crear un programa que pida al usuario dos números enteros distintos del 0 y muestre por pantalla el resultado de sumarlos, dividirlos, multiplicarlos y restarlos. 
numero1=int(input("Ingresa un numero"))
numero2=int(input("Ingresa un numero"))
Suma= numero1+numero2
Resta= numero1-numero2
Multiplicacion= numero1*numero2
Division= numero1//numero2
print("La suma es:",Suma,"La resta es:",Resta,"La multiplicacion es:",Multiplicacion,"y la division es:",Division)
#8) Crear un programa que pida al usuario su altura y su peso e imprima por pantalla su índice de masa corporal. Tener en cuenta que el índice de masa corporal se calcula del siguiente modo: 
peso = float(input("Ingrese su peso en kg: "))
altura = float(input("Ingrese su altura en metros: "))
imc = peso / (altura ** 2)
print("Su IMC es:", imc)
#9) Crear un programa que pida al usuario una temperatura en grados Celsius e imprima por pantalla su equivalente en grados Fahrenheit. Tener en cuenta la siguiente equivalencia: 
celsius = float(input("Ingrese la temperatura en Celsius: "))
fahrenheit = (9/5) * celsius + 32
print("La temperatura en Fahrenheit es:", fahrenheit)
#10) Crear un programa que pida al usuario 3 números e imprima por pantalla el promedio de dichos números. 
numero1 = int(input("Ingrese el primer numero "))
numero2 = int(input("Ingrese el segundo numero "))
numero3 = int(input("Ingrese el tercer numero "))
promedio= (numero1+numero2+numero3) / 3
print ("El promedio es de ",promedio)