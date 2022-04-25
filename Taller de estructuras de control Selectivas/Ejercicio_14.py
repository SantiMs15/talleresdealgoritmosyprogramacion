import math
"""
Lectura actual-->int-->la
Lectura anterior-->int--lv
"""
la=int(input("Lectura actual de luz: "))
lv=int(input("Lectura anterior de luz: "))
#caja negra
vl=abs(la-lv)
vf=""
if vl>=0 and vl<=100:
    vf=vl*4600
    print(f"Debe pagar: {vf}")
elif vl>=101 and vl<=300:
    vf=vl*80.00
    print(f"Debe pagar: {vf}")
elif vl>=301 and vl<=500:
    vf=vl*100000
    print(f"Debe pagar: {vf}")
elif vl>=501:
    vf=vl*120000
    print(f"Debe pagar: {vf}")