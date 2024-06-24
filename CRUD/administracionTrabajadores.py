##MENU GENERAL - REGISTRO TRABAJADOR 
import re


# registroTrabajadores = [{1:555,2:"k", 3:"Juan", 4: "Castro",5:"sss"}]
registroTrabajadores = [{1:"555", 2:"Juan", 3: "Castro",4:"sss"}]


def registroTrabajador():
    registro = {1:"", 2:"",3:"", 4:""}
    while True:
        try:
            rutTrabajador = int(input("Ingresa su rut sin guión ni dígito verificador \n"))
            break
        except ValueError:
            print("Error. No puede ingresar letras, solo numeros ni puntos")
    digito = input("Ingrese digito verificador \n")
    
    rut = str(rutTrabajador)+"-"+digito
    registro[1] = rut
    
    nombreTrabajador = input("Ingrese su nombre \n")
    registro[2] = nombreTrabajador
    apellidoTrabajador = input("Ingrese su apellido \n")
    registro[3] = apellidoTrabajador

    contraseñaTrabajador = input("Ingrese contraseña \n")
    registro[4] = contraseñaTrabajador

    #guarda un registro en el total de registros
    registroTrabajadores.append(registro)
    
    print("=============================================================")
    print(f"Bienvenido, {nombreTrabajador}, ahora puede iniciar sesion")
    print(f"""
            =================================
            Tus datos:
            =================================
            RUT: {rutTrabajador}-{digito}
            Nombre cliente: {nombreTrabajador}
            Apellido cliente: {apellidoTrabajador}
            =================================
            """)
    
    import time
    time.sleep(3)