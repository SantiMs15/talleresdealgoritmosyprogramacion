#Entradas
sueldo=float(input("Digite el valor del sueldo base: "))
venta1=float(input("Valor de la primera venta: "))
venta2=float(input("Valor de la segunda venta: "))
venta3=float(input("Valor de la tercera venta: "))
#Caja negra
comision=(venta1*0.10)+(venta2*0.10)+(venta3*0.10)
sueldo_total=sueldo+comision
#Salidas
print(f"El valor total de las comisiones es de: {comision}")
print(f"El sueldo total del mes es de: {sueldo_total}")