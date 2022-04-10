
#Entradas
naranjas=int(input("Digite cantidad de naranjas: "))
valor=float(input("Digite el valor de la docena de naranjas: "))
ganancias=float(input("Digite el valor de las ganancias: "))
#Caja Negra
money=valor/12*naranjas
money2=money+ganancias
porcentaje=money2*100/money
porcentajef=porcentaje-200
#Salida
print(f"El porcentaje de la ganancia obtenida es del: {porcentajef}")