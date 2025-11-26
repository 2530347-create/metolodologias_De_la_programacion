# 

"""
       while conditional:
        action

"""
"""
# while infinito
while true:
    print("charly")
"""
"""
  programa si el usuario escribe un num eros entre 25 y 50, entonces estara
   dentro del rango y salirme de while,
   de otro modo pedirle otro numero.
"""
"""
while True:
    try:
        number = int(input("ingresa un numero"))
        if number >= 25 and number <= 50:
        print("dentro del rango")
        break
    else:
        print("fuera de rango")
        
    except ValueError:
        print("se ha introducuido una variable no valida")
"""

while True:
    try:
        number = int(input("ingresa un numero: "))
        if 10<= number <=20:
            print("dentro del rango")
            break
        else:
            print("fuera de rango")
    except ValueError:
        print("se ha introducuido una variable no valida")
    except KeyboardInterrupt:
        print("programa terminado por el usuario")
        break
print("saliste")
    