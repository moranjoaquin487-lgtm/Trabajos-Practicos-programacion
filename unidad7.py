# 1)
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}
precios_frutas.update({'Naranja': 1200, 'Manzana': 1500, 'Pera': 2300})
print("1) Diccionario con nuevas frutas:", precios_frutas)

# 2)
precios_frutas.update({'Banana': 1330, 'Manzana': 1700, 'Melón': 2800})
print("2) Diccionario con precios actualizados:", precios_frutas)

# 3)
frutas = list(precios_frutas.keys())
print("3) Lista de frutas:", frutas)

# 4)
agenda = {}
for i in range(5):
    nombre = input(f"Ingrese el nombre del contacto {i+1}: ")
    numero = input(f"Ingrese el número de {nombre}: ")
    agenda[nombre] = numero

consulta = input("Ingrese el nombre para consultar su número: ")
if consulta in agenda:
    print(f"El número de {consulta} es {agenda[consulta]}")
else:
    print("Contacto no encontrado.")

# 5)
frase = input("Ingrese una frase: ").lower().split()
palabras_unicas = set(frase)
conteo = {palabra: frase.count(palabra) for palabra in palabras_unicas}
print("Palabras únicas:", palabras_unicas)
print("Conteo de palabras:", conteo)

# 6)
alumnos = {}
for i in range(3):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    notas = tuple(float(input(f"Ingrese la nota {j+1} de {nombre}: ")) for j in range(3))
    alumnos[nombre] = notas

for alumno, notas in alumnos.items():
    promedio = sum(notas) / len(notas)
    print(f"El promedio de {alumno} es {promedio:.2f}")

# 7)
parcial1 = {int(x) for x in input("Ingrese legajos que aprobaron el Parcial 1 separados por espacios: ").split()}
parcial2 = {int(x) for x in input("Ingrese legajos que aprobaron el Parcial 2 separados por espacios: ").split()}

print("Aprobaron ambos parciales:", parcial1 & parcial2)
print("Aprobaron solo uno:", parcial1 ^ parcial2)
print("Aprobaron al menos uno:", parcial1 | parcial2)

# 8)
productos = {}
while True:
    opcion = input("\n1- Consultar stock\n2- Agregar unidades\n3- Agregar producto nuevo\n4- Salir\nElija una opción: ")
    if opcion == '1':
        prod = input("Ingrese producto a consultar: ")
        print(f"Stock de {prod}: {productos.get(prod, 'No existe')}")
    elif opcion == '2':
        prod = input("Producto: ")
        if prod in productos:
            cant = int(input("Cantidad a agregar: "))
            productos[prod] += cant
            print(f"Nuevo stock de {prod}: {productos[prod]}")
        else:
            print("El producto no existe.")
    elif opcion == '3':
        prod = input("Nuevo producto: ")
        cant = int(input("Cantidad inicial: "))
        productos[prod] = cant
        print("Producto agregado.")
    elif opcion == '4':
        break
    else:
        print("Opción inválida.")

# 9)
agenda_eventos = {}
for i in range(3):
    dia = input("Ingrese día: ")
    hora = input("Ingrese hora: ")
    evento = input("Ingrese evento: ")
    agenda_eventos[(dia, hora)] = evento

consulta_dia = input("Día a consultar: ")
consulta_hora = input("Hora a consultar: ")
print("Evento:", agenda_eventos.get((consulta_dia, consulta_hora), "No hay evento."))

# 10)
paises = {'Argentina': 'Buenos Aires', 'Chile': 'Santiago', 'Uruguay': 'Montevideo'}
invertido = {capital: pais for pais, capital in paises.items()}
print("Diccionario invertido:", invertido)
