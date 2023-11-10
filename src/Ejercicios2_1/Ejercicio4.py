"""n=int(input("Introduce un número: "))

if(n%2==0):
    print("El número es par")
else:
    print("El número es impar")"""

def pedirNumero():
    n=int(input("Introduce un número: "))
    return n

def parImpar(n):
    if(n%2==0):
        return True
    else:
        return False
        

def main():
    n=pedirNumero()

    if(parImpar(n)):
        print("El número es par")
    else:
        print("El número es impar")

if (__name__ == "__main__"):
    main()