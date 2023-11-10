"""edad=int(input("Introduce la edad del cliente: "))

if(edad<4):
    precio=0
elif(edad>=4 and edad<=18):
    precio=5
else:
    precio=10

print("El precio de la entrada es",precio)"""

def pedirEdad():
    edad=input("Introduce la edad del cliente: ")
    salir=False
    while not salir:
        if(edad.isnumeric and int(edad)>=0):
            salir=True
        else:
            print("Introduce una edad correcta")

    return int(edad)

def definirPrecio(edad):
    if(edad<4):
        precio=0
    elif(edad>=4 and edad<=18):
        precio=5
    else:
        precio=10

    return precio

def main():
    edad=pedirEdad()

    print("El precio de la entrada es",definirPrecio(edad))

if (__name__ == "__main__"):
    main()