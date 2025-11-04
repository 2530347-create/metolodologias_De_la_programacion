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

message_f  = f"mi primera bicicleta fue una " {bicycles[-5].title()}."
print(message_f)

## Agregar elementos a una lista
print("/n")
print(Agregar elementos de una lsita)
print(bicycles)

print("metodo de la lista para agregar elementos: list_name.apped(element)")
bicycles. append("ducatti")
print(bicycles)