"""tablas=10

cont=0
cont2=0

while(cont<=tablas):
    for cont2 in range(tablas+1):
        print(cont,"x",cont2,"=",cont*cont2)
        cont2+=1
    cont+=1
    print("\n")"""

def imprimirTablas():
    tablas=10

    cont=0
    cont2=0

    while(cont<=tablas):
        for cont2 in range(tablas+1):
            print(cont,"x",cont2,"=",cont*cont2)
            cont2+=1
        cont+=1
        print("\n")

def main():
    imprimirTablas()

if (__name__ == "__main__"):
    main()