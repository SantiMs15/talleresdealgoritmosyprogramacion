"""
Categoria-->int-->c
sueldo-->float-->siuu
"""
c=int(input("Escriba la categoría del trabajador: "))
siuu=float(input("Escriba el sueldo del trabajador: "))
#caja negra
val="" 
if c==1:
    val=siuu*0.10+siuu
    print(f"{c}Categoría \nNuevo sueldo bruto: {val}")
elif c==2:
    val=siuu*0.15+siuu
    print(f"Categoría {c}\nNuevo sueldo bruto: {val}")
elif c==3:
    val=siuu*0.20+siuu
    print(f"Categoría: {c}\nNuevo sueldo bruto: {val}")
elif c==4:
    val=siuu*0.40+siuu
    print(f"Categoría {c}\nNuevo sueldo bruto: {val}")
elif c==5:
    val=siuu*0.60+siuu
    print(f"Categoría {c}\nNuevo sueldo bruto: {val}")
    