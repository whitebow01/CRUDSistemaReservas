import registros
import login
import os

menuLogin={1:login.loginTrabajador,2:registros.registroTrabajador,3:exit}

def default():
    print("Opcion fuera de rango")
    return


respuesta="si"

while respuesta == "si":

    print("╔══════════════════════════════════════════╗")
    print("║ Bienvenido al menú                       ║")
    print("║                                          ║")
    print("║ Eliga su opción                          ║")
    print("║                                          ║")
    print("║ Opción 1 > Iniciar sesión                ║")
    print("║                                          ║")
    print("║ Opción 2 > Registrar                     ║")
    print("║                                          ║")
    print("║ Opción 3 > Salir                         ║")
    print("║                                          ║")
    print("╚══════════════════════════════════════════╝")
    
    opcion = int(input("Elija una opcion\n"))
    menuLogin.get(opcion,default)()                   
    if opcion == 3:
        break
    respuesta = input("Desea hacer algo más?: \n")
    respuesta = respuesta.lower()
    

os.system("cls")