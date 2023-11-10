def pedirContraseña():
    contraseña=input("Introduce la contraseña: ")
    return contraseña

def validarContraseña(contraseña):
    validar=input("Introduce de nuevo la contraseña: ")
    salir=False
    while not salir:
        if(contraseña==validar):
            print("Contraseña correcta")
            salir=True
        else:
            print("Contraseña incorrecta")
            validar=input("Introduce de nuevo la contraseña: ")
    return contraseña

def main():
    contraseña=pedirContraseña()

    validarContraseña(contraseña)


if (__name__ == "__main__"):
    main()
