#Conversion de numeros arabigos a romanos
import time
print ("******************************Bienvenid@******************************")
n = input("""ingrese uno de los siguientes numeros arabigos a convertir a romano
                    1 - 5 - 10 - 50 - 100 - 500 - 1000:\n ->""")
if n == "1":
    ar = n.replace("1","I")
    print("\nEl numero en Romano es: ",ar)
elif n == "5":
    ar = n.replace("5","V")
    print ("\nElnumero en Romano es: ",ar)
elif n == "10":
    ar = n.replace("10","X")
    print ("\nElnumero en Romano es: ",ar)
elif n == "50":
    ar = n.replace("50","L")
    print ("\nElnumero en Romano es: ",ar)
elif n == "100":
    ar = n.replace("100","C")
    print ("\nElnumero en Romano es: ",ar)
elif n == "500":
    ar = n.replace("500","D")
    print ("\nElnumero en Romano es: ",ar)
elif n == "1000":
    ar = n.replace("1000","M")
    print ("\nElnumero en Romano es: ",ar)
print("\n***Fin del Programa Gracias Por Preferirnos***")

time.sleep(5)
exit()
