def pedirInversion():
    inversion=input("Introduce la cantidad que quiere invertir: ")
    salir=False
    while not salir:
        if(inversion.replace(".","").isnumeric() and int(inversion)>=0):
            salir=True
        else:
            print("Error, el valor introducido es incorrecto")
    return float(inversion)

def pedirInteres():
    interes=input("Introduce el interes anual en %: ")
    salir=False
    while not salir:
        if(interes.isnumeric() and int(interes)>=0):
            salir=True
        else:
            print("Error, el valor introducido es incorrecto")
    return int(interes)

def pedirAños():
    años=input("Introduce los años: ")
    salir=False
    while not salir:
        if(años.isnumeric() and int(años)>=0):
            salir=True
        else:
            print("Error, el valor introducido es incorrecto")
    return int(años)

def cantidadInversion(inversion,interes,años):
    for año in range(1, años+1):
        inversion*=1+interes/100
        print(f"Año {año}, Capital obtenido={inversion:.2f}")

def main():
    inversion=pedirInversion()
    interes=pedirInteres()
    años=pedirAños()

    cantidadInversion(inversion,interes,años)

if (__name__ == "__main__"):
    main()