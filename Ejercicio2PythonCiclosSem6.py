#programa promedio estudiantes
import time
i = True

while i :
    print("***** Ingrese 3 notas de un estudiante *****")
    nota1 = float(input("Ingrese la 1 Nota del estudiante: "))
    nota2 = float(input("Ingrese la 2 Nota del estudiante: "))
    nota3 = float(input("Ingrese la 3 Nota del estudiante: "))

    promedio = (nota1 + nota2 + nota3)/3
    

    if (nota1 >= 1 and nota1 <=10):
        print("Notas validas\n")
    else:
        print("Notas invalidas")
        estudiante = input("\n¿Desea agregar nuevamente las notas del estudiante? Si/no: ")
        if (estudiante.lower() == "si"):
            i = True
        else:
            i = False
            print("***** Gracias por preferirnos *****")

    if (promedio >= 7 and promedio <= 10):
        print("¡Congratulation! Alumno Promocionado.")
        print(f"\nEl Promedio del estudiantes es {promedio}")
    elif (promedio >= 4 and promedio < 7):
        print("¡Congratulation! Alumno Regular.")
        print(f"\nEl Promedio del estudiantes es {promedio}")
    elif (promedio < 4):
        print("¡Sorry! Alumno Reprobado.")
        print(f"\nEl Promedio del estudiantes es {promedio}")
    

    estudiante = input("\n¿Desea continuar con otro Estudiante? Si/no: ")
    if (estudiante.lower() == "si"):
        i = True
    else:
        i = False
        print("***** Gracias por preferirnos *****")
        time.sleep(2)
        exit()
