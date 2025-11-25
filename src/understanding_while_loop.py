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

while True:
    try:
        number = int(input("ingresa un numero"))
        if number >= 21 and number <= 50:
        print("dentro del rango")
        break
    else:
        print("fuera de rango")
        
    except ValueError:
        print("se ha introducuido una variable no valida")
    