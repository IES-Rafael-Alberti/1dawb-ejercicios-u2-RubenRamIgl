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
    return suma
    

def contarPares(numeros):
    cont=0
    for i in numeros:
        if(i%2==0):
            cont+=1
    return cont

def main():
    numeros=pedirNumeros()
    print("La suma de los números positivos es:",sumarNumeros(numeros))
    print("Se introdujeron",contarPares(numeros),"números pares")
    

if (__name__ == "__main__"):
    main()