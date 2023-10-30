"""n1=float(input("Introduce un número: "))
n2=float(input("Introduce el número por el que vas a dividir: "))

if(n2==0):
    print("Error, el número no puede ser dividido por 0")
else:
    print(str(n1)+"/"+str(n2),"=",n1/n2)"""

def pedirNumero():
    n1=input("Introduce un número: ")
    salir=False

    while not salir:
        if(n1.isnumeric()):
            salir=True
        else:
            print("Error, debes introducir un número")

    return float(n1)
    
def pedirDivisor():
    n2=input("Introduce el número por el que vas a dividir: ")
    salir=False

    while not salir:
        if(n2.isnumeric):
            salir=True
        else:
            print("Error, debes introducir un número")

    return float(n2)

def division(n1:float,n2:float):
    if n2!=0:
        resultado=n1/n2
        print(f"{n1}/{n2}={resultado:.2f}")
    else:
        print("Error, el número no puede ser dividido entre 0")

def main():
    n1=pedirNumero()
    n2=pedirDivisor()
    
    division(n1,n2)

if (__name__ == "__main__"):
    main()