#Dado un correo comparar si es igual y dar inicio else inicio fallido

correo = "juan2022@wipi.net"
email = str(input("Digite su Usuario @wipi.net: "))
if correo == email.lower():
    print("Inicio de sesion exitoso")
else:
    print("Email invalido")
