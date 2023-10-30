def pedirEdad():
    salir=False
    while not salir:
        entrada=input("Introduzca su edad: ")

        if(entrada.isnumeric() and 0<int(entrada)<=25):
            salir = True
        else:
            print("***Error*** edad introducida no válida.")
    
    edad = int(entrada)

    return edad

def mayorEdad(edad):
    if(edad>=18):
        return True
    else:
        return False
    
def main():
    edad = pedirEdad()

    if(mayorEdad(edad)):
        print("Eres mayor de edad.")
    else:
        print("No eres mayor de edad.")


if (__name__ == "__main__"):
    main()