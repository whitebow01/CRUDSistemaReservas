import menuAdmin

#REGISTRO DE CLIENTES
registroClientes=[{1:"20326456-8",2:"Luis",3:"Molla"},
                {1: "17854629-4", 2: "Carlos", 3: "Fernández"},
                {1: "20316587-7", 2: "Ana", 3: "Martínez"},
                {1: "18923467-1", 2: "Jorge", 3: "Pérez"},                
                ]


def default():
    print("Opcion fuera de rango")
    return

#LISTA DE CLIENTES
def vistaClientes():
        for x in registroClientes:
            print("==============================")
            print(f" Rut: {x[1]} \n  Nombre: {x[2]} \n Apellido:{x[3]}")
            print("==============================")
        
            
#REGISTRAR CLIENTES
def registroCliente():
    registro = {1:"",2:"",3:""}
    rutCliente = input("Ingresa rut del cliente \n")
    registro[1] = rutCliente
    nombreCliente = input("Ingresa el nombre del cliente \n")
    registro[2] = nombreCliente
    apellidoCliente = input("Ingrese apellido del cliente \n")
    registro[3] = apellidoCliente
    registroClientes.append(registro)
    
    print(f"""
        =================================
        Cliente registrado 
        =================================
        RUT: {rutCliente}
        Nombre cliente: {nombreCliente}
        Apellido cliente: {apellidoCliente}
        =================================
        """)
    
#ELIMINAR UN CLIENTE
def eliminarCliente():
    rutCliente = input("Ingresa el rut a eliminar \n")
    for cliente in registroClientes:
        if cliente[1] == rutCliente:
            registroClientes.remove(cliente)
            print("==============================")
            print("Cliente eliminado")
            print("==============================")

            break
        else:
            print("Cliente no encontrado")
            print("==============================")

#MODIFICAR UN CLIENTE
def modificarCliente():
    encontrado = False

    while not encontrado:
        
        rutCliente = input("Ingresa el rut del cliente \n")
        for cliente in registroClientes:    
            if cliente[1] == rutCliente:
                
                print("Cliente encontrado")
                print("==============================")

                print("1.Nombre \n 2.Apellido")
                eleccion = input("Seleccione quiere modificar?? \n")
                
                if eleccion == "1":
                    nombre = input("Ingrese nuevo nombre \n")
                    cliente[2] = nombre
                    print(f"Nombre cambiado a {nombre}")

                elif eleccion == "2":
                    apellido = input("Ingrese nuevo apellido \n")
                    cliente[3] = apellido
                    print(f"Apellido cambiado a {apellido}")

                else:
                    print("Eleccion incorrecta")
                    print("==============================")
                    
                encontrado = True
                break
            
        if encontrado:
            break
        
        if not encontrado:
            print("No se encuentra el rut del cliente")    
            pregunta = input("Quisiera intentar con otro rut? \n")
            if pregunta != "si":
                break
            
#DICCIONARIO CON MENU - ADMINISTRACION CLIENTES   
def menuCliente():    
    menuClientes = {1: vistaClientes, 
                    2: registroCliente, 
                    3:modificarCliente,
                    4:eliminarCliente, 
                    5:menuAdmin.menuAdministrador
                    }

    respuesta = "si"
    while respuesta =="si":
        print("\n--- Administración de Clientes ---")
        print("Opcion 1:  Listar clientes")
        print("Opcion 2:  Registrar cliente")
        print("Opcion 3: Modificar cliente")
        print("Opcion 4:  Eliminar cliente")
        print("Opcion 5: Volver al menu principal")
            
        opcion = int(input("ELija una opcion \n"))
        if opcion == 5:
            respuesta = input("Seguro quiere salir?? si/no \n")
            respuesta = respuesta.lower()
            
        menuClientes.get(opcion,default)()