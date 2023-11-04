def pedirNumeros():
    n=input("Introduce un número (0 para salir): ")
    salir=False
    while not salir:
        if (n.isnumeric()):
            if(int(n)==0):
                salir=True
            return n
        else:
            if(int(n)<0):
                n=0
                n = input("Introduce un número (0 para salir):")
            else:
                print("Error, número no válido")
                n = input("Introduce un número (0 para salir):")


        
        
def sumarNumeros():
    suma=0
    while True:
        n=pedirNumeros()
        if n!=0:
            suma+=n
        else:
            print("La suma de los números positivoses:", suma)
            break

def main():
    sumarNumeros()

if (__name__ == "__main__"):
    main()