def pedirNumeros():
    numeros=[]
    salir=False
    while not salir:
        n=input("Introduce un número (-1 para salir): ")
        if(n.isnumeric()):
            numeros.append(int(n))
        elif(n=="-1"):
            salir=True
        else:
            print("Error, número no válido")
    return numeros
        
def sumarNumeros(numeros):
    suma=sum(numeros)
    print("La suma de los números positivos es:",suma)

def contarPares(numeros):
    cont=0
    for i in numeros:
        if(i%2==0):
            cont+=1
    print("Se introdujeron",cont,"números pares")

def main():
    numeros=pedirNumeros()
    sumarNumeros(numeros)
    contarPares(numeros)

if (__name__ == "__main__"):
    main()