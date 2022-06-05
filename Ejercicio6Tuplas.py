"""Dada una lista de 10 numeros cualquiera Verificar por numero si es par
o impar. Si es par se va a una lista llamada par y si es impar a una lista
llamada impar al final se muestran ambas en forma de tupla"""

lista = [2, 5, 6, 4, 7, 8, 9, 10, 3, 1]
print(f"Los numeros de la lista a verificar son: \n{lista}")
par = []
impar = []
for i in lista:
    if i%2==0:
        par.append(i)
    else:
        if i%2!=0:
            impar.append(i)
par = tuple(par)
impar = tuple(impar)
print(f"\nLa lista con los numeros pares es: \n{par}")
print(f"\nLa lista con los numeros impares es: \n{impar}")
