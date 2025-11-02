

def crear_archivo_inicial():
    """Crea el archivo productos.txt con tres productos iniciales."""
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        archivo.write("Lapicera,120.5,30\n")
        archivo.write("Cuaderno,250.0,15\n")
        archivo.write("Goma,90.0,40\n")
    print("Archivo inicial creado con éxito.\n")


def leer_productos():
    """Lee el archivo y devuelve una lista de diccionarios con los productos."""
    productos = []
    try:
        with open("productos.txt", "r", encoding="utf-8") as archivo:
            for linea in archivo:
                nombre, precio, cantidad = linea.strip().split(",")
                productos.append({
                    "nombre": nombre,
                    "precio": float(precio),
                    "cantidad": int(cantidad)
                })
        return productos
    except FileNotFoundError:
        print("No se encontró el archivo productos.txt. Crealo primero.")
        return []


def mostrar_productos(productos):
    """Muestra todos los productos en formato legible."""
    if not productos:
        print("No hay productos para mostrar.\n")
    else:
        print("Listado de productos:\n")
        for p in productos:
            print(f"Producto: {p['nombre']} | Precio: ${p['precio']} | Cantidad: {p['cantidad']}")
        print()


def agregar_producto():
    """Permite agregar un producto nuevo al archivo."""
    nombre = input("Ingrese el nombre del nuevo producto: ").strip()
    precio = float(input("Ingrese el precio: "))
    cantidad = int(input("Ingrese la cantidad: "))

    with open("productos.txt", "a", encoding="utf-8") as archivo:
        archivo.write(f"{nombre},{precio},{cantidad}\n")

    print(f"Producto '{nombre}' agregado correctamente.\n")


def buscar_producto(productos):
    """Busca un producto por nombre."""
    nombre_buscar = input("Ingrese el nombre del producto a buscar: ").strip()
    encontrado = False
    for p in productos:
        if p["nombre"].lower() == nombre_buscar.lower():
            print(f"Producto encontrado -> Nombre: {p['nombre']}, Precio: ${p['precio']}, Cantidad: {p['cantidad']}\n")
            encontrado = True
            break
    if not encontrado:
        print("Producto no encontrado.\n")


def guardar_productos(productos):
    """Sobrescribe el archivo con los productos actualizados."""
    with open("productos.txt", "w", encoding="utf-8") as archivo:
        for p in productos:
            archivo.write(f"{p['nombre']},{p['precio']},{p['cantidad']}\n")
    print("Archivo actualizado correctamente.\n")


# -------------------------------
# Programa principal
# -------------------------------
def main():
    print("=== Gestión de productos ===\n")

    # Si no existe el archivo, se puede crear
    opcion = input("¿Desea crear el archivo inicial? (s/n): ").lower()
    if opcion == "s":
        crear_archivo_inicial()

    productos = leer_productos()
    mostrar_productos(productos)

    opcion = input("¿Desea agregar un nuevo producto? (s/n): ").lower()
    if opcion == "s":
        agregar_producto()
        productos = leer_productos()  # recargar lista con el nuevo producto

    opcion = input("¿Desea buscar un producto? (s/n): ").lower()
    if opcion == "s":
        buscar_producto(productos)

    # Guardar los productos actualizados en el archivo
    guardar_productos(productos)
    print("Programa finalizado.\n")


if __name__ == "__main__":
    main()
