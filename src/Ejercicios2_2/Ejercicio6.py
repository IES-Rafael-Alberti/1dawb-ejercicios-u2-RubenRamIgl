"""n=int(input("Introduce la altura del triángulo: "))

cont=1

for cont in range(1,n+1):
    print("*"*cont)"""

def altura():
    n=input("Introduce la altura del triágulo: ")
    salir=False
    while not salir:
        if(n.isnumeric() and int(n)>=0):
            salir=True
        else:
            print("Error, número no válido")
    return int(n)

def triángulo(n):
    cont=1

    for cont in range(1,n+1):
        print("*"*cont)

def main():
    n=altura()

    triángulo(n)

if (__name__ == "__main__"):
    main()