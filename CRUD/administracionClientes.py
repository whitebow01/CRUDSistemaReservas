import menuAdmin

#REGISTRO DE CLIENTES
registroClientes=[{1:"20326456-8",2:"Luis",3:"Molla"},
                {1: "17854629-4", 2: "Carlos", 3: "Fernández"},
                {1: "20316587-7", 2: "Ana", 3: "Martínez"},
                {1: "18923467-1", 2: "Jorge", 3: "Pérez"},                
                ]


def default():
    print("Opción fuera de rango")
    return

#LISTA DE CLIENTES
def vistaClientes():
    cont = 0
    for x in registroClientes:
        print("══════════════════════════════")
        print(f" Rut: {x[1]} \n  Nombre: {x[2]} \n Apellido:{x[3]}")
        print("══════════════════════════════")
        
    for f in registroClientes:
        if f[1] != 0:
            cont +=1
            
    print(f"Clientes registrados: {cont}")
    print("══════════════════════════════")
    import time
    time.sleep(2)
    
#REGISTRAR CLIENTES
def registroCliente():
    registro = {1:"",2:"",3:""}
    while True:
        try:
            rutCliente = int(input("Ingresa su rut sin guión ni dígito verificador \n"))
            break
        except ValueError:
            print("Error. No puede ingresar letras, ni signos")
    digito = input("Ingrese digito verificador sin guíon\n")
    
    rut = str(rutCliente)+"-"+digito
    registro[1] = rut
    
    nombreCliente = input("Ingresa el nombre del cliente \n")
    registro[2] = nombreCliente
    apellidoCliente = input("Ingrese apellido del cliente \n")
    registro[3] = apellidoCliente
    registroClientes.append(registro)
    
    print(f"""
        ═════════════════════════════════
        Cliente registrado 
        ═════════════════════════════════
        RUT: {rutCliente}-{digito}
        Nombre cliente: {nombreCliente}
        Apellido cliente: {apellidoCliente}
        ═════════════════════════════════
        """)
    
#ELIMINAR UN CLIENTE
def eliminarCliente():
    print("════════════════════════════════")
    print("Clientes registrados:")
    print("═════════════════════════════════")

    for clientes in registroClientes:
        print(f" RUT: {clientes[1]}")

    print("═════════════════════════════════")
    
    encontrado = False
    rutCliente = input("Ingresa el RUT a eliminar \n")
    for cliente in registroClientes:
        if cliente[1] == rutCliente:
            registroClientes.remove(cliente)
            print("══════════════════════════════")
            print("Cliente eliminado")
            print("══════════════════════════════")
            encontrado = True
            import time
            time.sleep(2)
            break
    if not encontrado:    
        print("Cliente no encontrado")
        print("══════════════════════════════")
        import time
        time.sleep(2)

#MODIFICAR UN CLIENTE
def modificarCliente():
    encontrado = False

    while not encontrado:
        
        rutCliente = input("Ingresa el RUT del cliente \n")
        for cliente in registroClientes:    
            if cliente[1] == rutCliente:
                
                print("Cliente encontrado")
                print("══════════════════════════════")

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
                    print("Elección incorrecta")
                    print("══════════════════════════════")
                    
                encontrado = True
                import time
                time.sleep(2)
                break
            
        if encontrado:
            break
        
        if not encontrado:
            print("No se encuentra el RUT del cliente")    
            pregunta = input("Quisiera intentar con otro rut? si/no \n")
            if pregunta != "si":
                import time
                time.sleep(2)
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
        print("\n═══ Administración de Clientes ═══")
        print("Opción 1:  Listar clientes")
        print("Opción 2:  Registrar cliente")
        print("Opción 3:  Modificar cliente")
        print("Opción 4:  Eliminar cliente")
        print("Opción 5:  Volver al menu principal")
            
        opcion = int(input("Elija una opción \n"))
        if opcion == 5:
            respuesta = input("Seguro quiere salir?? si/no \n")
            respuesta = respuesta.lower()
            
        menuClientes.get(opcion,default)()