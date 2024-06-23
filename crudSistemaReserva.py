# import menuAdmin
# import random

# def default():
#     print("Opcion fuera de rango") 
#     return
    

# #CLIENTES
# def administracionClientes():
#     listaClientes = menuAdmin.registroClientes

#     def vistaClientes():
#         for x in listaClientes:
#             print("==============================")
#             print(f" Rut: {x[1]} \n  Nombre: {x[2]} \n Apellido:{x[3]}")
#             print("==============================")
            
#     #REGISTRAR CLIENTES DIRECTO AL MENU
            
#     def eliminarCliente():
#         rutCliente = input("Ingresa el rut a eliminar \n")
#         for cliente in listaClientes:
#             if cliente[1] == rutCliente:
#                 listaClientes.remove(cliente)
#                 print("Cliente eliminado")
#                 print("==============================")

#                 break
#             else:
#                 print("Cliente no encontrado")
#                 print("==============================")

    
#     def modificarCliente():
#         encontrado = False
        
#         rutCliente = input("Ingresa el rut del cliente")
#         for cliente in listaClientes:    
#             if cliente[1] == rutCliente:
                
#                 print("Cliente encontrado")
#                 print("==============================")

#                 print("1.Nombre \n 2.Apellido")
#                 eleccion = input("Seleccione cual quiere modificar??")
                
#                 if eleccion == "1":
#                     nombre = input("Ingrese nuevo nombre \n")
#                     cliente[2] = nombre
#                     print(f"Nombre cambiado a {nombre}")

#                 elif eleccion == "2":
#                     apellido = input("Ingrese nuevo apellido \n")
#                     cliente[3] = apellido
#                     print(f"Apellido cambiado a {apellido}")

#                 else:
#                     print("Eleccion incorrecta")
#                     print("==============================")
                    
#                 # encontrado = True
#                 break
        
#         if not encontrado:
#             print("No se encuentra el rut del cliente")    
#             print("====================================")

                
#     #DICCIONARIO CON MENU - ADMINISTRACION CLIENTES       
#     menuClientes = {1: vistaClientes, 
#                     2:menuAdmin.registroCliente, 
#                     3:modificarCliente,
#                     4:eliminarCliente, 
#                     5:menuAdmin
#                     }
    
#     respuesta = "si"
#     while respuesta =="si":
#         print("\n--- Administración de Clientes ---")
#         print("Opcion 1:  Listar clientes")
#         print("Opcion 2:  Registrar cliente")
#         print("Opcion 3: Modificar cliente")
#         print("Opcion 4:  Eliminar cliente")
#         print("Opcion 5: Volver al menu principal")
            
#         opcion = int(input("ELija una opcion \n"))
#         menuClientes.get(opcion,default)()
        
#         respuesta = input("Quiere hacer algo mas en menu cliente? si/no \n")
#         respuesta = respuesta.lower()

# # HABITACIONES
# def administracionHabitaciones():
#     listaHabitaciones = menuAdmin.registroHabitaciones

#     def vistaHabitaciones():
#         for x in listaHabitaciones:
#             print("==============================")
#             print(f" ID: {x[1]} \n  N°Habitacion: {x[2]} \n Tipo:{x[3]} \n Valor:${4}, \n Etado:{x["reservado"]} ")
#             print("==============================")
        
#     #REGISTRAR HABITACION DIRECTO AL MENU

#     def eliminarHabitacion():
#         idHabitacion = input("Ingrese la habitacion que quiere eliminar \n")
#         for habitacion in listaHabitaciones:
#             if habitacion[1] == idHabitacion:
#                 listaHabitaciones.remove(habitacion)
#                 print("Habitacion eliminado")
#                 print("==============================")
#                 break
#             else:
#                 print("Cliente no encontrado")

#     def modificarHabitacion():
#         encontrado: False
#         idHabitacion = input("Ingrese la habitacion que quiere eliminar \n")

#         for habitacion in listaHabitaciones:
#             if habitacion[1] == idHabitacion:
#                 print("Cliente encontrado")
#                 print("==============================")
#                 estado = input("Cambie estado de habitacion")
#                 habitacion[5] = estado
#                 print("Habitacion modificada")
                
#             else:
#                 print("Habitacion no encontrado")
#             encontrado = True
#             break
#         if not encontrado:
#             modificarHabitacion() # VER SI RESULTA
#             print("No se encuentra el rut del cliente")  
#             print("==============================")
#     #DICCIONARIO CON MENU - ADMINISTRACION HABITACIONESS        
#     menuHabitaciones = {1:vistaHabitaciones, 
#                         2:menuAdmin.registroHabitacion,
#                         3:modificarHabitacion,
#                         4:eliminarHabitacion,
#                         5:menuAdmin
#                         }
    
#     respuesta = "si"
#     while respuesta =="si":
#         print("\n--- Administración de Habitaciones ---")
#         print("Opcion 1:  Listar habitaciones")
#         print("Opcion 2:  Registrar habitacion")
#         print("Opcion 3: Modificar habitacion")
#         print("Opcion 4:  Eliminar habitacion")
#         print("Opcion 5: Volver al menu principal")

            
#         opcion = int(input("ELija una opcion \n"))
#         menuHabitaciones.get(opcion)()
        
#         respuesta = input("Administrará algo mas en habitaciones?? si/no \n")
#         respuesta = respuesta.lower()

# # RESERVACIONES
# def administracionReservaciones():
#     listaReservaciones = menuAdmin.registroReservaciones

#     # registros.registroReserva()
    
#     def vistaReservas():
#         for x in listaReservaciones:
#             print(f"ID:{x[1]} \n Cliente:{x[2]} \n Habitacion:{x[3]}")
            
#     menuReservaciones = {1:vistaReservas,
#                         2:menuAdmin.registroReserva,
#                         5:menuAdmin}
#     respuesta = "si"
#     while respuesta =="si":
#         print("\n--- Administración de Reservaciones ---")
#         print("Opcion 1:  Listar Reservaciones")
#         print("Opcion 2:  Registrar Reservacion")
#         # print("Opcion 3: Modificar Reservacion")
#         # print("Opcion 4:  Eliminar Reservacion")
#         print("Opcion 5: Volver al menu principal")
            
#         opcion = int(input("ELija una opcion \n"))
#         menuReservaciones.get(opcion)()
        
#         respuesta = input("Quiere hacer algo mas en menu de reservaciones? si/no \n")
#         respuesta = respuesta.lower()



# #MENU ADMIN
# def menuAdmin():
#     #DICCIONARIO CON MENU - MENU GENERAL ADMIN LOGEADO
#     menu ={1:administracionClientes, 
#         2:administracionHabitaciones,
#         3:administracionReservaciones,
#         # 4:exit
#         }

#     respuesta = "si"
#     while respuesta == "si":
#         print("\n--- Menú Principal Administrador---")
#         print("1. Administrar clientes")
#         print("2. Administrar habitaciones")
#         print("3. Administrar reservaciones")
#         print("4. Salir del programa")
        
        
#         opcion = int(input("ELija una opcion \n"))
#         menu.get(opcion, default)()
        
# # get(opcion, default) busca el valor de la opcion dentro del diccionario menu
        
#         respuesta = input("Quiere hacer algo mas en el menu general? si/no \n")
#         respuesta = respuesta.lower()
    