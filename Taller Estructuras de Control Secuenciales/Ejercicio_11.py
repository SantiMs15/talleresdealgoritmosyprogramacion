#Entradas
nombre=str(input("Escriba el nombre del trabajador: "))
numero_horas=int(input("Escriba el numero de horas: "))
pago_hora=float(input("Escriba el pago por hora: "))
horas_extras=int(input("Escriba las horas extra: "))
total_hijos=int(input("Escriba cantidad de hijos: "))
#Caja negra
he=pago_hora*0.25+pago_hora
pago_labor=(numero_horas*pago_hora)+(he*horas_extras)
deducciones=pago_labor-pago_labor*0.14
asignaciones=250000+180000+173000*total_hijos
sueldo_neto=pago_labor+asignaciones-deducciones
#Salidas
print("El sueldo neto es de :",sueldo_neto)
print("El total de las asignaciones es de:",asignaciones)
print("El total de las deducciones es de:",deducciones)