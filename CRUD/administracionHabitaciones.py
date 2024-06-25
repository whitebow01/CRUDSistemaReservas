import menuAdmin

#REGISTRO HABITACIONES    
registroHabitaciones = [{1:1, 2: "1", 3: "Individual",4:20000,"reservado":False},
                        {1:2, 2: "2", 3: "Doble", 4:25000, "reservado":True},
                        {1:3, 2: "3", 3: "Suite", 4:42000, "reservado":False},
                        {1:4, 2: "4", 3: "Individual", 4:15000, "reservado":True},
                        {1:5, 2: "5", 3: "Doble", 4:30000, "reservado":False}
                        ]

#LISTA DE HABITACIONES
def vistaHabitaciones():
    cont = 0
    for x in registroHabitaciones:
        print("══════════════════════════════")
        print(f" ID:{x[1]} \n N°Habitacion:{x[2]} \n Tipo:{x[3]} \n Valor:${x[4]}, \n Etado:{x["reservado"]}")
        print("══════════════════════════════")
        
    for f in registroHabitaciones:
        if f["reservado"] == False:
            cont +=1
            
    print(f"Las habitaciones desocupadas son: {cont}")
    print("══════════════════════════════════════")        
        # import time
        # time.sleep(1)
        
#REGISTRAR HABITACIONES       
def registroHabitacion():
    registro = {}
    idHabitacion = len(registroHabitaciones)+1 #autoincremental
    registro[1] = idHabitacion
    numeroHabitacion = len(registroHabitaciones)+1 #autoincremental
    registro[2] = numeroHabitacion
    print("═══════════════════════════")
    print("Individual - Doble - Suite")
    print("═══════════════════════════")
    valido = False
    while not valido:
        tipoHabitacion = input("Ingrese tipo de habitacion \n")
        if tipoHabitacion in ["Individual", "Doble", "Suite"]:
            registro[3] = tipoHabitacion
            valido = True
            break
        
    while True:
        try:
            valorHabitacion = int(input("Ingrese valor de la habitacion \n"))
            registro[4] = valorHabitacion
            break
        except ValueError:
            print("Error. No puede ingresar letras ni signos, solo numeros")
            import time
            time.sleep(2)
                
    estadoHabitacion = False
    registro["reservado"] = estadoHabitacion
    
    registroHabitaciones.append(registro)
    print(f"""
        ═════════════════════════════════
        Habitación creada
        ═════════════════════════════════
        ID: {idHabitacion}  
        Número habitación: {numeroHabitacion}
        Tipo habitación: {tipoHabitacion}
        Valor habitación:${valorHabitacion}
        ═════════════════════════════════
        """)
    import time
    time.sleep(2)
    
#ELIMINAR UNA HABITACION
def eliminarHabitacion():

    while True:
        try:
            idHabitacion = int(input("Ingrese la habitación que quiere eliminar \n"))
            break
        except ValueError:
            print("Error. Por favor, ingrese solo numeros")
    encontrada = False

    for habitacion in registroHabitaciones:
        if habitacion[1] == idHabitacion:
            registroHabitaciones.remove(habitacion)
            print("════════════════════════════════════")
            print("Habitación eliminada existosamente")
            print("════════════════════════════════════")
            encontrada = True
            import time
            time.sleep(2)
            break            
    if not encontrada:
        print("══════════════════════════════")
        print("Habitacion no encontrado")
        print("══════════════════════════════")
        import time
        time.sleep(2)
            
            
#MODIFICAR UNA HABITACION                
def modificarHabitacion():
    encontrado = False
    idHabitacion = int(input("Ingrese la habitacion que quiere modificar \n"))

    for habitacion in registroHabitaciones:
        if habitacion[1] == idHabitacion:
            encontrado = True
            print("Habitacion encontrado")
            print("══════════════════════════════")
            print("1.Tipo \n 2.Valor")
            eleccion = input("Seleccione cual quiere modificar?? \n")
            if eleccion == "1":
                print("Individual - Doble - Suite")
                
                validacion = False
                while not validacion:
                    tipo = input("Ingrese  el nuevo tipo de habitacion \n")
                    if tipo in ["Individual", "Doble", "Suite"]:
                        habitacion[3] = tipo
                        validacion = True
                        print(f"""
                                ═════════════════════════════════
                                Habitacion modificada
                                ═════════════════════════════════
                                ID: {habitacion[1]}  
                                Número habitación: {habitacion[2]}
                                Tipo habitación: {habitacion[3]}
                                Valor habitación:${habitacion[4]}
                                Estado habitación: {habitacion["reservado"]}
                                ═════════════════════════════════
                                """)
                        import time
                        time.sleep(2)
                        break
            elif eleccion == "2":
                
                while True:
                    try:
                        valor = int(input("Ingrese nuevo valor de la habitación \n"))
                        habitacion[4] = valor
                        print(f"""
                        ═════════════════════════════════
                        Habitacion modificada
                        ═════════════════════════════════
                        ID: {habitacion[1]}  
                        Número habitación: {habitacion[2]}
                        Tipo habitación: {habitacion[3]}
                        Valor habitación:${habitacion[4]}
                        Estado habitación: {habitacion["reservado"]}
                        ═════════════════════════════════
                        """)
                        import time
                        time.sleep(2)
                        break
                        
                    except ValueError:
                        print("Error. Por favor, ingrese cifras en numeros")
                        import time
                        time.sleep(2)
                        
            else:
                print("Elección incorrecta")
                return
            
            break
    
    if not encontrado:
        # modificarHabitacion() # VER SI RESULTA
        print("══════════════════════════════")
        print("No se encuentra el id de la habitacion")  
        print("══════════════════════════════")
        import time
        time.sleep(2)    
            
#DICCIONARIO CON MENU - ADMINISTRACION HABITACIONESS   
def menuHabitacion():     
    menuHabitaciones = {1:vistaHabitaciones, 
                        2:registroHabitacion,
                        3:modificarHabitacion,
                        4:eliminarHabitacion,
                        5:menuAdmin.menuAdministrador
                        }
    respuesta = "si"
    while respuesta =="si":
        print("\n═══ Administración de Habitaciones ═══")
        print("Opcion 1:  Listar habitaciones")
        print("Opcion 2:  Registrar habitación")
        print("Opcion 3:  Modificar habitación")
        print("Opcion 4:  Eliminar habitación")
        print("Opcion 5:  Volver al menu principal")

        try:   
            opcion = int(input("Elija una opcion \n"))
            if opcion ==5:
                respuesta = input("Seguro quiere salir al menú general?? si/no \n")
                respuesta = respuesta.lower()
            
            menuHabitaciones.get(opcion)()
        except ValueError:
            print("Error. Por favor, ingrese solo numeros")
            import time
            time.sleep(2)