n=int(input("Introduce un número positivo: "))

cont=1

while(cont<=n):
    if(cont%2!=0):
        if(cont==n or cont==n-1):
         print(cont, end="")
        else:
         print(cont, end=",")
    cont+=1
        