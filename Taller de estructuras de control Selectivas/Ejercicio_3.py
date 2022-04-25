"""
A-->int-->A
B-->int-->B
C-->int-->C
D-->int-->D
"""
A=int(input(" "))
B=int(input(" "))
C=int(input(" "))
D=int(input(" "))
#Caja negra
if D==0: 
    r=(A-C)**2
    print(f"{r}")
elif D>0:
    r=(A-C)**3/D
    print(f"{r}")