#Entradas
presupuesto=float(input("Digite el presupuesto total del hospital: "))
#Caja negra
ginecología=presupuesto*0.40
traumatología=presupuesto*0.30
pediatría=presupuesto*0.30
#Salidas
print(f"El valor que recibirá el área de ginecología es de: {ginecología} COP")
print(f"El valor que recibirá el área de traumatología es de: {traumatología} COP")
print(f"El valor que recibirá el área de pediatría es de: {pediatría} COP")