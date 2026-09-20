'''Dados un conjunto, A, escribe un programa en Python que imprima si el conjunto es
un subconjunto de otro conjunto, B'''

A = {1, 2, 3, 4}
B = {1, 2, 3, 4, 5, 6}

if A.issubset(B):
    print("A es un subconjunto de B")
else:
    print("A no es un subconjunto de B")

