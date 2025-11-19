
"""
try:
    age =int(input("Escribe tu edad: "))
    
    if age >= 18:
        print ("mayor de edad")
    else:
        print("menor")

except:
    print("pon numeros no letras")

print("hola andrik")
"""

"""
age = 0

try:
    age =int(input("Escribe tu edad: "))
    
except:
    print("pon numeros no letras")

# bloque if-elif-else
if age >=100:
    print("Mas de un siglo... ¿Enserio?")
elif age >= 18 and age < 100:
    print ("Eres mayor de edad")
elif age >= 0 and age < 18:
    print("Eres menor de edad")
else:
    print("ERROR, hazlo bien no mamaes")

print("Gracias")
"""

"""
age = 0

try:
    age =int(input("Bienvenido, Escribe tu edad: "))
    
except:
    age=-1
    print("pon numeros no letras")


if age >=18:
    print("Entrada $400")
    print("favor de no empujar a menores")
elif age >= 4 and age < 18:
    print ("Entrada $200")
    print("favor de esta cerca de los padres")
elif age >= 0 and age < 4:
    print("Entrada Gratuita")
else:
    print("ERROR, escribe bien tu edad por favor")

print("Disfruta su visita")
"""

"""
#if multiple

guisos= ["deshebrada", "asado", "salsa verde", "pozole"]

if "asado" in guisos:
    print("si hay asado")
else:
    print("no hay asado")
if "Tamales" in guisos:
    print("si hay tamales")
else:
    print("No hay tamales")
if "salsa verde" in guisos:
    print("Si hay salsa verde") 
else:
    print("No hay salse verde")
"""

# Utilizando varias listas

guusos_disponibles = ["deshebrada", "deshebrada", "mole"]
guisos_a_ordenar = ["deshebrada", "caldo de iguana",]

print("Que quires")

for guisos in guisos_a_ordenar:
    print(f"Deseo{guisos}")
    if guisos in guisos_disponibles:
        print(f"Si tenemos {guisos}")
    else:
        print("No tenemos de ese guiso")
print("Realizando pedido...")