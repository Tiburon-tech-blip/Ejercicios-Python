'''Escribe un programa que intente sumar un número y una cadena. Si se produce un error
de tipo, captura la excepción TypeError y muestra un mensaje de error al usuario.'''

try:
    num = 5
    cadena = "Hola"
    resultado = num + cadena
except TypeError:
    print("Error: No se puede sumar un número y una cadena.")

