#Entradas
precio_i=float(input("Digite el valor del dispositivo: "))
precio_c=float(input("Digite el valor del dispositivo pagado en cuotas: "))
#Caja negra
pi=precio_i/12
pc=precio_c/12
valorf=pc*100/pi
disc=abs(valorf-100)
#Salida
print(f"El porcentaje de ínteres por cuota sobre el valor del equipo es de: {disc}%")