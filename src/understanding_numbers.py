

#  numeros

"""
 Enteros
Los podemos sumar (+), restar (-) , multiplicar (*) y dividir (/).
 Les podemos aplicar potencias (**2, **3, **4, ...), modulo (%)
"""

Numer_1 = 35
Numer_2 = 15
suma = Numer_1+Numer_2
resta = Numer_1-Numer_2
multiplicando = Numer_1*Numer_2
division = Numer_1/Numer_2
potencia = Numer_1**2
Modulo = Numer_1%Numer_2

print("suma: ", suma, type(suma))
print("resta: ", resta, type(resta))
print("multiplicando: ", multiplicando, type(multiplicando))
print("division: ", division, type(division))
print("potencia: ", potencia, type(potencia))
print("Modulo: ", Modulo, type(Modulo))

"""
 Jerarquia de operaciones

 2+3*4 = 14
 (2+3)*4 = 20
"""

""" 
 floats
  Python llama Floats a cualquier numero flotante
 Los podemos sumar (+), restar (-) , multiplicar (*) y dividir (/).
 Les podemos aplicar potencias (**2, **3, **4, ...),
"""

print(0.1+0.1)
print(0.2-0.2)
print(0.1*2)
print(2*0.2)

#  Imprimir la edad de alguien
age = 18
message = "andrik tiene " + str(age) + "años" 
print(message)

"""
 TypeError: no puede reconocer el tipo de informacion 
 que se esta utilizando
"""