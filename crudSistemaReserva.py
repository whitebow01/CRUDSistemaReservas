import registros

reservaciones= [{}]

def default():
    print("Opcion fuera de rango") 
    


#TRABAJADORES
def administrarTrabajadores():
    listaTrabajadores = registros.registroTrabajadores


    def listaTrab():
        for x in listaTrabajadores:
            print(f" {x[1]} \n {x[2]} \n {x[3]} \n {x[4]} \n")

    respuesta = "si"
    while respuesta =="si":
        print("\n--- Administración de Clientes ---")
        print("Opcion 1:  Listar clientes")
        print("Opcion 2:  Registrar cliente")
        print("Opcion 3: Modificar cliete")
        print("Opcion 4:  Eliminar cliente")
                
        #opcion = int(input("ELija una opcion \n"))
        #menuClientes.get(opcion)()
            
        respuesta = input("Administrará algo mas en trabajadores?? si/no \n")
        respuesta = respuesta.lower()

#CLIENTES
def administracionClientes():
    listaClientes = registros.registroClientes

    def vistaClientes():
        for x in listaClientes:
            print(f" Rut: {x[1]} \n  Nombre: {x[2]} \n Apellido:{x[3]}")
    
    
    # def modificarCliente():
    #     bandera = False
    #     encontrado = False
        
    #     rutCliente = input("Ingresa el rut del cliente")
    #     if rutCliente in listaClientes:
    #         print("Cliente encontrado")
    #     nombre = input("Ingrese rut a modificar")

    #     for x in listaClientes:
    #         bandera = rutCliente in x
    #         if (bandera):
    #             aux = listaClientes.index(x)
    #             encontrado = True
    #         if (encontrado):
    #             listaClientes[aux][2] = nombre
    #         else:
    #             print("El cliente no esta registrado")    
    
    def eliminarCliente():
        rutCliente = input("Ingresa el rut del cliente")
        encontrado = False
        for x in listaClientes:
            if x[1] == rutCliente:
                listaClientes.remove(x)
                encontrado = True
                print("Cliente eliminado")
                break
            else:
                print("Cliente no encontrado")
                
    #DICCIONARIO CON MENU - ADMINISTRACION CLIENTES       
    menuClientes = {1: vistaClientes, 2:registros.registroCliente, 4:eliminarCliente}
    
    respuesta = "si"
    while respuesta =="si":
        print("\n--- Administración de Clientes ---")
        print("Opcion 1:  Listar clientes")
        print("Opcion 2:  Registrar cliente")
        print("Opcion 3: Modificar cliete")
        print("Opcion 4:  Eliminar cliente")
            
        opcion = int(input("ELija una opcion \n"))
        menuClientes.get(opcion)()
        
        respuesta = input("Administrará algo mas en clientes?? si/no \n")
        respuesta = respuesta.lower()
            
        

#HABITACIONES
listaHabitaciones = registros.registroHabitaciones
def administracionHabitaciones():
    
    
    respuesta = "si"
    while respuesta =="si":
        print("\n--- Administración de Clientes ---")
        print("Opcion 1:  Listar clientes")
        print("Opcion 2:  Registrar cliente")
        print("Opcion 3: Modificar cliete")
        print("Opcion 4:  Eliminar cliente")
            
        opcion = int(input("ELija una opcion \n"))
        #menuClientes.get(opcion)()
        
        respuesta = input("Administrará algo mas en habitaciones?? si/no \n")
        respuesta = respuesta.lower()

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
        menu.get(opcion)()

        respuesta = input("Quiere hacer algo mas en el menu general? si/no \n")
        respuesta = respuesta.lower()
        