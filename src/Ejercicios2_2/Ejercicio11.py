def pedirPalabra():
    palabra=input("Introduce una palabra: ")
    return palabra

def mostrarReves(palabra):
    reves=""
    for letra in palabra:
        reves=letra+reves
    return reves

def main():
    palabra=pedirPalabra()
    reves=mostrarReves(palabra)

    print(reves)

if (__name__ == "__main__"):
    main()