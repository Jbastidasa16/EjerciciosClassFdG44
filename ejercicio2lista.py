"""Escriba un programa que permita recibir una frase,
luego crear una lista separando la frase donde haya espacion y que,
a continuación, pida una palabra y diga cuantas veces aparece esa palabra en la
lista. Sino aparece arrojar un mensaje por pantalla diciendo que no encontrada"""


frase = str(input("digite la frase: "))
x = frase.split()
print(x,"\n")
palabra = input("Digite la palabra a buscar: ")
cont = 0

for i in x:
    if palabra == i:
        cont += 1
if cont == 0:
    print("No se encuentra")
else:
    print(f"La palabra se repite {cont} veces en la lista")

