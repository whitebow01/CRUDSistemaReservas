import CRUD.administracionClientes
import CRUD.administracionHabitaciones
import menuAdmin


listaClientes = CRUD.administracionClientes.registroClientes
listaHabitaciones = CRUD.administracionHabitaciones.registroHabitaciones

#REGISTRO RESERVACIONES
registroReservaciones = [{1:"2",2:"20326456-8",3:"16884"}]

#LISTA DE RESERVACIONES    
def vistaReservas():
    for x in registroReservaciones:
        print("=================================")
        print(f" ID:{x[1]} \n Cliente:{x[2]} \n Habitacion:{x[3]}")
        print("=================================")


#REGISTRO DE RESERVACIONES
def registroReserva():
    idReserva = len(registroReservaciones)+1 #Autoincremental
    rutCliente = input("Igrese rut del cliente \n")
    idHabitacion = int(input("Ingrese id habitacion \n"))
    
    clienteEncontrado = False
    for cliente in listaClientes:
        if cliente[1] == rutCliente:
            clienteEncontrado = True
            break
    if not clienteEncontrado:
        print("Cliente no encontrado")
        return
    
    habitacionEncontrada = False
    for habitacion in listaHabitaciones:
        if habitacion[1] == idHabitacion:
            habitacionEncontrada = True
            #CREAMOS LA RESERVA CON EL RUT Y EL ID DE LA HABITACION
            if not habitacion["reservado"]:
                registroHabitacion = {1:idReserva,2:cliente[1],3:habitacion[1]}
                registroReservaciones.append(registroHabitacion)
                habitacion["reservado"] = True
                #Si reservado en el registro de habitaciones es false, lo cambia a true
                print("Agregado al sistema!")
            else:
                print("La habitacion ya está reservada")
            break
        
    #lista de habitaciones, ver los cambios    
    # for habitacion in listaHabitaciones:
    #     print(habitacion)
    
    if not habitacionEncontrada:
        print("Habitacion no encontrada")
        return

    print(f"""
        =================================
        Habitacion reservada con exito!
        =================================
        ID: {idReserva} 
        RUT cliente: {cliente[1]}
        Nombre cliente: {cliente[2]} 
        ID Habitacion: {habitacion[1]} 
        N° Habitacion: {habitacion[2]}
        =================================
        """)



#DICCIONARIO CON MENU - ADMINISTRACION RESERVACIONES   
def menuReserva():       
    menuReservaciones = {1:vistaReservas,
                        2:registroReserva,
                        5:menuAdmin.menuAdministrador}
    respuesta = "si"
    while respuesta =="si":
        print("\n--- Administración de Reservaciones ---")
        print("Opcion 1:  Listar Reservaciones")
        print("Opcion 2:  Registrar Reservacion")
        # print("Opcion 3: Modificar Reservacion")
        # print("Opcion 4:  Eliminar Reservacion")
        print("Opcion 5: Volver al menu principal")
            
        opcion = int(input("ELija una opcion \n"))
        if opcion == 5:
            respuesta = input("Seguro quiere salir?? si/no\n")
            respuesta = respuesta.lower()   
            
        menuReservaciones.get(opcion)()
        
        