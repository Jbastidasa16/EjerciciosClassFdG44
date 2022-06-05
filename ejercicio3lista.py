#realizar un programa que pida n cantidad de estudiantes
#pedir nombres, y ordenarlos tipo lista.

lista = []
cant_estu = int(input ("Digite la cantidad de estudiantes: "))
for i in range (cant_estu):
    nom_estu = str(input(f"Digite el nombre del estiduante {i+1}: "))
    lista.append(nom_estu)
lista.sort()
print(f"la lista de los estudiantes ordenados es: \n{lista}")
