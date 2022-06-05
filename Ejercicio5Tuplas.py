"""dada la tupla (True, 10, 'hola', 'Python', 'ciclo', True, False, True)
recorrerla si hay un valor booleano True debe agregar un  nuevo ítem al final,
si el valor es False debe eliminar la posición en donde se encuentra el valor.
Imprime el resultado"""

x = (True, 10, 'hola', 'Python', 'ciclo', True, False, True)
z = list(x)
for i in x:
    if True in x:
        z.append("newItem")
if False in x:
    z.remove(False)
x = tuple(z)
print(x)
