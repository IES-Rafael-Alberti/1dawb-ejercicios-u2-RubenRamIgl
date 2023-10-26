tipo=input("La pizza es vegetariana?(si/no): ")

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
    print("Su pizza es "+pizza+" y sus ingredientes son mozzarella, tomate y "+ingrediente)