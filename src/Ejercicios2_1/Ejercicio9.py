edad=int(input("Introduce la edad del cliente: "))

if(edad<4):
    precio=0
elif(edad>=4 and edad<=18):
    precio=5
else:
    precio=10

print("El precio de la entrada es",precio)