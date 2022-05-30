#crear un programa sume n numeros datos y diga cuales son pares y cuales imapar


par = 0
impar = 0
i = 1
cont = 0
n = int(input("Digite la cantidad de nuemros a ingresar: "))

for i in range(n):
    num = int(input(f"Digite el numero {i+1}: "))
    if (num % 2 == 0):
        par = par +1
        cont = cont + num
    else:
        impar = impar + 1
        cont = cont + num
    i += 1
cont = cont
print (f"La cantidad de numeros Pares son: {par}")
print (f"La cantidad de numeros Impares son: {impar}")
print (f"La suma total de los numeros es : {cont}")
