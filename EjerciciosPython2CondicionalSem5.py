#Dados 3 numeros comparar
import time

print ("******Digite 3 numeros******")
num1 = int(input ("Digite un numero: "))
num2 = int(input ("Digite un numero: "))
num3 = int(input ("Digite un numero: "))

if num1 > num2 and num1 > num3:
    mayor = num1
elif num2 > num1 and num2 > num3:
    mayor = num2
elif num3 > num1 and num3 > num2:
    mayor = num3

if num1 < num2 and num1 < num3:
    menor = num1
elif num2 < num1 and num2 < num3:
    menor = num2
elif num3 < num1 and num3 < num2:
    menor = num3
print ("EL NUMERO MENOR ES: ",menor)
print ("EL NUMERO MAYOR ES: ",mayor)

n1 = str(num1)
n2 = str(num2)
n3 = str(num3)
print(len(n1))
print(len(n2))
print(len(n3))
time.sleep(10)
