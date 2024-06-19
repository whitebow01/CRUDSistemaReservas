import os,time
import registros
def menuLogin():
    usuarioCorrecto = False
    contraseñaCorrecta = False
    while not usuarioCorrecto or not contraseñaCorrecta:
        login_name = input("Ingrese su rut \n")
        for usuario in registros.registroClientes:
            if login_name == usuario[1]:
                usuarioCorrecto = True
                print("Nombre de usuario correcto")
                login_password = input("Ingresa tu contraseña \n")
                if login_password == usuario[4]:
                    contraseñaCorrecta = True
                    print("Contraseña correcta")
                    print(f"Bienvenido, usuario {login_name}")
                else:
                    print("Contraseña incorrecta")
                    usuarioCorrecto = False  # Reiniciar si la contraseña es incorrecta
        if not usuarioCorrecto:
            print("Nombre de usuario incorrecto")
        
        
        
        # userBan=False
        # acceso=False
        # user=int(input("Ingrese su rut sin número verificador ni guíon \n")) 
        # password=input("Ingrese su contraseña: \n")
        # for x in registros.registroClientes:
        #     clienteBan=user in x 
        #     aux=x             #busca si clave existe en la lista
        #     if(clienteBan):
        #         print("Nombre correcto")
        #         break
        # if(clienteBan):
        #     clave=x[user]
        #     if(clave==password):
        #         print(f"Bienvenido, {registros.nombre}, clave correcta")
        #     acceso=True
        #     break
        # else:
        #     print("El usuario o la clave son incorrecto")  