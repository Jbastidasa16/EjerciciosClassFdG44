#dado n cantidad de empleados digitar la edad si son mayores de 65 imprimir por pantalla

i = 0
mayor = 0

print("***** Agregar la edad de los empleados de una empresa *****")
emp = int(input("Digite la cantidad de empleados: "))

while i in range(emp):
    edad = int(input(f"Digite la edad del empleado {i+1}: "))
    if (edad >= 65):
        mayor = mayor + 1
    else:
        mayor = 0
    i = i + 1
mayor = mayor

print(f"Existen trabajadores mayores de 65 años en un numero de: {mayor}")
