import os,time

registroClientes = [{1:"15468545", 2:"Juan", 3: "Castro",4:"sss"}]

def registroCliente():
    registro = {1:"", 2:"",3:"", 4:""}
    rut = input("Ingrese su rut sin número verificador ni guion \n")
    registro[1] = rut
    nombre = input("Ingrese su nombre \n")
    registro[2] = nombre
    apellido = input("Ingrese su apellido \n")
    registro[3] = apellido
    contraseña = input("Ingrese contraseña \n")
    registro[4] = contraseña

    registroClientes.append(registro)

    print(f"Bienvenido, {nombre}, ahora puede iniciar sesion")

    print(f"Tus datos:  \n rut: {rut} \n nombre: {nombre}\n apellido:{apellido}\n contraseña: """)

