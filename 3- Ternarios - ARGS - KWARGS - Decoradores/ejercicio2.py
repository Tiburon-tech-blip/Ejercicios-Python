'''Buscar una palabra en una lista ingresada por teclado usando args y un operador
ternario'''

def buscar_palabra(palabra, *lista):             # La función recibe una palabra y una lista de palabras como argumentos. El operador ternario se utiliza para determinar si la palabra está en la lista o no, devolviendo un mensaje correspondiente.
	return "La palabra está en la lista." if palabra in lista else "La palabra no está en la lista."


palabras = input("Ingresa las palabras separadas por comas: ").split(",")  # Ingreso palabras y las tranformo en una lista
palabras = [palabra.strip() for palabra in palabras]                       # Recorro la lista para quitar los espacios en blanco de cada palabra y guardarlos en una nueva lista
palabra_buscada = input("¿Qué palabra deseas buscar? ").strip()            # solicito la palabra a buscar y quito los espacios en blanco al inicio y al final

print(buscar_palabra(palabra_buscada, *palabras))                          # Imprimo el resultado de la búsqueda
