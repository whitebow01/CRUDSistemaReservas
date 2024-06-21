import registros

reservaciones= [{}]

def default():
    print("Opcion fuera de rango") 
    


#TRABAJADORES
listaTrabajadores = registros.registroTrabajadores

def listaTrab():
    for x in listaTrabajadores:
        print(f" {x[1]} \n {x[2]} \n {x[3]} \n {x[4]} \n")



#CLIENTES
def administracionClientes():
    listaClientes = registros.registroClientes

    def vistaClientes():
        for x in listaClientes:
            print(f" Rut: {x[1]} \n  Nombre: {x[2]} \n Apellido:{x[3]}")
    
    #DICCIONARIO CON MENU - ADMINISTRACION CLIENTES       
    menuClientes = {1: vistaClientes}
    
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


#RESERVACIONES





#MENU ADMIN

    

def menuAdmin():
    # menu ={1:administracionClientes}

    respuesta = "si"
    while respuesta == "si":
        print("\n--- Menú Principal ---")
        print("1. Administrar clientes")
        print("2. Administrar trabajadores")
        print("3. Administrar habitaciones")
        opcion = int(input("ELija una opcion \n"))
        
        if opcion == 1:
            administracionClientes()

            
            # try:
            #     opcion = int(input("ELija una opcion \n"))
            #     if opcion in menuAdmin:
            #         menuAdmin[opcion]()
            # except ValueError:
            #     print("Opcion fuera de rango")
        
        # elif opcion == '2':
        #     administracionTrabajadores()
        elif opcion == 4:
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida, intente de nuevo.")
        
        #menu.get(opcion.default)()
        respuesta = input("Quiere hacer algo mas en el menu general? si/no \n")
        respuesta = respuesta.lower()
        