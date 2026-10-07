'''Imprimir un mensaje de error si no se pasan suficientes argumentos'''

def validar_argumentos(cantidad_minima): 
	def decorador(funcion): 
		def envoltura(*args, **kwargs): 
			if len(args) < cantidad_minima: 
				print(f"Error: se necesitan al menos {cantidad_minima} argumentos.") 
				return 
			return funcion(*args, **kwargs) 
		return envoltura 
	return decorador 

@validar_argumentos(2) 
def buscar_palabra(palabra, *lista): 
	return "La palabra está en la lista." if palabra in lista else "La palabra NO está en la lista." 

print(buscar_palabra("hola"))

palabras = ["hola", "chau", "adiós"]
print(buscar_palabra("hola", *palabras))
