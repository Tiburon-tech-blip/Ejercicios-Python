'''Determinar si un número es par o impar'''

numero = int(input("Ingresa un número: "))
resultado = "par" if numero % 2 == 0 else "impar"
print(f"El número {numero} es {resultado}.")
