"""tipo=input("La pizza es vegetariana?(si/no): ")

if(tipo.lower()=="si"):
    pizza="vegetariana"
    print("Ingredientes vegetarianos: Pimiento y tofu")
    ingrediente=input("Elige un ingrediente: ")
elif(tipo.lower()=="no"):
    pizza="no vegetariana"
    print("Ingredientes no vegetarianos: Peperoni, jamón y salmón")
    ingrediente=input("Ejige un ingrediente: ")

if(ingrediente!="pimiento" and ingrediente!="tofu" and ingrediente!="peperoni" and 
   ingrediente!="jamón" and ingrediente!="salmón"):
    print("El ingrediente es incorrecto")
else:
    print("Su pizza es "+pizza+" y sus ingredientes son mozzarella, tomate y "+ingrediente)"""

def pedirTipo():
    tipo=input("La pizza es vegetariana?(si/no): ")
    return tipo.lower()

def pedirIngredientes(tipo):
    tipo=str(tipo)
    if(tipo.lower()=="si"):
        salir=False
        pizza="vegetariana"
        print("Ingredientes vegetarianos: Pimiento y tofu")
        while not salir: 
            ingrediente=input("Elige un ingrediente: ")
            if(ingrediente.lower()=="pimiento" or ingrediente.lower()=="tofu"):
                salir=True
            else:
                print("Error, introduce un ingrediente correcto")
                
    else:
        salir=False
        pizza="no vegetariana"
        print("Ingredientes no vegetarianos: Peperoni, jamón y salmón")
        while not salir: 
            ingrediente=input("Elige un ingrediente: ")
            if(ingrediente.lower()=="peperoni" or ingrediente.lower()=="jamón" or 
               ingrediente.lower()=="salmón"):
                salir=True
            else:
                print("Error, introduce un ingrediente correcto")
                

    return pizza,ingrediente

def main():
    tipo=pedirTipo()
    pizza,ingrediente=pedirIngredientes(tipo)
    print("Su pizza es "+pizza+" y sus ingredientes son mozzarella, tomate y "+ingrediente)

if (__name__ == "__main__"):
    main()