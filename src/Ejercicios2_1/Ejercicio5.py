edad=int(input("Introduce tu edad: "))
ingresos=float(input("Introduce tus ingresos: "))

if(edad>16 and ingresos>=1000):
    print("Puedes tributar")
else:
    print("No puedes tributar")