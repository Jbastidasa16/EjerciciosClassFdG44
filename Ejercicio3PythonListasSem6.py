"""Dadas 2 listas con 5 entradas cada una, verificar cada entrada
si es un entero alamacenarlo en una nueva lista llamada a;
si es una cadena lo almacene en una nueva lista llamada b,
imprimir por pantalla"""

lista1 = ["Bus", 540, 620, 330, "Mundo"]
lista2 = ["Carro", "Moto", "Animal", 450, 510]
a = []
b = []

for i in range (5):

    if type(lista1[i]) == (int):
        a.append(lista1[i])
    elif type(lista1[i]) == (str):
        b.append(lista1[i])

    if type(lista2[i]) == (int):
        a.append(lista2[i])
    elif type(lista2[i]) == (str):
        b.append(lista2[i])

print(lista1)
print(lista2)
print(" ")
print(a)
print(b)
