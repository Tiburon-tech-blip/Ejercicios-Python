'''Calcular el promedio de una lista de números usando args y un operador ternario'''


def calcular_promedio(*numeros):          # La función recibe una lista de números como argumentos. El operador ternario se utiliza para determinar si la lista está vacía o no, devolviendo el promedio o 0 en caso de que esté vacía.
	return sum(numeros) / len(numeros) if numeros else 0


lista_numeros = [8, 7, 9, 10]
promedio = calcular_promedio(*lista_numeros)
print(f"El promedio es: {promedio}")
