# List
"""
    Las listas son elementos mutables
    Las listas nos permiten almacenar informacion
    en un lugar la cantidad que tenga: ya sea
    pocos o muchos elementos

    se recomienda nobrar una variables del tipo lista en plural

    En python los corchetes [] definen una lista; sus elementos
    van separados por comas.
    Ejemplos:
"""
bicycles= ['trek', 'canondale', 'redline', 'specialized', 'giants']
print(bicycles)

print(bicycles[0].title())

# Los indices comienzanen en 0 y terminan en n-1, donde n es el nimero de elementos
print(bicycles[4].title())

# Accediento al ultimo elementos
print(bicycles[-1].title())# ultimo elementos
print(bicycles[-2].title())
print(bicycles[-5].title())# primer elementos

#  utilizando valores individuales

message = "mi primera bicicleta fue una " + bicycles[-5].title() + "."
print(message)

message_f = f"mi primera bicicleta fue una {bicycles[-5].title()}."
print(message_f)

## Agregar elementos a una lista
print("\n")
print("Agregar elementos de una lsita")
print(bicycles)

print("metodo de la lista para agregar elementos: list_name.apped(element)")
bicycles. append("ducatti")
print(bicycles)

"""
 Agregar elementos a una lista 
      - append(): Agrega un elementos al final de la lista
"""
print("\n--- grega un elementos al final de la lista() ---")
motorcycles = ['trek', 'canondale', 'redline', 'specialized', 'giants']
print(motorcycles)
motorcycles.append('otro')
print(motorcycles)

"""
 Agregar elementos a ua lista en una posicion especifica
    - insert(): Insetra un elementos en una posiciom especifica
"""
print("\n--- Insetra un elementos en una posiciom especifica() ---")
motorcycles = ['trek', 'canondale', 'redline', 'specialized', 'giants']
print(motorcycles)
motorcycles.insert(1,'otro')
print(motorcycles)

"""
 ELiminar elementos de ina lista
   -del: Elimina un elementos en una posicion especifica
"""

print("\n--- Elimina un elementos en una posicion especifica() ---")
motorcycles = ['trek', 'canondale', 'redline', 'specialized', 'giants']
print(motorcycles)
del motorcycles[0]
print(motorcycles)

"""
    Eliminar elementos de una lista y sural valor eliminado metodo pop
"""
print("\n---Eliminar elementos de una lista y sural valor eliminado() ---")
motorcycles = ['trek', 'canondale', 'redline', 'specialized', 'giants']
print(motorcycles)
last_motorcycles = motorcycles.pop()
print(motorcycles)
print (f'elimnaste gigant' )

"""
    Eliminar elementos especifico
      -pop(index): Elimina elementos especifico de la lista
         por un valor metodo pop(index)
"""
print("\n--- Elimina elementos especifico de la listad() ---")
motorcycles = ['trek', 'canondale', 'redline', 'specialized', 'giants']
print(motorcycles)
motorcycles.remove('trek')
print(motorcycles)
print("\n")

"""
    Organizadar una lista permanente
        -sort(): Ordena la lista en orden alfafetico
"""

print("\n--- Ordena la lista en orden alfafetico() ---")
motorcycles = ['trek', 'canondale', 'redline', 'specialized', 'giants']
print(motorcycles)
motorcycles.sort()
print(motorcycles)
print("\n")

"""
    Ejemplo:
"""

students =  ["josue","victor","ana","mike","paulo","gerardo"]
print(students)
desired_student = input("¿Que estudiante vas a borrar?")
students.remove(desired_student.strip().lower())
print(students)
print("Tu has eliminado : ", desired_student)
students.reverse()
print(students)

print(len(students))

cars =  ["kia", "fors", "tesla", "volvo", "chevrolet"]
print(cars)
print(sorted(cars))
sorted_list = sorted (cars)
print("Lista original: ",cars)

