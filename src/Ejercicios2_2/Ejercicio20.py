def pedirFrase():
    frase=input("Introduce una frase: ")
    return frase

def pedirLetra():
    letra=input("Introduce una letra: ")
    return letra

def contarLetra(frase,letra):
    contiene=False
    for i,caracter in enumerate(frase):
        if(caracter==letra):
            print(f"El carácter {letra} está en la posición {i}")
            contiene=True
    
    if not contiene:
        print("La frase no contiene la letra")

def main():
    frase=pedirFrase()
    letra=pedirLetra()

    contarLetra(frase,letra)

if (__name__ == "__main__"):
    main()