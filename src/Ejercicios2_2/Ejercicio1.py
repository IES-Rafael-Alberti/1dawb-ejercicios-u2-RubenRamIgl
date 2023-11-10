"""palabra=input("Introduce una palabra: ")

cont=0

for i in range(cont,10):
    print(palabra)
    cont+=1"""

def pedirPalabra():
    palabra=input("Introduce una palabra: ")
    return palabra

def imprimirPalabra(palabra):
    resultado=""

    for i in range(10):
        resultado+=palabra+" "

    return resultado

def main():
    palabra=pedirPalabra()

    resultado=imprimirPalabra(palabra)
    print(resultado)

if (__name__ == "__main__"):
    main()