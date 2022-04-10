#Entradas
luz_ant=int(input("Digite los kilovatios de la lectura anterior: "))
luz_act=int(input("Digite los kilovatios de la lectura actual: "))
kilovatio_value=float(input("Digite el valor del kilovatio: "))
#Caja negra
value_luz_ant=luz_ant*kilovatio_value
value_luz_act=luz_act*kilovatio_value
value_diff=abs(value_luz_act-value_luz_ant)
#Salida
print(f"El valor de la luz de la lectura pasada fue de: {value_luz_ant} COP ")
print(f"El valor de la luz en la lectura actual es de: {value_luz_act} COP")
print(f"La diferencia en las medidas fue de un valor de: {value_diff} COP")