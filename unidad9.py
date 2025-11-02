def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

num = int(input())
for i in range(1, num + 1):
    print(factorial(i))


def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

pos = int(input())
for i in range(pos):
    print(fibonacci(i), end=" ")
print()


def potencia(base, exponente):
    if exponente == 0:
        return 1
    return base * potencia(base, exponente - 1)

b = int(input())
e = int(input())
print(potencia(b, e))


def decimal_a_binario(n):
    if n == 0:
        return ""
    return decimal_a_binario(n // 2) + str(n % 2)

n = int(input())
binario = decimal_a_binario(n)
print(binario or "0")


def es_palindromo(palabra):
    if len(palabra) <= 1:
        return True
    if palabra[0] != palabra[-1]:
        return False
    return es_palindromo(palabra[1:-1])

texto = input().lower()
print(es_palindromo(texto))


def suma_digitos(n):
    if n < 10:
        return n
    return n % 10 + suma_digitos(n // 10)

n = int(input())
print(suma_digitos(n))


def contar_bloques(n):
    if n == 1:
        return 1
    return n + contar_bloques(n - 1)

niveles = int(input())
print(contar_bloques(niveles))


def contar_digito(numero, digito):
    if numero == 0:
        return 0
    return (1 if numero % 10 == digito else 0) + contar_digito(numero // 10, digito)

numero = int(input())
dig = int(input())
print(contar_digito(numero, dig))
