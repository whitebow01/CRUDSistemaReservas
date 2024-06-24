##MENU GENERAL - REGISTRO TRABAJADOR 
import re


registroTrabajadores = [{1:"555",2:"k", 3:"Juan", 4: "Castro",5:"sss"}]


def registroTrabajador():
    registro = {1:"", 2:"",3:"", 4:""}
    # rutTrabajador = input("Ingresa su rut")
    # registro[1] = rutTrabajador
    try:
        rutTrabajador = int(input("Ingresa su rut sin guion ni digito verificador"))
        registro[1] = rutTrabajador
    except ValueError:
        print("Error. No ingrese su numero verificador, solo numeros")
    digito = input("Ingrese digito verificador")
    registro[2] = digito
    # print(f"{rutTrabajador}-{digito}")
    nombreTrabajador = input("Ingrese su nombre \n")
    registro[3] = nombreTrabajador
    apellidoTrabajador = input("Ingrese su apellido \n")
    registro[4] = apellidoTrabajador

    contraseñaTrabajador = input("Ingrese contraseña \n")
    registro[5] = contraseñaTrabajador

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
    
