#Tabla de multiplicar en formato tabla
for i in range(2,11):
    for j in range(1,11):
      print ("{:>5}".format(j*i), end=" ")
      j+=1
    i+=1
    print()
