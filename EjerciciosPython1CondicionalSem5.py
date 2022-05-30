#Dadas dos palabras comparar si son iguales.
import time
p1 = input("Digite una palabra: ")
p2 = input ("Digite otra palabra: ")
if p1 == p2:
    print(f"Las palabras son iguales: {p1} {p2}")
    
    
else:
    cambio = p2.replace("a", "e")
    cambio = cambio.replace("i", "e")
    cambio = cambio.replace("o", "e")
    cambio = cambio.replace("u", "e")
    
    print("Lsa palabras no son iguales "+cambio)
time.sleep(10)

