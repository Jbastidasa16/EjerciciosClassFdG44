"""Digitando una frase de 5 palabras separadas por espacio, convertirla en tupla
y luego verificar si dentro de ella se encuentra la palabra 'Hola'.
Si es así imprinmir el indice en donde se encuentra, sino arrojar un mensaje de
no encontrado. imprimir la tupla y el tipo de dato al final."""

x = input("Digite 5 pabras separadas por espacio: ")
x = x.lower()
z= x.split()
x = tuple(z)
#print(x)
if "hola" in z:
    y = z.index("hola")
    print (y)
else:
    print("Palabra No Encontrada")
print(x)
print(type(x))

