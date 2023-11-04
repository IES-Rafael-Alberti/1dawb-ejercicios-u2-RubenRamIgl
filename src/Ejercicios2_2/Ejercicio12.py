def pedirFrase():
    frase=input("Introduce una frase: ")
    return frase

def pedirLetra():
    letra=input("Introduce una letra: ")
    return letra

def contarLetra(frase,letra):
    cont=0
    for i in frase:
        if(i==letra):
            cont+=1
    return cont

def main():
    frase=pedirFrase()
    letra=pedirLetra()

    print("El número de veces que aparece",letra,"es",contarLetra(frase,letra))

if (__name__ == "__main__"):
    main()