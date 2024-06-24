import CRUD.administracionClientes
import CRUD.administracionHabitaciones
import CRUD.administracionReservaciones
import CRUD.administracionTrabajadores

def default():
    print("Opcion fuera de rango") 
    return

def MenuAnterior():
    import menuGeneral
    menuGeneral.menuGeneralInicio()

#MENU ADMIN
def menuAdministrador():

    #DICCIONARIO CON MENU - MENU GENERAL ADMIN LOGEADO
    menu ={1:CRUD.administracionClientes.menuCliente, 
        2:CRUD.administracionHabitaciones.menuHabitacion,
        3:CRUD.administracionReservaciones.menuReserva,
        4:MenuAnterior,
        5:exit
        }

    respuesta = "si"
    while respuesta == "si":
        print("\n--- Menú Principal Administrador---")
        print("1. Administrar clientes")
        print("2. Administrar habitaciones")
        print("3. Administrar reservaciones")
        print("4. Volver al menu general")
        print("5. Salir del programa")
        
        try:
            opcion = int(input("ELija una opcion \n"))
        except ValueError:
            print("Error. Por favor, ingrese solo numeros")
        
        menu.get(opcion, default)()
        
# get(opcion, default) busca el valor de la opcion dentro del diccionario menu
        
        respuesta = input("Quiere hacer algo mas en el menu general? si/no \n")
        respuesta = respuesta.lower()
    