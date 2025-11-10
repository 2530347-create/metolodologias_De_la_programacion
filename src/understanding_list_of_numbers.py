"""
    Las listas tambien pueden almacenar numeros
     ademas de ser ideales para eso
     Python ofrece una gran cantidad de herramientas que 
     ayudan a trabajar eficientemente listas de numeros
"""
 
"""
    metodo range() nos ayuda a crear facilmente
    series de numeros
    Ejemplo:
"""
print("numeros de 0 a 9")
for value in range(10): # 10 numero entre 0-9
   print(value)

print("numeros de 1 a 9")
for value in range(1,10): # 10 numero entre 1-9
   print(value)


print("numeros impares del 1 al 9")
for value in range(1,10,2): # 10 impares entre 1-9
   print(value)
odd_numbers = list(range(1,10,2))
print (odd_numbers)
print("numeros par del 1 al 9")
for value in range(0,10,2): # 10 pares entre 1-9
   print(value)
ever_numbers = list(range(0,10,2))
print(ever_numbers)
print("Tabla  del 9")
for value in range(0,91,9): 
   print(value)
Tabla= list(range(0,91,9))
print(Tabla)

# Cuadrados de los primeros 10 numeros
squares = []
for numbers in range (1,11):
    square = numbers**2
    squares.append(square)
print(square)

# # Mas metodos built-in
# Metodo min()
digits = [1,2,3,4,5,6,7,8,9,0]
print(min(digits))# salida: 0
# Metodo max()
digits = [1,2,3,4,5,6,7,8,9,0]
print(max(digits)) # salida: 9
# Metodo sum()
digits = [1,2,3,4,5,6,7,8,9,0]
print(sum(digits)) # salida: 45