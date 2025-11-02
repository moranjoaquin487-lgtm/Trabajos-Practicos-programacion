
import math


def imprimir_hola_mundo():
    """Imprime 'Hola Mundo!' en pantalla."""
    print("Hola Mundo!")


def saludar_usuario(nombre: str) -> str:
    """Recibe un nombre y devuelve un saludo personalizado.

    Ejemplo:
        saludar_usuario('Marcos') -> 'Hola Marcos!'
    """
    return f"Hola {nombre}!"


def informacion_personal(nombre: str, apellido: str, edad: int, residencia: str) -> None:
    """Imprime la información personal formateada."""
    print(f"Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.")


def calcular_area_circulo(radio: float) -> float:
    """Devuelve el área de un círculo dado su radio."""
    return math.pi * radio * radio


def calcular_perimetro_circulo(radio: float) -> float:
    """Devuelve el perímetro (circunferencia) de un círculo dado su radio."""
    return 2 * math.pi * radio


def segundos_a_horas(segundos: float) -> float:
    """Convierte segundos a horas (puede devolver fracción de horas)."""
    return segundos / 3600.0


def tabla_multiplicar(numero: int) -> None:
    """Imprime la tabla de multiplicar del número del 1 al 10."""
    for i in range(1, 11):
        print(f"{numero} x {i} = {numero * i}")


def operaciones_basicas(a: float, b: float):
    """Devuelve una tupla con (suma, resta, multiplicacion, division).

    Si la división no es posible (división por 0) devuelve None en lugar del cociente.
    """
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    try:
        division = a / b
    except ZeroDivisionError:
        division = None
    return (suma, resta, multiplicacion, division)


def calcular_imc(peso: float, altura: float) -> float:
    """Calcula el IMC = peso(kg) / altura(m)^2. Devuelve float."""
    if altura <= 0:
        raise ValueError("La altura debe ser mayor que 0")
    return peso / (altura * altura)


def celsius_a_fahrenheit(celsius: float) -> float:
    """Convierte Celsius a Fahrenheit."""
    return (celsius * 9.0 / 5.0) + 32.0


def calcular_promedio(a: float, b: float, c: float) -> float:
    """Devuelve el promedio aritmético de tres números."""
    return (a + b + c) / 3.0


# -----------------------------
# Funciones para interactuar con el usuario
# -----------------------------

def pedir_float(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Entrada inválida. Ingrese un número.")


def pedir_int(prompt: str) -> int:
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Entrada inválida. Ingrese un número entero.")


# Menú para ejecutar las actividades
def menu():
    while True:
        print("\n--- Menú de actividades (Funciones) ---")
        print("1. Imprimir 'Hola Mundo'")
        print("2. Saludar usuario")
        print("3. Información personal")
        print("4. Área y perímetro de un círculo")
        print("5. Segundos a horas")
        print("6. Tabla de multiplicar")
        print("7. Operaciones básicas")
        print("8. Calcular IMC")
        print("9. Celsius a Fahrenheit")
        print("10. Calcular promedio")
        print("0. Salir")

        opcion = input("Elija una opción: ")

        if opcion == '1':
            imprimir_hola_mundo()

        elif opcion == '2':
            nombre = input("Ingrese su nombre: ")
            print(saludar_usuario(nombre))

        elif opcion == '3':
            nombre = input("Nombre: ")
            apellido = input("Apellido: ")
            edad = pedir_int("Edad: ")
            residencia = input("Residencia: ")
            informacion_personal(nombre, apellido, edad, residencia)

        elif opcion == '4':
            radio = pedir_float("Ingrese el radio del círculo: ")
            area = calcular_area_circulo(radio)
            perimetro = calcular_perimetro_circulo(radio)
            print(f"Área: {area:.4f}")
            print(f"Perímetro: {perimetro:.4f}")

        elif opcion == '5':
            segundos = pedir_float("Ingrese la cantidad de segundos: ")
            horas = segundos_a_horas(segundos)
            print(f"Equivalente en horas: {horas:.6f} h")

        elif opcion == '6':
            numero = pedir_int("Ingrese el número para la tabla: ")
            tabla_multiplicar(numero)

        elif opcion == '7':
            a = pedir_float("Ingrese a: ")
            b = pedir_float("Ingrese b: ")
            suma, resta, mult, div = operaciones_basicas(a, b)
            print(f"Suma: {suma}")
            print(f"Resta: {resta}")
            print(f"Multiplicación: {mult}")
            if div is None:
                print("División: No se puede dividir por 0")
            else:
                print(f"División: {div}")

        elif opcion == '8':
            peso = pedir_float("Ingrese su peso en kg: ")
            altura = pedir_float("Ingrese su altura en metros: ")
            try:
                imc = calcular_imc(peso, altura)
                print(f"IMC: {imc:.2f}")
            except ValueError as e:
                print(e)

        elif opcion == '9':
            c = pedir_float("Ingrese la temperatura en °C: ")
            f = celsius_a_fahrenheit(c)
            print(f"{c} °C = {f:.2f} °F")

        elif opcion == '10':
            a = pedir_float("Ingrese el primer número: ")
            b = pedir_float("Ingrese el segundo número: ")
            c = pedir_float("Ingrese el tercer número: ")
            prom = calcular_promedio(a, b, c)
            print(f"Promedio: {prom:.4f}")

        elif opcion == '0':
            print("Saliendo. ¡Hasta luego!")
            break

        else:
            print("Opción no válida. Intente nuevamente.")


if __name__ == '__main__':
    menu()
