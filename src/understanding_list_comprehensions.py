"""
squares= []
for value in range (0,11):
    square = value**2
    squares.append(square)
print(squares)
"""
"""
   Una list comprenhention combina el ciclo for y la creacion 
   de nuevos elementos en una sola linea yb automaticamento agrega
   cada nuevo elemento a la lista, sin utilizar el metodo append.
"""

square = [value**2 for value in range(0,11)]
print(square)

# Para lo numeros pares entre 0 y 100

ebens_range = [value for value in range(0,101,2)]

evens_if =[value for value in range(0,101,2) if value%2==0]
print(evens_if)