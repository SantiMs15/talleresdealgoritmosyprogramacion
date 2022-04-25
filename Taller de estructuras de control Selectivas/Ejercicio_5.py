"""
sueldo-->float-->siuu
dpto1-->float-->d1
dpto2-->float-->d2
dpto3-->float-->d3
"""
siuu=float(input("Sueldo: "))
d1=float(input("Ventas dpto 1: "))
d2=float(input("Ventas dpto 2: "))
d3=float(input("Ventas dpto 3: "))
#Caja negra
sells=d1+d2+d3
perc=sells*0.33
ns=(siuu*0.20)+siuu
if d1>perc:
    print(f"El sueldo de dpto 1 es: {ns}")
else:
    print(f"El sueldo de dpto 1 es: {siuu}")
if d2>perc:
    print(f"El sueldo de dpto 2 es:{ns}")
else:
    print(f"El sueldo de dpto 2 es: {siuu}")
if d3>perc:
    print(f"El sueldo de dpto 3 es: {ns}")
else:
    print(f"El sueldo de dpto 3 es: {siuu}")