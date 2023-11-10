def pedirNumeros():
    numeros=[]
    while True:
        numero=int(input("Introduce un número (0 para salir): "))
        if numero==0:
            break
        numeros.append(numero)
    return numeros

def esPrimo(numero):
    for n in range(2, numero):
        if(numero%n==0):
            return False
    return True

def contarPrimos(numeros):
    cantidadPrimos=0
    for numero in numeros:
        if(esPrimo(numero)):
            cantidadPrimos+=1
    return cantidadPrimos

def main():
    numeros=pedirNumeros()
    cantidad_primos =contarPrimos(numeros)
    print("Cantidad de números primos es:",cantidad_primos)

if(__name__ == "__main__"):
    main()
