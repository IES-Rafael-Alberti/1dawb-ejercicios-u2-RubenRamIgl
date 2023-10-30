"""puntuacion=float(input("Introduce la puntuación: "))
nivel=""
dinero=2400
extra=dinero*puntuacion
total=dinero+(dinero*puntuacion)

if(puntuacion==0.0):
    nivel="Inaceptable"
elif(puntuacion==0.4):
    nivel="Aceptable"
elif(puntuacion>=0.6):
    nivel="Meritorio"
else:
    print("Error la puntuación no es válida")

print("Tu nivel es "+nivel+" y tu sueldo es de "+str(dinero)+" € con "+str(extra)+
      " € de extra("+str(total)+"€)")"""

def pedirPuntuacion():
    puntuacion=input("Introduce la puntuación: ")
    salir=False
    while not salir:
        if(puntuacion.replace(".","").isnumeric()):
            salir=True
        else:
            print("El valor introducido no es válido")
            puntuacion=input("Introduce la puntuación: ")
    
    return float(puntuacion)

def definirNivel(puntuacion):
    dinero=2400
    extra=dinero*puntuacion
    total=dinero+(dinero*puntuacion)
    if(puntuacion==0.0):
        nivel="Inaceptable"
    elif(puntuacion==0.4):
        nivel="Aceptable"
    elif(puntuacion>=0.6):
        nivel="Meritorio"
    else:
        print("Error la puntuación no es válida")

    print("Tu nivel es "+nivel+" y tu sueldo es de "+str(dinero)+" € con "+str(extra)+
      " € de extra("+str(total)+"€)")
    
def main():
    puntuacion=pedirPuntuacion()

    definirNivel(puntuacion)

if (__name__ == "__main__"):
    main()