##MENU GENERAL - REGISTRO TRABAJADOR 
import re


registroTrabajadores = [{1:"555", 2:"Juan", 3: "Castro",4:"sss"}]
def validar_rut(cadena):
                                                # Definir el patrón de la expresión regular

    patron = re.compile(r'^\d{8}-[\dk]$')       #^ indica el inicio del patron #\d{8} indica que deben haber exactamente 8 dígitos (puede modificar si quiere)
                                                #- debe haber guion            #d|k verifica si hay digito o una letra k, si no lo hay no valida el rut
                                                    
                                                #el "re." es un modulo de expresiones regulares que entrega herramientas para trabajar
                                                #con expresiones regulares para buscar o manipular un texto con un patron definido.

#el "compile" es una función en el módulo "re" de Python que se utiliza para
#crear un objeto de expresión regular a partir de un patrón de texto (como el rut) 
                                             

    if patron.match(cadena):                    #Verificar si la cadena cumple con el patrón asignado en este caso el del rut.
        return True                             #En este caso el patron del rut (8 numeros guíon y si tiene o no la k)
    else:
        return False

def registroTrabajador():
    registro = {1:"", 2:"",3:"", 4:""}
    rutTrabajador = input("Ingrese su rut\n")
    if validar_rut(rutTrabajador):
        registro[1] = rutTrabajador
    else:
        print("El rut ingresado no es valido, intente nuevamente")
    
    nombreTrabajador = input("Ingrese su nombre \n")
    registro[2] = nombreTrabajador
    apellidoTrabajador = input("Ingrese su apellido \n")
    registro[3] = apellidoTrabajador
    contraseñaTrabajador = input("Ingrese contraseña \n")
    registro[4] = contraseñaTrabajador

    registroTrabajadores.append(registro)

    print("=============================================================")
    print(f"Bienvenido, {nombreTrabajador}, ahora puede iniciar sesion")
    print(f"""
            =================================
            Tus datos:
            =================================
            RUT: {rutTrabajador}
            Nombre cliente: {nombreTrabajador}
            Apellido cliente: {apellidoTrabajador}
            =================================
            """)
    
