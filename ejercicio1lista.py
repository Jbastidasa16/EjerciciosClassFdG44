"""Escriba un programa que permita crear una lista de palabras, para ello,
el programa tiene que pedir un numero de posiciones y luego solicitar palabras
para crear la lista. Por ultimo, el programa tiene que escribir la lista."""

x = int(input("Digite la cantidad de palabras a insertar en la lista: "))
lista = []

for i in range(x):
    y = input(f"Escriba la {i+1} a ingresar en la lista: ")
    lista.insert(i,y)
print(lista)
