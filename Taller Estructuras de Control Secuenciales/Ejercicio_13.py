#Entradas
n_1=int(input("Digite la cantidad de billetes de 50000: "))
n_2=int(input("Digite la cantidad de billetes de 20000: "))
n_3=int(input("Digite la cantidad de billetes de 10000: "))
n_4=int(input("Digite la cantidad de billetes de 5000: "))
n_5=int(input("Digite la cantidad de billetes de 2000: "))
n_6=int(input("Digite la cantidad de billetes de 1000: "))
n_7=int(input("Digite la cantidad de billetes de 500: "))
n_8=int(input("Digite la cantidad de billetes de 100: "))
#Caja negra
d1=n_1*50000
d2=n_2*20000
d3=n_3*10000
d4=n_4*5000
d5=n_5*2000
d6=n_6*1000
d7=n_7*500
d8=n_8*100
total_dinero=d1+d2+d3+d4+d5+d6+d7+d8
#Salidas
print(f"El total del dinero que tiene el banco es de: {total_dinero} COP")
