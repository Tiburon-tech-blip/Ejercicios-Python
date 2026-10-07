''' Dados dos conjuntos, A y B, escribe un programa en Python que imprima el
conjunto de los elementos que se encuentran en A o en B, pero no en ambos. '''

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

C = A ^ B
print(C)
