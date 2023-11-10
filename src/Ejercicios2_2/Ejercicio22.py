def pedirNumeros():
    numeros=[]
    salir=False
    while not salir:
        n=input("Introduce un número (0 para salir): ")
        if(n=="0"):
            salir=True
        elif(n.isnumeric()):
            numeros.append(int(n))
        else:
            print("Error, número no válido")
    return numeros

def contarPares(numeros):
    cont=0
    for i in numeros:
        if(i%2==0):
            cont+=1
    print("Se introdujeron",cont,"números pares")

def contarImpares(numeros):
    cont=0
    for i in numeros:
        if(i%2!=0):
            cont+=1
    print("Se introdujeron",cont,"números impares")

def main():
    numeros=pedirNumeros()
    contarPares(numeros)
    contarImpares(numeros)

if (__name__ == "__main__"):
    main()