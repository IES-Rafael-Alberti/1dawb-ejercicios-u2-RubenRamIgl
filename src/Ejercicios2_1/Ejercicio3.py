n1=float(input("Introduce un número: "))
n2=float(input("Introduce el número por el que vas a dividir: "))

if(n2==0):
    print("Error, el número no puede ser dividido por 0")
else:
    print(str(n1)+"/"+str(n2),"=",n1/n2)