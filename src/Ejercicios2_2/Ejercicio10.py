def pedirNumero():
    num=input("Introduce un número entero: ")
    salir=False
    while not salir:
        if(num.isnumeric() and int(num)>=0):
            salir=True
        else:
            print("Error, número no válido")
            num=input("Introduce un número entero: ")
    return int(num)

def esPrimo(num):
    for n in range(2, num):
        if(num%n==0):
            return False
    return True

def main():
    num=pedirNumero()

    if(esPrimo(num)):
        print("El número es primo")
    else:
        print("El número no es primo")

if (__name__ == "__main__"):
    main()