x = []
lista = int(input("Digite la cantidad de palabras a agregar: "))
for i in range(lista):
    palabras = (input(f"Digite la palabra {i}: "))
    x.insert(0,palabras)
print(x)

palabra = str(input("Digite la palabra a Buscar para Borrarla"))
if palabra in x:
    x.remove(palabra)
    print(x)
