"""nombre=input("Introduce tu nombre (Empieza por mayúscula): ")
sexo=input("Introduce tu sexo: ")

if((nombre<"M" and sexo=="mujer") or (nombre>"N" and sexo=="hombre")):
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")"""

def pedirNombre():
    return input("Introduce tu nombre: ")

def pedirSexo():
    sexo=""
    while sexo!="M" and sexo!="F":
        sexo=input("Introduce tu sexo (M/F): ").upper()

    return sexo

def asignarGrupo(nombre,sexo):
    inicialNombre=nombre[0:1].upper()
    grupo=""
    if((inicialNombre<"M" and sexo=="F") or (inicialNombre>"N" and sexo=="M")):
        grupo="A"
    else:
        grupo="B"

    return grupo

    

def main():
    nombre=pedirNombre()
    sexo=pedirSexo()

    print(f"Estás en el grupo {asignarGrupo(nombre,sexo)}.")

if (__name__ == "__main__"):
    main()