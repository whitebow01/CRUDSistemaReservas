import menuAdmin

#REGISTRO HABITACIONES    
registroHabitaciones = [{1:1, 2: "1", 3: "Individual",4:20000,"reservado":False},
                        {1:2, 2: "2", 3: "Doble", 4: 25000, "reservado":True},
                        {1:3, 2: "3", 3: "Suite", 4: 42000, "reservado":False},
                        {1:4, 2: "4", 3: "Individual", 4: 15000, "reservado":True},
                        {1:5, 2: "5", 3: "Doble", 4: 30000, "reservado":False}
                        ]

#LISTA DE HABITACIONES
def vistaHabitaciones():
    for x in registroHabitaciones:
        print("==============================")
        print(f" ID:{x[1]} \n N°Habitacion:{x[2]} \n Tipo:{x[3]} \n Valor:${[4]}, \n Etado:{x["reservado"]}")
        print("==============================")

#REGISTRAR HABITACIONES       
def registroHabitacion():
    registro = {1:"",2:"",3:"",4:"","reservado":""}
    idHabitacion = len(registroHabitaciones)+1 #autoincremental
    registro[1] = idHabitacion
    numeroHabitacion = len(registroHabitaciones)+1 #autoincremental
    registro[2] = numeroHabitacion
    tipoHabitacion = input("Ingrese tipo de habitacion \n")
    registro[3] = tipoHabitacion
    valorHabitacion = input("Ingrese valor habitacion \n")
    registro[4] = valorHabitacion
    estadoHabitacion = False
    registro["reservado"] = estadoHabitacion
    
    registroHabitaciones.append(registro)
    print(f"""
        =================================
        Habitacion creada
        =================================
        ID: {idHabitacion}  
        Numero habitacion: {numeroHabitacion}
        Tipo habitacion: {tipoHabitacion}
        Valor habitacion: {valorHabitacion}
        =================================
        """)

#ELIMINAR UNA HABITACION
def eliminarHabitacion():
        idHabitacion = int(input("Ingrese la habitacion que quiere eliminar \n"))
        for habitacion in registroHabitaciones:
            if habitacion[1] == idHabitacion:
                registroHabitaciones.remove(habitacion)
                print("==============================")
                print("Habitacion eliminada")
                print("==============================")
                break
            else:
                print("Habitacion no encontrado")
                
#MODIFICAR UNA HABITACION                
def modificarHabitacion():
        encontrado: False
        idHabitacion = int(input("Ingrese la habitacion que quiere modificar \n"))

        for habitacion in registroHabitaciones:
            if habitacion[1] == idHabitacion:
                print("Habitacion encontrado")
                print("==============================")
                print("1.Tipo \n 2.Valor")
                eleccion = input("Seleccione quiere modificar??")
                if eleccion == "1":
                    tipo = input("Ingrese  el nuevo tipo de habitacion")
                    habitacion[3] = tipo
                    print(f"""
                            =================================
                            Habitacion modificada
                            =================================
                            ID: {habitacion[1]}  
                            Numero habitacion: {habitacion[2]}
                            Tipo habitacion: {habitacion[3]}
                            Valor habitacion: {habitacion[4]}
                            Estado habitacion: {habitacion["reservado"]}
                            =================================
                            """)
                if eleccion == "2":
                    valor = int(input("Ingrese nuevo valor de la habitacion"))
                    habitacion[4] = valor
                    print(f"""
                            =================================
                            Habitacion modificada
                            =================================
                            ID: {habitacion[1]}  
                            Numero habitacion: {habitacion[2]}
                            Tipo habitacion: {habitacion[3]}
                            Valor habitacion: {habitacion[4]}
                            Estado habitacion: {habitacion["reservado"]}
                            =================================
                            """)
                
            else:
                print("Habitacion no encontrado")
            encontrado = True
            break
        
        if not encontrado:
            # modificarHabitacion() # VER SI RESULTA
            print("No se encuentra el rut del cliente")  
            print("==============================")
            
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
        print("\n--- Administración de Habitaciones ---")
        print("Opcion 1:  Listar habitaciones")
        print("Opcion 2:  Registrar habitacion")
        print("Opcion 3: Modificar habitacion")
        print("Opcion 4:  Eliminar habitacion")
        print("Opcion 5: Volver al menu principal")

            
        opcion = int(input("ELija una opcion \n"))
        if opcion ==5:
            respuesta = input("Seguro quiere salir?? si/no \n")
            respuesta = respuesta.lower()
            
        menuHabitaciones.get(opcion)()
        
        