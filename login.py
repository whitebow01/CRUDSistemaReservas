import os,time
import registros
import crudSistemaReserva
def loginTrabajador():
    usuarioCorrecto = False
    contraseñaCorrecta = False
    listaTrabajadores = registros.registroTrabajadores
    #Esto llama al registro con los trabajadores

    while not usuarioCorrecto: #Bucle hasta que usuariocorrecto sea True
        rutTrabajador = input("Ingrese su RUT \n")
        for usuario in listaTrabajadores:
            if rutTrabajador == usuario[1]:
                usuarioCorrecto = True
                print("RUT correcto")
                break
        if not usuarioCorrecto:
            print("RUT incorrecto")

    while not contraseñaCorrecta: #Bucle hasta que contraseñacorrecta sea True
        passwordTrabajador = input("Ingresa tu contraseña \n")
        if passwordTrabajador == usuario[4]:
            contraseñaCorrecta = True
            print("Contraseña correcta")
            print(f"Bienvenido, ")
        else:
            print("Contraseña incorrecta")
    #MENU USUARIO LOGEADO       
    if usuarioCorrecto and contraseñaCorrecta == True:
        respuesta = "si" 

        crudSistemaReserva.menuAdmin() 
        #Si todo se cumple, entra al archivo crudSistemaReserva
        #y luego a la funcion menu admin que contiene:
            #Administracion clientes
            #Administracion trabajadores
            #Administracion habitaciones
