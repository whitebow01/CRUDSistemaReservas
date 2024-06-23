import menuAdmin

##MENU ADMIN - REGISTRO HABITACIONES    
registroHabitaciones = [{1:1, 2: "1", 3: "Individual",4:20000,"reservado":False},
                        {1:2, 2: "2", 3: "Doble", 4: 25000, "reservado":True},
                        {1:3, 2: "3", 3: "Suite", 4: 42000, "reservado":False},
                        {1:4, 2: "4", 3: "Individual", 4: 15000, "reservado":True},
                        {1:5, 2: "5", 3: "Doble", 4: 30000, "reservado":False}
                        ]
def vistaHabitaciones():
    for x in registroHabitaciones:
        print("==============================")
        print(f" ID: {x[1]} \n  N°Habitacion: {x[2]} \n Tipo:{x[3]} \n Valor:${[4]}, \n Etado:{x["reservado"]} ")
        print("==============================")
        
def registroHabitacion():
    registro = {1:"",2:"",3:"",4:"","reservado":""}
    idHabitacion = len(registroHabitaciones)+1 #autoincremental
    registro[1] = idHabitacion
    numeroHabitacion = len(registroHabitaciones)+1 #autoincremental
    registro[2] = numeroHabitacion
    tipoHabitacion = input("Ingrese tipo de habitacion")
    registro[3] = tipoHabitacion
    valorHabitacion = input("Ingrese valor habitacion")
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


def eliminarHabitacion():
        idHabitacion = input("Ingrese la habitacion que quiere eliminar \n")
        for habitacion in registroHabitaciones:
            if habitacion[1] == idHabitacion:
                registroHabitaciones.remove(habitacion)
                print("Habitacion eliminado")
                print("==============================")
                break
            else:
                print("Cliente no encontrado")
                
def modificarHabitacion():
        encontrado: False
        idHabitacion = input("Ingrese la habitacion que quiere eliminar \n")

        for habitacion in registroHabitaciones:
            if habitacion[1] == idHabitacion:
                print("Cliente encontrado")
                print("==============================")
                estado = input("Cambie estado de habitacion")
                habitacion[5] = estado
                print("Habitacion modificada")
                
            else:
                print("Habitacion no encontrado")
            encontrado = True
            break
        if not encontrado:
            modificarHabitacion() # VER SI RESULTA
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
        
        