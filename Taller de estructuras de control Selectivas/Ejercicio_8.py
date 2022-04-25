"""
P-->int-->p
Q-->int-->q
"""
p=int(input(""))
q=int(input(""))
#Caja negra
res=p**3+q**4-2*p**2
if res>680:
    print(f"{res}")
    print("P  y  Q satisfacen la expresión")
else:
    print(f"{res}")
    print("P y Q no Satisfacen la expresión")
