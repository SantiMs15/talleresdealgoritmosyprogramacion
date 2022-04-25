"""
dinero-->float-->d
tasa de ínteres--float-->ti
"""
#:V

d=float(input("Digite el dinero: "))
ti=float(input("Digite la tasa de ínteres: "))
#Caja negra
vi=d*ti/100
vf=""
if vi>100000:
    vf=vi+d
    print(f"El dinero total es de: {vf}")
else:
    print("No se realizaron movimientos")