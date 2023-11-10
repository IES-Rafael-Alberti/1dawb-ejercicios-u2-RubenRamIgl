def pedirNumeros():
    numeros = []
    salir=False
    while not salir:
        n=input("Introduce un número (0 para salir): ")
        if(n.isnumeric()):
            n=int(n)
            if(n==0):
                salir=True
            elif(n>0):
                numeros.append(n)
            else:
                print("Error, número no válido")
        else:
            print("Error, número no válido")
    return numeros

def numeroMayor(numeros):
    mayor=max(numeros)
    return mayor

def main():
    n=pedirNumeros()
    print("El número mayor es",numeroMayor(n))
    

if (__name__ == "__main__"):
    main()