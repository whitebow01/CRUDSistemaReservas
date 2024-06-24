import CRUD.administracionTrabajadores
import login


menuLogin={1:login.loginTrabajador,
        2:CRUD.administracionTrabajadores.registroTrabajador,
        3:exit
        }

def default():
    print("Opcion fuera de rango")
    return


respuesta="si"

while respuesta == "si":

    print("╔════════════════════════════════════════════════╗")
    print("║ Bienvenido al menú general                     ║")
    print("║                                                ║")
    print("║ Eliga su opción:                               ║")
    print("║                                                ║")
    print("║ Opción 1 > Iniciar sesión como administrador   ║")
    print("║                                                ║")
    print("║ Opción 2 > Registrar administrador             ║")
    print("║                                                ║")
    print("║ Opción 3 > Salir                               ║")
    print("║                                                ║")
    print("╚════════════════════════════════════════════════╝")
    
    
    opcion = int(input("Elija una opcion\n"))
    menuLogin.get(opcion,default)()                   
    if opcion == 3:
        break
    respuesta = input("Desea hacer algo más?: si/no \n")
    respuesta = respuesta.lower()