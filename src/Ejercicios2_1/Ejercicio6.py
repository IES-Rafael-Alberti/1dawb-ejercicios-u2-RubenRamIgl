nombre=input("Introduce tu nombre (Empieza por mayúscula): ")
sexo=input("Introduce tu sexo: ")

if((nombre<"M" and sexo=="mujer") or (nombre>"N" and sexo=="hombre")):
    print("Perteneces al grupo A")
else:
    print("Perteneces al grupo B")