##MENU GENERAL - REGISTRO TRABAJADOR 
registroTrabajadores = [{1:"555", 2:"Juan", 3: "Castro",4:"sss"}]

def registroTrabajador():
    registro = {1:"", 2:"",3:"", 4:""}
    rutTrabajador = input("Ingrese su rut\n")
    registro[1] = rutTrabajador
    nombreTrabajador = input("Ingrese su nombre \n")
    registro[2] = nombreTrabajador
    apellidoTrabajador = input("Ingrese su apellido \n")
    registro[3] = apellidoTrabajador
    contraseñaTrabajador = input("Ingrese contraseña \n")
    registro[4] = contraseñaTrabajador

    registroTrabajadores.append(registro)

    print(f"Bienvenido, {nombreTrabajador}, ahora puede iniciar sesion")

    print(f"Tus datos:  \n rut: {rutTrabajador} \n nombre: {nombreTrabajador}\n apellido:{apellidoTrabajador}\n contraseña: """)

