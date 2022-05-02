cantidad=int(input("Digite cantidad de estudiantes: "))
altura_mayor=0
for i in range(1,cantidad):
    altura=float(input("Digite la altura: "))
    if(altura_mayor<=altura):
        altura_mayor=altura
#Salida
print(altura_mayor)