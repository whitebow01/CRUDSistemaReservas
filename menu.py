import registros
import login
import os

menuLogin={1:login.menuLogin,2:registros.registroCliente}


def default():
    print("Opcion fuera de rango")

respuesta="si"
while respuesta == "si":

    print("╔══════════════════════════════════════════╗")
    print("║ Bienvenido al menú                       ║")
    print("║                                          ║")
    print("║ Eliga su opción                          ║")
    print("║                                          ║")
    print("║                                          ║")
    print("║ Opción 1 > Iniciar sesión                ║")
    print("║                                          ║")
    print("║ Opción 2 > Registrarse                   ║")
    print("║                                          ║")
    print("║ Opción 5 > Salir                         ║")
    print("║                                          ║")
    print("╚══════════════════════════════════════════╝")
    
    opcion = int(input("Elija una opcion \n"))
    menuLogin.get(opcion,default)()                   
    
    respuesta = input("Desea hacer algo más? \n")
    respuesta = respuesta.lower()
    

os.system("cls")