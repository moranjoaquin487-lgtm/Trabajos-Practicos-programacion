#1
for i in range(101):
    print(i)

#2
numero = int(input("Ingrese un número entero: "))
cantidad_digitos = len(str(abs(numero)))
print(f"El número tiene {cantidad_digitos} dígitos")

#3
valor1 = int(input("Ingrese el primer valor: "))
valor2 = int(input("Ingrese el segundo valor: "))

if valor1 > valor2:
    valor1, valor2 = valor2, valor1

suma = 0
for i in range(valor1 + 1, valor2):
    suma += i

print(f"La suma de los números entre {valor1} y {valor2} es: {suma}")

#4
suma_total = 0
numero = int(input("Ingrese un número (0 para terminar): "))

while numero != 0:
    suma_total += numero
    numero = int(input("Ingrese un número (0 para terminar): "))

print(f"La suma total es: {suma_total}")

#5
import random

numero_secreto = random.randint(0, 9)
intentos = 0
adivinado = False

print("¡Adivina el número entre 0 y 9!")

while not adivinado:
    intento = int(input("Ingresa tu número: "))
    intentos += 1
    
    if intento == numero_secreto:
        adivinado = True
        print(f"¡Felicitaciones! Adivinaste en {intentos} intentos")
    elif intento < numero_secreto:
        print("El número es mayor")
    else:
        print("El número es menor")

#6
for i in range(100, -1, -2):
    print(i)

#7
numero = int(input("Ingrese un número entero positivo: "))

if numero < 0:
    print("El número debe ser positivo")
else:
    suma = 0
    for i in range(numero + 1):
        suma += i
    print(f"La suma de 0 a {numero} es: {suma}")

#8
CANTIDAD = 100  

pares = 0
impares = 0
positivos = 0
negativos = 0

for i in range(CANTIDAD):
    numero = int(input(f"Ingrese el número {i+1}: "))
    
    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1
    
    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print(f"\nResultados:")
print(f"Números pares: {pares}")
print(f"Números impares: {impares}")
print(f"Números positivos: {positivos}")
print(f"Números negativos: {negativos}")

#9
CANTIDAD = 100  

suma = 0

for i in range(CANTIDAD):
    numero = int(input(f"Ingrese el número {i+1}: "))
    suma += numero

media = suma / CANTIDAD
print(f"La media de los {CANTIDAD} números es: {media:.2f}")

#10
numero = int(input("Ingrese un número entero: "))

signo = -1 if numero < 0 else 1
numero = abs(numero)

numero_invertido = 0
while numero > 0:
    digito = numero % 10
    numero_invertido = numero_invertido * 10 + digito
    numero = numero // 10

numero_invertido *= signo
print(f"El número invertido es: {numero_invertido}")
