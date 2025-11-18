
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