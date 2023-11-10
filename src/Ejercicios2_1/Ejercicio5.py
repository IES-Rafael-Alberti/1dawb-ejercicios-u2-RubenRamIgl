"""edad=int(input("Introduce tu edad: "))
ingresos=float(input("Introduce tus ingresos: "))

if(edad>16 and ingresos>=1000):
    print("Puedes tributar")
else:
    print("No puedes tributar")"""

def pedirEdad():
    edad=input("Introduce tu edad: ")
    salir=False
    while not salir:
        if(edad.isnumeric() and int(edad)>=0):
            salir=True
        else:
            print("Error, edad no válida")
            edad=input("Introduce tu edad: ")

    return int(edad)
        

def pedirIngresos():
    ingresos=input("Introduce tus ingresos: ")
    salir=False
    while not salir:
        if(ingresos.replace(".","").isnumeric()):
            salir=True
        else:
            print("Error, ingresos no válidos")
            ingresos=input("Introduce tus ingresos: ")

    return float(ingresos)
        

def tributa(edad,ingresos):
    if(edad>16 and ingresos>=1000):
        return True
    else:
        return False

def main():
    edad=pedirEdad()
    ingresos=pedirIngresos()

    if(tributa(edad,ingresos)):
        print("Puedes tributar")
    else:
        print("No puede tributar")

if (__name__ == "__main__"):
    main()