"""n=int(input("Introduce un número: "))

if(n%2==0):
    print("El número es par")
else:
    print("El número es impar")"""

def pedirNumero():
    return int(input("Introduce un número: "))

def parImpar(n):
    if(n%2==0):
        print("El número es par")
    else:
        print("El número es impar")
        

def main():
    n=pedirNumero()

    parImpar(n)

if (__name__ == "__main__"):
    main()