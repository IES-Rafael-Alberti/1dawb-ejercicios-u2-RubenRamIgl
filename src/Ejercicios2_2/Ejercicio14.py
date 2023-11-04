def pedirNumeros():
    n=input("Introduce un número(0 para salir): ")
    salir=False
    while not salir:
        if(n.isnumeric() and int(n)>=0):
            return int(n)
        elif(n==0):
            salir=True
        else:
            n==0
            print("Error, número no válido")
            n=input("Introduce un número(0 para salir): ")
        
def sumarNumeros():
    suma=0
    while True:
        n=pedirNumeros()
        if n!=0:
            suma+=n
        else:
            print("La suma de los números es:", suma)
            break

def main():
    sumarNumeros()

if (__name__ == "__main__"):
    main()