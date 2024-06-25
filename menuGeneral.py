import CRUD.administracionTrabajadores
import login

def default():
    print("Opción fuera de rango")
    return

def menuGeneralInicio():
    #MENU QUE APARECERA EN LOGIN
    menuLogin={1:login.loginTrabajador,
            2:CRUD.administracionTrabajadores.registroTrabajador,
            3:exit
            }
    
    respuesta="si"
    while respuesta == "si":
        print("╔════════════════════════════════════════════════╗")
        print("║ Bienvenido al menú general                     ║")
        print("║                                                ║")
        print("║ Eliga su opción                                ║")
        print("║                                                ║")
        print("║ Opción 1 > Iniciar sesión como administrador   ║")
        print("║                                                ║")
        print("║ Opción 2 > Registrar administrador             ║")
        print("║                                                ║")
        print("║ Opción 3 > Salir                               ║")
        print("║                                                ║")
        print("╚════════════════════════════════════════════════╝")
        
        #validacion solo numeros
        try:
            opcion = int(input("Elija una opción\n"))
            menuLogin.get(opcion,default)()   
        except ValueError:
            print("Error. Por favor, ingrese solo numeros")
            import time
            time.sleep(2)
        #validacion si o no
        while respuesta not in ["si", "no"]: 
            print("Error, debe responder si o no")    
            respuesta = input("Desea hacer algo más?: si/no \n")
            respuesta = respuesta.lower()
                    
menuGeneralInicio()