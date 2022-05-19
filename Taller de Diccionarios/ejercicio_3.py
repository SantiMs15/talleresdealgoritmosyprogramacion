usuarios = { 
    "iperurena": { 
        "nombre": "Iñaki", 
            "apellido": "Perurena", 
            "password": "123123" 
        }, 
        "fmuguruza": { 
            "nombre": "Fermín", 
                "apellido": "Muguruza", 
                "password": "654321" 
        }, 
        "aolaizola": { 
            "nombre": "Aimar", 
                "apellido": "Olaizola", 
                "password": "123456" 
    } 
} 
c=0
for i in usuarios:
    a=input("Digite su usuario: ")
    b=input("Digite su contraseña: ")
    if a in usuarios and (b==usuarios[a]["password"]):
        nombre=usuarios[a]["nombre"]
        apellido=usuarios[a]["apellido"]
        print(nombre,apellido)
        break
    else:
        c=c+1
        if c==3:
            print("No quedan intentos")