def pedirFrase():
    frase=input("Introduce una frase: ")
    salir=False
    while not salir:
        if(frase==""):
            print("Frase vacía")
            frase=input("Introduce una frase: ")
        else:
            salir=True
    return frase

def palabraLarga(frase):
    listaFrase=frase.split(" ")
    palabraLarga=listaFrase[0]
    longitud=len(palabraLarga)

    for palabra in listaFrase:
        if(len(palabra)>longitud):
            palabraLarga=palabra
            longitud=len(palabra)

    return palabraLarga

def contarLetras(palabra):
    TotalLetras=len(palabra)
    return TotalLetras

def main():
    frase=pedirFrase()
    palabra=palabraLarga(frase)
    cantidadLetras=contarLetras(palabra)

    print("La palabra mas larga es: "+palabra+" y contiene "+str(cantidadLetras)+" letras")

if (__name__ == "__main__"):
    main()