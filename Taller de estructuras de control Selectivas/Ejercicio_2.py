"""
sueldo-->float-->siuuu
"""
siuuu=float(input("Digite sueldo: "))
#Caja Negra
if siuuu<=899999:
    siuuu=(siuuu*0.15)+(siuuu)
    print(f"Nuevo sueldo: {siuuu}")
elif siuuu>=900000:
    siuuu=(siuuu*0.12)+(siuuu)
    print(f"Nuevo sueldo: {siuuu}")
    