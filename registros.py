import os,time

##MENU GENERAL - REGISTRO TRABAJADOR 
registroTrabajadores = [{1:"15546854-5", 2:"Juan", 3: "Castro",4:"sss"}]

def registroTrabajador():
    registro = {1:"", 2:"",3:"", 4:""}
    rut = input("Ingrese su rut\n")
    registro[1] = rut
    nombre = input("Ingrese su nombre \n")
    registro[2] = nombre
    apellido = input("Ingrese su apellido \n")
    registro[3] = apellido
    contraseña = input("Ingrese contraseña \n")
    registro[4] = contraseña

    registroTrabajadores.append(registro)

    print(f"Bienvenido, {nombre}, ahora puede iniciar sesion")

    print(f"Tus datos:  \n rut: {rut} \n nombre: {nombre}\n apellido:{apellido}\n contraseña: """)


    ##MENU ADMIN - REGISTRO CLIENTE

registroClientes=[{1:"20326456-8",2:"Luis",3:"Molla"}]

def registroCliente():
    registro = {1:"",2:"",3:""}
    rutCliente = input("Ingresa rut del cliente")
    registro[1] = rutCliente
    nombreCliente = input("Ingresa el nombre del cliente")
    registro[2] = nombreCliente
    apellidoCliente = input("Ingrese apellido del cliente")
    registro[3] = apellidoCliente
    registroClientes.append(registro)
    
    print(f"Cliente {nombreCliente} ingresado correctamente")
