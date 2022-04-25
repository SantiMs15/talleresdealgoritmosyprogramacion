"""
Kilometros-->float-->km
"""
km=float(input("Digite los kilometros: "))
#caja negra
val=""
if km<300:
    val=50000
    print(f"Se cancelan: {val}")
elif km>300 and km<1000:
    val=(km-300)*30000+70000
    print(f"Se cancelan: {val}")
elif km>1000:
    val=(km-1000)*9000+150000
    print(f"Se cancelan: {val}")