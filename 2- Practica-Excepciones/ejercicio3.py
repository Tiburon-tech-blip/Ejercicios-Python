'''Escribe un programa que intente acceder a una clave que no existe en un
diccionario. Si se produce una excepción KeyError, captura la excepción y muestra'''
try:
    diccionario = {"a": 1, "b": 2, "c": 3}
    valor = diccionario["d"]
except KeyError:
    print("Error: La clave 'd' no existe en el diccionario.")
    