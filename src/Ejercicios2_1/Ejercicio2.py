contraseña=input("Introduce una contraseña: ")
pregunta=input("Introduce de nuevo la contraseña: ")

if(contraseña.lower()==pregunta.lower()):
    print("La contraseña es correcta")
else:
    print("La contraseña es incorrecta")