import registros

reservaciones= [{}]

def default():
    print("Opcion fuera de rango") 
    


# #TRABAJADORES
# def administrarTrabajadores():
#     listaTrabajadores = registros.registroTrabajadores


#     def listaTrab():
#         for x in listaTrabajadores:
#             print(f" {x[1]} \n {x[2]} \n {x[3]} \n {x[4]} \n")

#     menuAdminTrabaj = {1:listaTrab,5:menuAdmin}
    
#     respuesta = "si"
#     while respuesta =="si":
#         print("\n--- Administración de Clientes ---")
#         print("Opcion 1:  Listar clientes")
#         print("Opcion 2:  Registrar cliente")
#         print("Opcion 3: Modificar cliete")
#         print("Opcion 4:  Eliminar cliente")
#         print("Opcion 5: Volver al menu principal") 
        
#         opcion = int(input("ELija una opcion \n"))
#         menuAdminTrabaj.get(opcion, default)()
            
#         respuesta = input("Administrará algo mas en trabajadores?? si/no \n")
#         respuesta = respuesta.lower()

#CLIENTES
def administracionClientes():
    listaClientes = registros.registroClientes

    def vistaClientes():
        for x in listaClientes:
            print("==============================")
            print(f" Rut: {x[1]} \n  Nombre: {x[2]} \n Apellido:{x[3]}")
            print("==============================")
            
    #REGISTRAR CLIENTES DIRECTO AL MENU
            
    def eliminarCliente():
        rutCliente = input("Ingresa el rut del cliente")
        for x in listaClientes:
            if x[1] == rutCliente:
                listaClientes.remove(x)
                print("Cliente eliminado")
                break
            else:
                print("Cliente no encontrado")
    
    def modificarCliente():
        encontrado = False
        
        rutCliente = input("Ingresa el rut del cliente")
        for cliente in listaClientes:
            if rutCliente == cliente[1]:
                print("Cliente encontrado")
            nombre = input("Ingrese nombre a modificar")
            cliente[2] = nombre
            encontrado = True
            print(f"Nombre cambiado a {nombre}")
            break
        if not encontrado:
            print("No se encuentra el rut del cliente")

    
                
    #DICCIONARIO CON MENU - ADMINISTRACION CLIENTES       
    menuClientes = {1: vistaClientes, 
                    2:registros.registroCliente, 
                    3:modificarCliente,
                    4:eliminarCliente, 
                    5:menuAdmin
                    }
    
    respuesta = "si"
    while respuesta =="si":
        print("\n--- Administración de Clientes ---")
        print("Opcion 1:  Listar clientes")
        print("Opcion 2:  Registrar cliente")
        print("Opcion 3: Modificar cliete")
        print("Opcion 4:  Eliminar cliente")
        print("Opcion 5: Volver al menu principal")
            
        opcion = int(input("ELija una opcion \n"))
        menuClientes.get(opcion,default)()
        
        respuesta = input("Administrará algo mas en clientes?? si/no \n")
        respuesta = respuesta.lower()
            
        

#HABITACIONES
# listaHabitaciones = registros.registroHabitaciones
# def administracionHabitaciones():
    
    
#     respuesta = "si"
#     while respuesta =="si":
#         print("\n--- Administración de Clientes ---")
#         print("Opcion 1:  Listar clientes")
#         print("Opcion 2:  Registrar cliente")
#         print("Opcion 3: Modificar cliete")
#         print("Opcion 4:  Eliminar cliente")
            
#         opcion = int(input("ELija una opcion \n"))
#         #menuClientes.get(opcion)()
        
#         respuesta = input("Administrará algo mas en habitaciones?? si/no \n")
#         respuesta = respuesta.lower()

#RESERVACIONES





#MENU ADMIN
def menuAdmin():
    #DICCIONARIO CON MENU - MENU GENERAL ADMIN LOGEADO
    menu ={1:administracionClientes}

    respuesta = "si"
    while respuesta == "si":
        print("\n--- Menú Principal ---")
        print("1. Administrar clientes")
        print("2. Administrar trabajadores")
        print("3. Administrar habitaciones")
        
        opcion = int(input("ELija una opcion \n"))
        menu.get(opcion, default)()

        respuesta = input("Quiere hacer algo mas en el menu general? si/no \n")
        respuesta = respuesta.lower()
        