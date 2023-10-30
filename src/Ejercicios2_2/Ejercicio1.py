"""palabra=input("Introduce una palabra: ")

cont=0

for i in range(cont,10):
    print(palabra)
    cont+=1"""

def pedirPalabra():
    palabra=input("Introduce una palabra: ")
    return palabra

def imprimirPalabra(palabra):
    cont=0

    for i in range(cont,10):
        print(palabra)
        cont+=1

def main():
    palabra=pedirPalabra()

    imprimirPalabra(palabra)

if (__name__ == "__main__"):
    main()