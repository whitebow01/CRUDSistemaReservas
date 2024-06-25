import CRUD.administracionClientes
import CRUD.administracionHabitaciones
import CRUD.administracionReservaciones
import CRUD.administracionTrabajadores

def default():
    print("Opcion fuera de rango") 
    return

def MenuAnterior():
    import time
    print("Saliendo al menú general...")
    time.sleep(2)  #3 segundos para ir al menu
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

    while True:
        print("\n═══ Menú Principal Administrador ═══")
        print("1. Administrar clientes")
        print("2. Administrar habitaciones")
        print("3. Administrar reservaciones")
        print("4. Volver al menu general")
        print("5. Salir del programa")
        
        try: ##validacion solo numeros
            opcion = int(input("ELija una opción \n"))
            menu.get(opcion, default)()
        except ValueError:
            print("Error. Por favor, ingrese solo numeros")
# get(opcion, default) busca el valor de la opcion dentro del diccionario menu
