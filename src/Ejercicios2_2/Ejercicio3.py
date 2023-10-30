"""n=int(input("Introduce un número positivo: "))

cont=1

while(cont<=n):
    if(cont%2!=0):
        if(cont==n or cont==n-1):
         print(cont, end="")
        else:
         print(cont, end=",")
    cont+=1"""

def numeroPositivo():
    n=input("Introduce un número positivo: ")
    salir=False
    while not salir:
        if(n.isnumeric() and int(n)>=0):
            salir=True
        else:
            print("Error, número no válido")
    return int(n)

def impares(n):
    cont=1

    while(cont<=n):
        if(cont%2!=0):
            if(cont==n or cont==n-1):
                print(cont, end="")
            else:
                print(cont, end=",")
        cont+=1

def main():
    n=numeroPositivo()

    impares(n)

if (__name__ == "__main__"):
    main()