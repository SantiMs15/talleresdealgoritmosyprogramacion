import math
"""
nombre del cliente-->str-->nc
valor compra-->float-->m
"""
nc=input("Digite su nombre: ")
m=float(input("Digite el valor de la compra: "))
#caja negra
val=""
if m<50000:
    print("No hay descuento")
elif m>=50000 and m<=100000:
    val=abs(m*0.5-m)
    print(f"{nc}\n {m}\n Valor final: {val} Descuento del 5%")
elif m>=100000 and m<=700000:
    val=abs(m*0.11-m)
    print(f"{nc}\n {m}\n Valor final: {val} Descuento del 11%")
elif m>=700000 and m<=1500000:
    val=abs(m*0.18-m)
    print(f"{nc}\n {m}\n Valor final: {val} Descuento del 18%")
elif m>1500000:
    val=abs(m*0.25-m)
    print(f"{nc}\n {m}\n Valor final: {val} Descuento del 25%")