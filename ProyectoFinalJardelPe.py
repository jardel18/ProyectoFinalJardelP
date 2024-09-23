import datetime
import random 
reservar_viajes = {}
reservas = []
vuelos_registrados = []
paquetesPredeterminados = {
    1: {
        "destino": "Cartagena",
        "duracion": 5,
        "alojamiento": "Hotel 5 estrellas",
        "actividades": ["Visitar el Castillo de San Felipe", "Recorrer la ciudad amurallada", "Disfrutar de las playas"],
        "precio": 2000000},
    2: {
        "destino": "Medellín",
        "duracion": 3,
        "alojamiento": "Apartamento",
        "actividades": ["Conocer la Comuna 13", "Visitar el Parque Explora", "Hacer un tour por Guatapé"],
        "precio": 1500000}
}
def menu_principal():
    print("\n*** Menu Principal ***")
    print("1. Reservas de Paquetes Turísticos")
    print("2. Reservas de Vuelos")
    print("3. Salir")
    print("\n***********************")
def menuDePaquetes():
    print("\n*** Menu de opciones*** ")
    print("1. Reserva Paquete Turistico ")
    print("2. Actualizar Paquete Turistico ")
    print("3. consultar paquete turistico ")
    print("4. Eliminar Paquete Turistico ")
    print("5. Salir")
    print("\n*********************** ")
def menuDeVuelos():
    print("\n*** Menu de opciones*** ")
    print("1. Registrar vuelos ")
    print("2. Actualizar vuelo ")
    print("3. Consultar vuelos ")
    print("4. Cancelar vuelos ")
    print("5. Salir")
    print("\n*********************** ")

def validarNombre(nombre):
    #Valida que lo que se escriba son letras, no se registra espacios en blancos, ni puntos, ni numero, solo palabras
    if nombre.isalpha():
        return True
    else:
        return False
def validarapellidos(apellidos):
    #Valida que los apellidos solo contengan letras y espacios.
    if apellidos.isalpha():
        return True
    else:
        return False
def validarfecha(fechaNacimiento):
    #Valida que la fecha tenga el formato DD/MM/AAAA y sea válida.
    try:
        fechaNacimiento = datetime.datetime.strptime(fechaNacimiento, "%d/%m/%Y").date()
        return  fechaNacimiento
    except ValueError:
        return False
def generar_id_a_partir_de_fecha(fecha_nacimiento):
    complementos = fecha_nacimiento.split ('/')
    fecha = int(complementos[0])*1000 + int(complementos[1])*100 +int(complementos[2])
    idAleatorio = random.randint (1000,9999)
    idGenerado = str (fecha) + str (idAleatorio)
    return idGenerado
def validar_fechas(fecha_salida, fecha_regreso):
    try:
        fecha_salida = datetime.datetime.strptime(fecha_salida, "%d/%m/%Y").date()
        fecha_regreso = datetime.datetime.strptime(fecha_regreso, "%d/%m/%Y").date()
        return fecha_regreso> fecha_salida
    except ValueError:
        return False
def reservar_viaje():
    # Datos del cliente
    while True:
        nombre = input("Ingrese su nombre: ")
        if validarNombre (nombre):
            break
        else:
            print("Por favor ingrese solo palabras")
    while True:        
        apellidos = input("Ingrese su apellido: ")
        if validarapellidos(apellidos):
            break
        else:
            print("Por favor ingrese solo palabras")
    while True:
        fechaNacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
        if validarfecha(fechaNacimiento):
            break
        else:
            print(" Fecha de nacimiento invalida. Por favor, usar el formato indicado ")
    fecha = (fechaNacimiento)
    idUnico = generar_id_a_partir_de_fecha(fecha)
    reserva = {"nombre":nombre, "apellido":apellidos,"fecha de nacimiento":fechaNacimiento,"id":idUnico}
    reservas.append(reserva)
    print(f"Usuario {nombre} {apellidos} con ID {idUnico} registrado Exitosamente ")
    print(reservas)   
    # Destino
    destinos = ["Santa Marta", "Cartagena", "Desierto del Tatacoa", "Valle del Cocora",]
    print("Destinos disponibles:")
    for i, destino in enumerate(destinos):
        print(f"{i+1}. {destino}")
    while True:
        try:
            destinoElegido = int(input("Ingrese el numero del destino: ")) - 1
            if 0 <= destinoElegido < len(destinos):
                break
            else:
                print("Opcion Invalida. Por favor, Ingrese un numero del 1 al",len(destinos))
        except ValueError:
            print("Debe ingresar un numero valido")
    print(f"Elegiste el destino {destinos[destinoElegido]}")
    destino = destinos[destinoElegido]

    # Fechas de viaje
    while True:
        fecha_salida = input("Ingrese fecha de salida (DD/MM/AAAA): ")
        fecha_regreso = input("Ingrese fecha de regreso (DD/MM/AAAA): ")
        if validar_fechas(fecha_salida, fecha_regreso):
            print("Se ha registrado la fecha ")
            break
        else:
            print("Fechas invalidas, Por favor, asegurese de que ambas fechas esten formato DD/MM/AAAA y que la fecha de regreso sea posterior a la de salida ")
    # Alojamiento
    alojamientos = ["Hotel", "Hostal", "Apartamentos", "Camping"]
    print("Opciones de Alojamiento: ")
    for i, alojamiento in enumerate(alojamientos):
        print(f"{i+1}. {alojamiento}")
    while True:
        try:
            tipoAlojamieto = int(input("Ingrese el numero del destino: ")) -1
            if 0 <= tipoAlojamieto < len(alojamientos):
                break
            else:
                print("Opcion Invalida. Por favor, Ingrese un numero del 1 al",len(alojamientos))
        except ValueError:
            print("Debe ingresar un numero valido")
    print(f"Elegiste el Alojamiento {alojamientos[tipoAlojamieto]}")
    alojamiento = alojamientos[tipoAlojamieto]

    # Actividades
    actividades = ["Buceo", "Malecon", "Visitas guiadas", "Lanchas"]
    print("Actividades a disponer:")
    for i, actividad in enumerate(actividades):
            print(f"{i+1}. {actividad}")
    while True:
        try:   
            actividades_elegidas = int(input("Ingrese los números de las actividades ")) -1
            if 0 <= actividades_elegidas < len(actividades):
                break
            else:
                print("Opcion invalida, Por favor, Ingrese un numero del 1 al",len (actividades))
        except ValueError:
            print("Debe ingresar un numero valido")
        print(f"Elegiste la actividad {actividades[actividades_elegidas]}")
    actividad = actividades[actividades_elegidas]

    # Precios
    def calcular_precio(destinos, alojamiento, actividades_elegidas):
        precios_destinos = {"Santa Marta": 3000000, "Cartagena": 2000000, "Desierto del Tatacoa": 12000000, "Valle del Cocora": 800000}
        precios_alojamientos = {"Hotel": 500000, "Hostal": 250000, "Apartamentos": 350000, "Camping": 100000}
        precio_base = precios_destinos[destinos[destinoElegido]] + precios_alojamientos[alojamiento]
        precio_actividades = (actividades_elegidas) * 100000
        return precio_base + precio_actividades

    precio_total = calcular_precio(destinos, alojamiento, actividades_elegidas)

    # Confirmar reserva
    print("\nResumen de su reserva:")
    print(f"Nombre: {nombre} {apellidos}")
    print(f"ID {idUnico}")
    print(f"Destino: {destinos[destinoElegido]}")
    print(f"Fechas: {fecha_salida} - {fecha_regreso}")
    print(f"Alojamiento: {alojamiento}")
    print(f"Actividades: {actividades[actividades_elegidas]}")
    print(f"Precio total: ${precio_total:,.2f}")

    confirmar = input("¿Confirma la reserva? (si/no): ")
    if confirmar.lower() == "si":
        print("¡Reserva confirmada!")
    else:        
        print("Reserva cancelada.")
def actualizarUsuario():
    idUnico=(input("Ingrese la ID de usuario registrado para actualizar: "))
    for reserva in reservas:
        if reserva["id"] == idUnico:
            print(f"actualizando informacion de {idUnico}")
            reserva ["nombre"] = (input("Ingrese el nuevo nombre: "))
            reserva ["apellido"] = (input("Ingrese el nuevo apellido: "))
            reserva ["fecha de nacimiento"] = (input("Ingrese la nueva fecha con formato DD/MM/AAAA. "))
            print(f"Informacion de {idUnico} actualizada exitosamente")
            print(reserva)
        return
    print(f"No se encontro ningun usuario con esta ID registrada {idUnico} ")
def consultarPaquetes():
    print("\nPaquetes turísticos disponibles:")
    for id_paquete, paquete in paquetesPredeterminados.items():
        print(f"Paquete {id_paquete}:")
        print(f"  Destino: {paquete['destino']}")
        print(f"  Duración: {paquete['duracion']} días")
        print(f"  Alojamiento: {paquete['alojamiento']}")
        print(f"  Actividades:")
        for actividad in paquete['actividades']:
            print(f"- {actividad}")
        print(f"  Precio: ${paquete['precio']}")
    while True:
        opcion = input("¿Desea seleccionar un paquete predefinido (si, no)? ").lower()
        if opcion == "si":
            while True:
                try:
                    id_paquete = int(input("Ingrese el número del paquete: "))
                    if id_paquete in paquetesPredeterminados:
                        paquete_seleccionado = paquetesPredeterminados[id_paquete]
                        print(f"Has registrado el paquete N°:{id_paquete}")
                        print(f"Paquete {id_paquete}:")
                        print(f"  Destino: {paquete['destino']}")
                        print(f"  Duración: {paquete['duracion']} días")
                        print(f"  Alojamiento: {paquete['alojamiento']}")
                        print(f"  Actividades:")
                        for actividad in paquete['actividades']:
                            print(f"- {actividad}")
                        print(f"  Precio: ${paquete['precio']}")
                        return paquete_seleccionado
                    else:
                        print("Paquete no válido. Por favor, ingrese un número válido.")
                except ValueError:
                    print("Debe ingresar un número entero.")
        elif opcion == "no":
            print("De regreso al menu principal ")
            break 
        else:
            print("Opción inválida. Por favor, ingrese 'si' o 'no'.")
def eliminarReserva():
    idUnico = input("Ingrese la ID de la reserva a eliminar: ")
    for index, reserva in enumerate(reservas):
        if reserva["id"] == idUnico:
            del reservas[index]
            print(f"La reserva con ID {idUnico} ha sido eliminada exitosamente")
            return
    print(f"No se encontró ninguna reserva con esa ID {idUnico}")

def validarNombre(nombre):
    #Valida que lo que se escriba son letras, no se registra espacios en blancos, ni puntos, ni numero, solo palabras
    if nombre.isalpha():
        return True
    else:
        return False
def validarapellidos(apellidos):
    #Valida que los apellidos solo contengan letras
    if apellidos.isalpha():
        return True
    else:
        return False
def validarfecha(fechaNacimiento):
    #Valida que la fecha tenga el formato DD/MM/AAAA y sea válida."""
    try:
        fechaNacimiento = datetime.datetime.strptime(fechaNacimiento, "%d/%m/%Y").date()
        return  fechaNacimiento
    except ValueError:
        return False
def generarid(fecha_nacimiento):
    complementos = fecha_nacimiento.split ('/')
    fecha = int(complementos[0])*1000 + int(complementos[1])*100 +int(complementos[2])
    idAleatorio = random.randint (1000,9999)
    idGenerado = str (fecha) + str (idAleatorio)
    return idGenerado
def validar_fechas(fecha_salida, fecha_regreso):
    try:
        fecha_salida = datetime.datetime.strptime(fecha_salida, "%d/%m/%Y").date()
        fecha_regreso = datetime.datetime.strptime(fecha_regreso, "%d/%m/%Y").date()
        return fecha_regreso> fecha_salida
    except ValueError:
        return False
def validar_origen (origen):
    if origen.isalpha():
        return True
    else:
        return False
def validar_salida (destino):
    if destino.isalpha():
        return True
    else:
        return False
def registrar_vuelo():
    while True:
        nombre = input("Ingrese su nombre: ")
        if validarNombre(nombre):
            break
        else:
            print("Por favor ingrese solo palabras")

    while True:
        apellidos = input("Ingrese su apellido: ")
        if validarapellidos(apellidos):
            break
        else:
            print("Por favor ingrese solo palabras")

    while True:
        fechaNacimiento = input("Ingrese fecha de nacimiento (DD/MM/AAAA): ")
        if validarfecha(fechaNacimiento):
            break
        else:
            print("Fecha de nacimiento inválida. Por favor, usar el formato indicado")

    idUnico = generarid(fechaNacimiento)

    while True:
        fecha_salida = input("Ingrese fecha de salida (DD/MM/AAAA): ")
        fecha_regreso = input("Ingrese fecha de regreso (DD/MM/AAAA): ")
        if validar_fechas(fecha_salida, fecha_regreso):
            print("Se ha registrado la fecha")
            break
        else:
            print("Fechas inválidas, por favor asegúrese de que ambas fechas estén en formato DD/MM/AAAA y que la fecha de regreso sea posterior a la de salida")

    while True:
        origen = input("Por favor ingrese la ciudad de origen: ")
        if validar_origen(origen):
            break
        else:
            print("Por favor ingrese solo palabras")

    while True:
        destino = input("Por favor ingrese la ciudad de destino: ")
        if validar_salida(destino):
            break
        else:
            print("Por favor ingrese solo palabras")

    aerolineas = ["Copa Airlines", "Avianca", "Wingo", "Latam"]
    print("Aerolineas disponibles, elija la de su preferencia: ")
    for i, aerolinea in enumerate(aerolineas):
        print(f"{i+1}. {aerolinea}")

    while True:
        try:
            aerolineaEscogida = int(input("Ingrese el número de la aerolínea: ")) - 1
            if 0 <= aerolineaEscogida < len(aerolineas):
                break
            else:
                print("Opción inválida. Por favor, ingrese un número del 1 al", len(aerolineas))
        except ValueError:
            print("Debe ingresar un número válido")

    print(f"Elegiste la aerolínea {aerolineas[aerolineaEscogida]}")
    aerolinea = aerolineas[aerolineaEscogida]
    print("Vuelo registrado exitosamente.")

    vuelos = {
        "nombre": nombre,
        "apellido": apellidos,
        "fecha de nacimiento": fechaNacimiento,
        "id": idUnico,
        "fecha de salida": fecha_salida,
        "fecha de regreso": fecha_regreso,
        "origen": origen,
        "destino": destino,
        "aerolinea":aerolineas[aerolineaEscogida]}

    def precio_de_vuelo(origen, destino, aerolinea):
        precioCiudades = {"cali": 100000, "bogota": 250000, "cartagena": 350000, "medellin": 150000}
        precioAerolineas = {"Copa Airlines": 20000, "Avianca": 30000, "Wingo": 15000, "Latam": 25000}
        precio_base = precioCiudades[origen] + precioCiudades[destino] + precioAerolineas[aerolinea]
        return precio_base

    precioTotal = precio_de_vuelo(origen, destino, aerolinea)
    print(f"Precio total: ${precioTotal:,.2f}")

    vuelos_registrados.append(vuelos) 
    print(f"Usuario {nombre} {apellidos} con ID {idUnico} registrado exitosamente.")
    print("\nResumen de su reserva:")
    print(f"Nombre: {nombre} {apellidos}")
    print(f"ID {idUnico}")
    print(f"Origen: {origen} - {destino}")
    print(f"Fechas: {fecha_salida} - {fecha_regreso}")
    print(f"Precio total: ${precioTotal:,.2f}")

    confirmar = input("¿Confirma la reserva? (si/no): ")
    if confirmar.lower() == "si":
        print("¡Reserva confirmada!")
    else:        
        print("Reserva cancelada.")
    print(vuelos_registrados)
def actualizar_vuelo():
    id_vuelo = input("Ingrese el ID del vuelo que desea actualizar: ")
    for vuelo in vuelos_registrados:
        if vuelo["id"] == id_vuelo: 
            print("Vuelo encontrado. Ingrese los nuevos datos (deje en blanco para mantener el valor actual).")

            nueva_aerolinea = input("Nueva aerolínea (actual: {}): ".format(vuelo["aerolinea"]))
            if nueva_aerolinea: 
                vuelo["aerolinea"] = nueva_aerolinea

            nueva_fecha_salida = input("Nueva fecha de salida (actual: {}): ".format(vuelo["fecha de salida"]))
            if nueva_fecha_salida:
                vuelo["fecha de salida"] = nueva_fecha_salida

            nueva_fecha_regreso = input("Nueva fecha de regreso (actual: {}): ".format(vuelo["fecha de regreso"]))
            if nueva_fecha_regreso:
                vuelo["fecha de regreso"] = nueva_fecha_regreso

            nuevo_origen = input("Nueva ciudad de origen (actual: {}): ".format(vuelo["origen"]))
            if nuevo_origen:
                vuelo["origen"] = nuevo_origen

            nuevo_destino = input("Nueva ciudad de destino (actual: {}): ".format(vuelo["destino"]))
            if nuevo_destino:
                vuelo["destino"] = nuevo_destino

            print("Vuelo actualizado exitosamente.")
            return

    print("No se encontró ningún vuelo con ese ID.")
def consultar_vuelo():
    id_vuelo = input("Ingrese el ID del vuelo que desea consultar: ")
    for vuelo in vuelos_registrados:
        if vuelo["id"] == id_vuelo:  # Accede al ID usando la clave del diccionario
            print("\n--- Detalles del Vuelo ---")
            print(f"ID: {vuelo['id']}")
            print(f"Nombre: {vuelo['nombre']}")
            print(f"Apellido: {vuelo['apellido']}")
            print(f"Fecha de Nacimiento: {vuelo['fecha de nacimiento']}")
            print(f"Fecha de Salida: {vuelo['fecha de salida']}")
            print(f"Fecha de Regreso: {vuelo['fecha de regreso']}")
            print(f"Origen: {vuelo['origen']}")
            print(f"Destino: {vuelo['destino']}")
            print(f"Aerolínea: {vuelo['aerolinea']}")
            return
    print("No se encontró ningún vuelo con ese ID.")
def cancelar_vuelo():
    id_vuelo = input("Ingrese el ID del vuelo que desea cancelar: ")
    for i, vuelo in enumerate(vuelos_registrados):
        if vuelo["id"] == id_vuelo: 
            del vuelos_registrados[i]
            print("Vuelo cancelado exitosamente.")
            return
    print("No se encontró ningún vuelo con ese ID.")

def menu():
    while True:
        menu_principal()
        opcion = input("Seleccione una opcion[1,3]: ")
        if opcion == "1":
            while True:
                menuDePaquetes()
                while True:
                    opcion = input("Seleccione una opcion[1,5]: ")
                    if opcion == "1":
                        reservar_viaje()
                    elif opcion == "2":
                        actualizarUsuario()
                    elif opcion == "3":
                        consultarPaquetes()
                    elif opcion == "4":
                        eliminarReserva()
                    elif opcion == "5":
                        print("Salir al menu principal")
                        break
                    else:
                        print("Opcion no valida, por favor, seleccione una opcion del 1 al 5: ")

        elif opcion == "2":
            while True:
                menuDeVuelos()
                if opcion == "1":
                    registrar_vuelo
                elif opcion == "2":
                    actualizar_vuelo
                elif opcion == "3":
                    consultar_vuelo
                elif opcion == "4":
                    eliminarReserva
                elif opcion =="5":
                    print("Salir al menu principal")
                    break
                else:
                  print("Opcion no valida, por favor, seleccione una opcion del 1 al 5: ")  

        elif opcion == "3":
            print("Presione 3 para salir del sistema")
            break
        else:
            print("Opción no válida, por favor, seleccione una opción del 1 al 3.")
menu()