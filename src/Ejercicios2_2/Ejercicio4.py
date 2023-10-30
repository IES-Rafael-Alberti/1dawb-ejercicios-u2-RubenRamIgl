"""n=int(input("Introduce un número positivo: "))

cont=n

while(cont>=0):
    if(cont==0):
        print(cont, end="")
    else:
         print(cont, end=",")
    cont-=1"""

def numeroPositivo():
    n=input("Introduce un número positivo: ")
    salir=False
    while not salir:
        if(n.isnumeric() and int(n)>=0):
            salir=True
        else:
            print("Error, número no válido")
    return int(n)

def cuentaAtras(n):
    cont=n

    while(cont>=0):
        if(cont==0):
            print(cont, end="")
        else:
            print(cont, end=",")
        cont-=1

def main():
    n=numeroPositivo()

    cuentaAtras(n)

if (__name__ == "__main__"):
    main()