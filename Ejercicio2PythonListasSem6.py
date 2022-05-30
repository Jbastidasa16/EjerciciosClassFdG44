"""Dada una frase de 5 palabras separadas por espacio convertir a lista
y verificar si dentro se enuentra la palabra Hola, Si es así, insertar un nuevo
item que diga palabra ENCONTRADA; sino, insertar un item que diga NO ENCONTRADA
imprimir lista"""

frase = input("digite una frase de 5 palabras: ")
lis = frase.lower()
lis = lis.split(" ")
if "hola" in lis:
    lis.append("ENCONTRADA")
else:
    lis.append("NO ENCONTRADA")
print(lis)
