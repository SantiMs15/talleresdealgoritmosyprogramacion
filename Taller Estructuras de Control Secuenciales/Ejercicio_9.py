#Entradas
numero_h=int(input("Digite el número de horas trabajadas: "))
valor_h=float(input("Digite el valor de la hora trabajada: "))
#Caja negra
sueldo_base=numero_h*valor_h
descuento=sueldo_base*0.20
sueldo_neto=sueldo_base-descuento
#Salida
print(f"El salario neto del trabajador es de: {sueldo_neto}")