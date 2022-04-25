from datetime import datetime
ahora = datetime.now()
año_actual = ahora.year
mes_actual = ahora.month
dia_actual = ahora.day
#entradas
fecha_nacimiento=input("Digite fecha de nacimiento")
año_nacimiento,mes_nacimiento,dia_nacimiento.split("/")
año_nacimiento=int(año_nacimiento)
mes_nacimiento=int(mes_nacimiento)
dia_nacimiento=int(dia_nacimiento)
#caja negra
edad=0
if(mes_actual>mes_nacimiento):
    edad=año_actual-año_nacimiento
elif(mes_actual==mes_nacimiento):
    if(dia_nacimiento>dia_actual)
#Calcular signo
zodiaco=""
if(mes_nacimiento>=11 and dia_nacimiento>=22) and (mes_nacimiento<=12 and dia_nacimiento=>21)
zodiaco="sagitario"
elif(mes_nacimiento>=12 and dia_nacimiento>=22) and (mes_nacimiento<=1 and dia_nacimiento=>20)
zodiaco="capricornio"
elif(mes_nacimiento>=1 and dia_nacimiento>=21)and(mes_nacimiento<=1 and dia_nacimiento=>19)
zodiaco="acuario"
elif(mes_nacimiento>=2 and dia_nacimiento>=20)and(mes_nacimiento<=1 and dia_nacimiento=>19)
zodiaco="piscis"
elif(mes_nacimiento>=3 and dia_nacimiento>=21)and(mes_nacimiento<=1 and dia_nacimiento=>20)
zodiaco="aries"
elif(mes_nacimiento>=4 and dia_nacimiento>=21)and(mes_nacimiento<=1 and dia_nacimiento=>21)
zodiaco="tauro"
elif(mes_nacimiento>=5 and dia_nacimiento>=22)and(mes_nacimiento<=1 and dia_nacimiento=>21)
zodiaco="géminis"
elif(mes_nacimiento>=6 and dia_nacimiento>=22)and(mes_nacimiento<=1 and dia_nacimiento=>22)
zodiaco="cáncer"
elif(mes_nacimiento>=7 and dia_nacimiento>=23)and(mes_nacimiento<=1 and dia_nacimiento=>23)
zodiaco="leo"
elif(mes_nacimiento>=8 and dia_nacimiento>=24)and(mes_nacimiento<=1 and dia_nacimiento=>24)
zodiaco="virgo"
elif(mes_nacimiento>=9 and dia_nacimiento>=23)and(mes_nacimiento<=1 and dia_nacimiento=>23)
zodiaco="libra"
elif(mes_nacimiento>=10 and dia_nacimiento>=23)and(mes_nacimiento<=1 and dia_nacimiento=>23)
zodiaco="escorpión"
#salidas
print(f"El signo es: {zodiaco}")