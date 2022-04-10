#Entradas
valor_off=float(input("Digite el valor oficial del producto: "))
valor_disc=float(input("Digite el valor de venta al público: "))
#Caja negra
valorf=valor_disc*100/valor_off
percentf=abs(valorf-100)
#Salidas
print(f"El porcentaje de descuento aplicado al producto es del: {percentf}%")