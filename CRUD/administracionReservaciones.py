import CRUD.administracionClientes
import CRUD.administracionHabitaciones
import menuAdmin


listaClientes = CRUD.administracionClientes.registroClientes
listaHabitaciones = CRUD.administracionHabitaciones.registroHabitaciones

#REGISTRO RESERVACIONES
registroReservaciones = [{1:2,2:"20326456-8",3:"16884"}]

#LISTA DE RESERVACIONES    
def vistaReservas():
    cont = 0
    for x in registroReservaciones:
        print("═════════════════════════════════")
        print(f" ID:{x[1]} \n Cliente:{x[2]} \n Habitacion:{x[3]}")
        print("═════════════════════════════════")
    
    for f in registroReservaciones:
        if f[1] != 0:
            cont +=1
            
    print(f"Rerservaciones registradas: {cont}")
    print("══════════════════════════════")
            
    import time
    time.sleep(2)

#REGISTRO DE RESERVACIONES
def registroReserva():
    print("════════════════════════════════")
    print("Clientes registrados:")
    print("═════════════════════════════════")

    for clientes in CRUD.administracionClientes.registroClientes:
        print(f" Rut: {clientes[1]}")

    print("═════════════════════════════════")
    idReserva = len(registroReservaciones)+1 #Autoincremental
    rutCliente = input("Igrese rut del cliente \n")
    
    clienteEncontrado = False
    for cliente in listaClientes:
        if cliente[1] == rutCliente:
            clienteEncontrado = True
            break
    if not clienteEncontrado:
        print("Cliente no encontrado")
        import time
        time.sleep(2)
        return
    print("═════════════════════════════════")
    print("Habitaciones disponibles:")
    print("═════════════════════════════════")
    for habitaciones in CRUD.administracionHabitaciones.registroHabitaciones:
        if habitaciones["reservado"] == False:
            print(f"ID:{habitaciones[1]}, Habitacion:{habitaciones[2]}, {habitaciones[3]}")
            
    print("═════════════════════════════════")
    while True:
        try:
            idHabitacion = int(input("Ingrese id habitacion \n"))
            break
        except ValueError:
            print("Error. Ingrese solo numeros")
        
    habitacionEncontrada = False
    for habitacion in listaHabitaciones:
        if habitacion[1] == idHabitacion:
            if habitacion["reservado"] == False:
                habitacionEncontrada = True
                #CREAMOS LA RESERVA CON EL RUT Y EL ID DE LA HABITACION
                if not habitacion["reservado"]:
                    #Se agrega la reserva
                    reserva = {1:idReserva,
                                2:cliente[1],
                                3:habitacion[1]
                                }
                    registroReservaciones.append(reserva)
                    habitacion["reservado"] = True
                    #Si reservado en el registro de habitaciones es false, lo cambia a true
                    print("Agregado al sistema!")
                else:
                    print("Habitacion ocupada")
                    break
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
        
        Habitacion reservada con exito!
        ═════════════════════════════════
        ID: {idReserva} 
        RUT cliente: {cliente[1]}
        Nombre cliente: {cliente[2]} 
        ID Habitación: {habitacion[1]} 
        N° Habitación: {habitacion[2]}
        ═════════════════════════════════=
        """)
    import time
    time.sleep(2)

def eliminarReserva():
    print("════════════════════════════════")
    print("Reservas registrados:")
    print("═════════════════════════════════")
    for reserva in registroReservaciones:
        print(f" ID: {reserva[1]} - Cliente:{reserva[2]} - Habitacion ID:{reserva[3]}")
    print("═════════════════════════════════")
    
    encontrado = False
    while True:
        try:
            idReserva = int(input("Ingresa el ID de la reserva a eliminar \n"))
            break
        except ValueError:
            print("Error. No puede ingresar letras, ni signos")
        
    for x in registroReservaciones:
        if x[1] == idReserva:
            registroReservaciones.remove(x)
            print("══════════════════════════════")
            print("Reserva eliminada")
            print("══════════════════════════════")
            encontrado = True
            import time
            time.sleep(2)
            break
    if not encontrado:    
        print("ID no encontrado")
        print("══════════════════════════════")
        import time
        time.sleep(2)

#DICCIONARIO CON MENU - ADMINISTRACION RESERVACIONES   
def menuReserva():       
    menuReservaciones = {1:vistaReservas,
                        2:registroReserva,
                        3:eliminarReserva,
                        5:menuAdmin.menuAdministrador}
    respuesta = "si"
    while respuesta =="si":
        print("\n═══ Administración de Reservaciones ═══")
        print("Opcion 1:  Listar Reservaciones")
        print("Opcion 2:  Registrar Reservacion")
        print("Opcion 3:  Eliminar Reservacion")
        # print("Opcion 3: Modificar Reservacion") No es necesaria. SOlO son IDS
        print("Opcion 5: Volver al menu principal")
            
        opcion = int(input("Elija una opción \n"))
        if opcion == 5:
            respuesta = input("Seguro quiere salir?? si/no\n")
            respuesta = respuesta.lower()   
            
        menuReservaciones.get(opcion)()
        
        