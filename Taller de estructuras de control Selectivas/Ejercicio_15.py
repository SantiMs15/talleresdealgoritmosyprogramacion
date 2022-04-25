"""
Sexo biológico del paciente-->int-->s
años dell paciente-->int-->a
meses del paciente-->int-->m
hemoglobina-->float-->h
"""
s=int(input("Mujer (1) u Hombre (2) (Biológico): "))
a=int(input("Años del paciente: "))
m=int(input("Meses del paciente (si aplica): "))
h=float(input("Nivel de hemoglobina: "))
#caja negra 
v=""
if m>0 and m<=1 and h<13:
    v=True
elif m>1 and m<=6 and h<10:
    v=True
elif m>6 and m<=12 and h<11:
    v=True
elif a>1 and a<=5 and h<11.5:
    v=True
elif a>5 and m<=10 and h<12.6:
    v=True
elif a>10 and m<=15 and h<13:
    v=True
elif a>15 and s<=1 and h<12:
    v=True
elif a>15 and s<=2 and h<14:
    v=True
if v==True:
    print("El paciente tiene anemia")
else:
    print("El paciente no tiene anemia")