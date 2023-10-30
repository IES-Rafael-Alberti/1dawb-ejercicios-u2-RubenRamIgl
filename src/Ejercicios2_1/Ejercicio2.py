"""
contraseña=input("Introduce una contraseña: ")
pregunta=input("Introduce de nuevo la contraseña: ")

if(contraseña.lower()==pregunta.lower()):
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")
"""
    
def pedirContraseña():
    contraseña=input("Introduce una contraseña: ")
    return contraseña

def validarContraseña():
    pregunta=input("Introduce de nuevo la contraseña: ")
    return pregunta

def igual(contraseña,pregunta):
    if(contraseña.lower()==pregunta.lower()):
        return True
    else:
        return False

def main():
    contraseña=pedirContraseña()
    pregunta=validarContraseña()
    if(igual(contraseña,pregunta)):
        print("La contraseña es correcta")
    else:
        print("La contraseña es incorrecta")

if (__name__ == "__main__"):
    main()
        