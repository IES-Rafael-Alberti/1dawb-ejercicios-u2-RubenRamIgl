n=int(input("Introduce un número positivo: "))

cont=n

while(cont>=0):
    if(cont==0):
        print(cont, end="")
    else:
         print(cont, end=",")
    cont-=1