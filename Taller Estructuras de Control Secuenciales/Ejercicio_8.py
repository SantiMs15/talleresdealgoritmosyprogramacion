import math
a=float(input("Ingrese lado a: "))
b=float(input("Ingrese lado b: "))
c=float(input("Ingrese lado c: "))
#Caja negra
s=(a+b+c)/2
area=math.sqrt(s*(s-a)(s-b)(s-c))
#salida
print(f"El area es: {round(area)}")