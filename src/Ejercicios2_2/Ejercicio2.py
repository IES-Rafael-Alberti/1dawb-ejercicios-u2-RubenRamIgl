"""edad=int(input("Introduce tu edad: "))

cont=1

for i in range(cont,edad+1):
    print(cont,end=" ")
    cont+=1"""

def pedirEdad():
    edad=input("Introduce tu edad: ")
    salir=False
    while not salir:
        if(edad.isnumeric()):
            salir=True
        else:
            print("Error, edad no válida")

    return int(edad)

def mostrarNúmeros(edad):
    cont=1

    for i in range(cont,edad+1):
        print(cont,end=" ")
        cont+=1

def main():
    edad=pedirEdad()

    mostrarNúmeros(edad)

if (__name__ == "__main__"):
    main()