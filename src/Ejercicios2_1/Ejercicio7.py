renta=int(input("Introduce tu renta anual: "))
impositivo=0

if(renta<10000):
    impositivo=5
elif(renta>=10000 and renta<20000):
    impositivo=15
elif(renta>=20000 and renta<35000):
    impositivo=20
elif(renta>=35000 and renta<60000):
    impositivo=30
else:
    impositivo=45

print("Tu impositivo es :",impositivo)