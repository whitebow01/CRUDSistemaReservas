import os,time

##MENU GENERAL - REGISTRO TRABAJADOR 
registroTrabajadores = [{1:"555", 2:"Juan", 3: "Castro",4:"sss"}]

def registroTrabajador():
    registro = {1:"", 2:"",3:"", 4:""}
    rutTrabajador = input("Ingrese su rut\n")
    registro[1] = rutTrabajador
    nombreTrabajador = input("Ingrese su nombre \n")
    registro[2] = nombreTrabajador
    apellidoTrabajador = input("Ingrese su apellido \n")
    registro[3] = apellidoTrabajador
    contraseñaTrabajador = input("Ingrese contraseña \n")
    registro[4] = contraseñaTrabajador

    registroTrabajadores.append(registro)

    print(f"Bienvenido, {nombreTrabajador}, ahora puede iniciar sesion")

    print(f"Tus datos:  \n rut: {rutTrabajador} \n nombre: {nombreTrabajador}\n apellido:{apellidoTrabajador}\n contraseña: """)


##MENU ADMIN - REGISTRO CLIENTE

registroClientes=[{1:"20326456-8",2:"Luis",3:"Molla"},
                {1: "17854629-4", 2: "Carlos", 3: "Fernández"},
                {1: "20316587-7", 2: "Ana", 3: "Martínez"},
                {1: "18923467-1", 2: "Jorge", 3: "Pérez"},
                ]

def registroCliente():
    registro = {1:"",2:"",3:""}
    rutCliente = input("Ingresa rut del cliente")
    registro[1] = rutCliente
    nombreCliente = input("Ingresa el nombre del cliente")
    registro[2] = nombreCliente
    apellidoCliente = input("Ingrese apellido del cliente")
    registro[3] = apellidoCliente
    registroClientes.append(registro)
    
    print(f"Cliente {nombreCliente} ingresado correctamente")


##MENU ADMIN - REGISTRO HABITACIONES    
registroHabitaciones = [{1:11, 2: "1", 3: "Individual",4:20000,"reservado":False},
                        {1:12, 2: "2", 3: "Doble", 4: 25000, "reservado":True},
                        {1:13, 2: "3", 3: "Suite", 4: 42000, "reservado":False},
                        {1:14, 2: "4", 3: "Individual", 4: 15000, "reservado":True},
                        {1:15, 2: "5", 3: "Doble", 4: 30000, "reservado":False}
                        ]

def registroHabitacion():
    registro = {1:"",2:"",3:"",4:"",5:""}
    idHaHabitacion = int(input("Ingrese id para habitacion"))#HACERLO ALEATORIO O AUTOINCREMENTAL
    registro[1] = idHaHabitacion
        # idHabitacion = []
        ## IDS autoincrementales
        # autoincrementalIdHabitacion = 1
    numeroHabitacion = int("Ingrese numero de habitacion")#Tambien aleatorio o autoincremental
    registro[2] = numeroHabitacion
    tipoHabitacion = input("Ingrese tipo de habitacion")
    registro[3] = tipoHabitacion
    valorHabitacion = int(input("Ingrese valor habitacion"))
    registro[4] = valorHabitacion
    estadoHabitacion = input("Reservado/Disponible")
    registro[5] = estadoHabitacion
    
    registroHabitaciones.append(registro)
    print(f"""
        Habitacion creada \n 
        ID: {idHaHabitacion} \n 
        Numero habitacion: {numeroHabitacion} \n 
        Tipo habitacion: {tipoHabitacion} \n 
        Valor habitacion: {valorHabitacion}
        """)
    

##MENU ADMIN - REGISTRO DE RESERVACIONES
#cliente 1 y habitacion 1
registroReservaciones = [{1:"2",2:"20326456-8",3:"16884"}]

def registroReserva():
    idReserva = len(registroReservaciones)+1
    #listar ruts
    rutCliente = input("Igrese rut del cliente")
    #listar habitaciones disponibles
    idHabitacion = int(input("Ingrese id habitacion"))
    
    clienteEncontrado = False
    for cliente in registroClientes:
        if cliente[1] == rutCliente:
            clienteEncontrado = True
            break
    if not clienteEncontrado:
        print("Cliente no encontrado")
        return
    
    habitacionEncontrada = False
    for habitacion in registroHabitaciones:
        if habitacion[1] == idHabitacion:
            habitacionEncontrada = True
            #CREAMOS LA RESERVA CON EL RUT Y EL ID DE LA HABITACION
            if not habitacion["reservado"]:
                registroHabitacion = {1:idReserva,2:cliente[1],3:habitacion[1]}
                registroReservaciones.append(registroHabitacion)
                habitacion["reservado"] = True
                #Si reservado en el registro de habitaciones es false, lo cambia a true
                print("Habitacion reservada con exito!")
            else:
                print("La habitacion ya está reservada")

            break
    #lista de habitaciones, ver los cambios    
    for habitacion in registroHabitaciones:
        print(habitacion)
        
    if not habitacionEncontrada:
        print("Habitacion no encontrada")
        return
    
    

