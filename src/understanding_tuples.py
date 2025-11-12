"""
    las tuplas son listas de elementos que no cambian de tamaño
    las tuplas son INMUTABLES.

    Se utilizan los () para definir una tupla.


"""

rectangle = (200,50) # (largo,ancho)
# print(rectangle[0])
# print(rectangle[1])

# for menasure in rectangle_measurements:
#     print(measure)

# print(dir(rectangle_measurements))

# Regrfesano un poco a las listas
cars=["bwm","porche","masada"]
print(cars)
cars[0]="bmw"
cars[1]="porshe"
cars[2]="mazada"
print(cars)

rectangle_measurements=(200,50)

#rectangle_measurements[0]=300 #mal
#rectangle_measurements[1]=100 #mal

rectangle_measurements=(300,100)

"""
    NO se puede midificar una tupla directamnete, solo podemos hacer
    es cambiar las asignasiones a una variable que almacena una tupla. 
"""