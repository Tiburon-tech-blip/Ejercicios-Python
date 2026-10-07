'''Calcular el mayor de dos números ingresados por teclado usando un operador
ternario'''


numero1 = float(input("Ingresa el primer número: "))
numero2 = float(input("Ingresa el segundo número: "))

mayor = numero1 if numero1 > numero2 else numero2

print(f"El mayor es: {mayor}")
