def pedirMonto():
    n=input("Introduce un precio (0 para salir): ")
    salir=False
    while not salir:
        if(n.isnumeric()):
            return float(n)
        elif (n=="0"):
            salir=True
        else:
            print("Error, número no válido")
            n=input("Introduce un precio (0 para salir):")
        
def sumarMontos():
    suma=0
    while True:
        monto=pedirMonto()
        if monto==0:
            break
        suma+=monto

    if(suma>=1000):
        print("Se le aplicó un descuento del 10%")
        descuento=suma*0.1
        suma-=descuento

    print("El monto total es:",suma)

def main():
    sumarMontos()

if (__name__ == "__main__"):
    main()