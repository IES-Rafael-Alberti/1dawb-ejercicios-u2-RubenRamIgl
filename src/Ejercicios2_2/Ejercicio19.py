def menu():
    salir=False
    while not salir:
        print("opcion 1: comenzar")
        print("opcion 2: imprimir listado")
        print("opcion 3: finalizar programa")
        opcion=input("Elige una opcion: ")
        if(opcion.isnumeric()):
            opcion=int(opcion)
            match(opcion):
                case 1:
                    print("programa iniciado")
                case 2:
                    print("lista")
                case 3:
                    print("saliste del programa")
                    salir=True
                case _:
                    print("Error, opción no válida")
                    opcion=input("Elige una opcion: ")

def main():
    menu()

if (__name__ == "__main__"):
    main()