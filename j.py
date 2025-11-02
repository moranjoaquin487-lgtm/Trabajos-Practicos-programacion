# listas para guardar los datos
titulos = []
ejemplares = []

# programa principal
while True:
    print("\n--- BIBLIOTECA ---")
    print("1. Ingresar titulos")
    print("2. Ingresar ejemplares")
    print("3. Mostrar catalogo")
    print("4. Consultar disponibilidad")
    print("5. Listar agotados")
    print("6. Agregar titulo")
    print("7. Actualizar ejemplares")
    print("8. Salir")
    
    opcion = input("\nElegir opcion: ")
    
    # opcion 1
    if opcion == "1":
        cant = input("Cuantos titulos quiere ingresar? ")
        
        if cant.isdigit():
            cant = int(cant)
            if cant > 0:
                i = 0
                while i < cant:
                    titulo = input("Ingrese titulo: ")
                    titulo = titulo.strip()
                    
                    if titulo == "":
                        print("ERROR: no puede estar vacio")
                    elif titulo in titulos:
                        print("ERROR: ese titulo ya existe")
                    else:
                        titulos.append(titulo)
                        ejemplares.append(0)
                        print("Titulo agregado")
                        i = i + 1
            else:
                print("ERROR: tiene que ser mayor a 0")
        else:
            print("ERROR: ingrese un numero valido")
    
    # opcion 2
    elif opcion == "2":
        if len(titulos) == 0:
            print("No hay titulos, primero agregue titulos")
        else:
            print("\nTitulos:")
            i = 0
            while i < len(titulos):
                print(str(i+1) + ". " + titulos[i] + " (ejemplares: " + str(ejemplares[i]) + ")")
                i = i + 1
            
            num = input("\nElegir numero de titulo: ")
            
            if num.isdigit():
                num = int(num)
                if num >= 1 and num <= len(titulos):
                    cant_ejem = input("Cuantos ejemplares? ")
                    
                    if cant_ejem.isdigit():
                        cant_ejem = int(cant_ejem)
                        if cant_ejem >= 0:
                            ejemplares[num-1] = cant_ejem
                            print("Ejemplares actualizados")
                        else:
                            print("ERROR: no puede ser negativo")
                    else:
                        print("ERROR: ingrese numero valido")
                else:
                    print("ERROR: numero invalido")
            else:
                print("ERROR: ingrese numero valido")
    
    # opcion 3
    elif opcion == "3":
        if len(titulos) == 0:
            print("\nCatalogo vacio")
        else:
            print("\n--- CATALOGO ---")
            i = 0
            while i < len(titulos):
                print(titulos[i] + " - " + str(ejemplares[i]) + " ejemplares")
                i = i + 1
    
    # opcion 4
    elif opcion == "4":
        if len(titulos) == 0:
            print("No hay titulos en el catalogo")
        else:
            buscar = input("Ingrese titulo a buscar: ")
            buscar = buscar.strip()
            
            if buscar == "":
                print("ERROR: no puede estar vacio")
            else:
                encontrado = False
                i = 0
                while i < len(titulos):
                    if titulos[i].lower() == buscar.lower():
                        print("\nTitulo: " + titulos[i])
                        print("Ejemplares: " + str(ejemplares[i]))
                        encontrado = True
                        break
                    i = i + 1
                
                if encontrado == False:
                    print("Titulo no encontrado")
    
    # opcion 5
    elif opcion == "5":
        if len(titulos) == 0:
            print("No hay titulos")
        else:
            hay_agotados = False
            print("\n--- TITULOS AGOTADOS ---")
            i = 0
            while i < len(titulos):
                if ejemplares[i] == 0:
                    print("- " + titulos[i])
                    hay_agotados = True
                i = i + 1
            
            if hay_agotados == False:
                print("No hay titulos agotados")
    
    # opcion 6
    elif opcion == "6":
        titulo_nuevo = input("Ingrese nuevo titulo: ")
        titulo_nuevo = titulo_nuevo.strip()
        
        if titulo_nuevo == "":
            print("ERROR: no puede estar vacio")
        elif titulo_nuevo in titulos:
            print("ERROR: ese titulo ya existe")
        else:
            cant = input("Cuantos ejemplares tiene? ")
            
            if cant.isdigit():
                cant = int(cant)
                if cant >= 0:
                    titulos.append(titulo_nuevo)
                    ejemplares.append(cant)
                    print("Titulo agregado correctamente")
                else:
                    print("ERROR: no puede ser negativo")
            else:
                print("ERROR: ingrese numero valido")
    
    # opcion 7
    elif opcion == "7":
        if len(titulos) == 0:
            print("No hay titulos")
        else:
            print("\nTitulos:")
            i = 0
            while i < len(titulos):
                print(str(i+1) + ". " + titulos[i] + " (" + str(ejemplares[i]) + " ejemplares)")
                i = i + 1
            
            num = input("\nElegir numero: ")
            
            if num.isdigit():
                num = int(num)
                if num >= 1 and num <= len(titulos):
                    print("\nTitulo: " + titulos[num-1])
                    print("Ejemplares actuales: " + str(ejemplares[num-1]))
                    print("\n1. Prestamo")
                    print("2. Devolucion")
                    
                    tipo = input("Elegir: ")
                    
                    if tipo == "1":
                        cant = input("Cuantos prestar? ")
                        
                        if cant.isdigit():
                            cant = int(cant)
                            if cant > 0:
                                if cant > ejemplares[num-1]:
                                    print("ERROR: no hay suficientes ejemplares")
                                else:
                                    ejemplares[num-1] = ejemplares[num-1] - cant
                                    print("Prestamo realizado, quedan " + str(ejemplares[num-1]))
                            else:
                                print("ERROR: tiene que ser mayor a 0")
                        else:
                            print("ERROR: ingrese numero valido")
                    
                    elif tipo == "2":
                        cant = input("Cuantos devolver? ")
                        
                        if cant.isdigit():
                            cant = int(cant)
                            if cant > 0:
                                ejemplares[num-1] = ejemplares[num-1] + cant
                                print("Devolucion realizada, ahora hay " + str(ejemplares[num-1]))
                            else:
                                print("ERROR: tiene que ser mayor a 0")
                        else:
                            print("ERROR: ingrese numero valido")
                    
                    else:
                        print("Opcion invalida")
                else:
                    print("ERROR: numero invalido")
            else:
                print("ERROR: ingrese numero valido")
    
    # opcion 8
    elif opcion == "8":
        print("\nSaliendo del programa...")
        break
    
    else:
        print("Opcion invalida")