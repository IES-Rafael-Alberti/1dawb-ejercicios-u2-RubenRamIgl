def pedirDigitos():
    digitos=input("Introduce una cadena de dígitos: ")
    salir=False
    while not salir:
        if(digitos.isnumeric()):
            salir=True
        else:
            print("Error, número no válido")
    return digitos

def digitoMayor(digitos):
    mayor=max(digitos)
    return mayor

def main():
    digitos=pedirDigitos()
    print("El dígito mayor es",digitoMayor(digitos))
    

if (__name__ == "__main__"):
    main()