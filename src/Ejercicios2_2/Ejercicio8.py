def altura():
    n=input("Introduce la altura del triágulo: ")
    salir=False
    while not salir:
        if(n.isnumeric() and int(n)>=0):
            salir=True
        else:
            print("Error, número no válido")
    return int(n)

def triangulo(n):
    for i in range(1, n + 1):
        for j in range(2 * i - 1, 0, -2):
            print(j, end=" ")
        print()
        

def main():
    n=altura()

    triangulo(n)

if (__name__ == "__main__"):
    main()