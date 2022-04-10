#Entradas
parcial1=float(input("Nota de la primera calificación: "))
parcial2=float(input("Nota de la segunda calificación: "))
parcial3=float(input("Nota de la tercera calificación: "))
examenf=float(input("Nota del examen final: "))
trabajo=float(input("Nota del trabajo final: "))
#Caja negra
parciales=(parcial1+parcial2+parcial3)/3*0.55
examen=examenf*0.30
trabajof=trabajo*0.15
nota_final=parciales+examen+trabajof
#Salidas
print(f"La nota final de computación es de: {nota_final}")