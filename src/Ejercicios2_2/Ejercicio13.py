def pedirFrase():
    frase=input("Introduce una palabra: ")
    return frase

def mostrarEco(palabra):
    palabras=palabra.split(" ")
    ultima=palabras[-1]
    eco=""
    for i in range(2):
        eco+=ultima+" "
    return eco

def main():
    while True:
        frase=pedirFrase()
        if(frase.lower()=="salir"):
            print("Saliste del programa")
            break
        else:
            print(frase+" "+mostrarEco(frase))

if (__name__ == "__main__"):
    main()