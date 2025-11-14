cars = ["audi", "bmw", "chevrolet", "corvette", "tesla"]

for car in cars:
    if car == "bmw" or car=="tesla" or car=="audi":
        print(car.upper())
    else:
        print(car)   


# condicionales:El condicional es el corazon de un if
# condicional true
car = "bmw"
print(car == "bmw") # salida true
# condicional false    
car_2 = "audi"
print(car_2 == "audi") # salida false

# condicional fa|lse
car_2 = "audi"
print(car_2.lower() == "Audi")

# condicional != para determinar desigualdad
requested_topping = "mushrooms" # --> string
if requested_topping != "anchovies":# -->
    print("Hold the anchovies")

# comparaciones numericos
age = 18 # --> int
print(age == 18) # --> true

answer = 17
if answer != 42:
    print("Esa no es la respuesta correcta. Intenta de nuevo!")

age = 19
print(age < 21) # --> true
print(age <= 21) # --> true
print(age > 21) # --> false|
print(age >= 21) # --> false

"""
El condicional es el corazon de if
car= "bwm"
print(car=="bwm") # true

# condicion false
car= "audi"
print(car=="audi") # false

# solucion a condicion fales
print(acrs.lower() == "audi")

requested_topping = "muahrooms"
if requested_topping
"""

# multiple
age_0 = 22
age_1 = 18
print("miltiples condiciones")
print("operacion and - pseint (y)")
print( age_0 >= 21 and age_1 >=21) #False
print( age_0 >= 21 and age_1 >=18) #True

age_0 = 22
age_1 = 18
print("miltiples condiciones")
print("operacion or - pseint (0)")
print( age_0 >= 21 and age_1 >=21) #True
print( age_0 >=23 and age_1 >=18) #False

#  ¿como sabemos que un calor esta en una lista?
print("\nA value is in a list")
requested_topping = ["mushrooms", "onions", "pineapple"]
print("mushrooms" in requested_topping)
print("pepperoni" in requested_topping)

# A value not list
banned_users = ["gabriel", "max", "andrik", "quevedo", "chris"]
user = "pedro"
print (user not in banned_users)

# cariables de tipo BOOLEANOS
game_active = True
can_edit = False

"""
    if stamens

    if condition:
        do something
    if condition
        do something (True)
    else:
        do someting(False)
"""
# preguntar la edad del usuario y decilre si tiene edad para votar
# input("") -> str
age = int (input("\n\nEscribe tu edad"))
print(f"\nTu edad es: {age}")

if age>=18:
    print("Puedes votar")
else:
    print("eres muy joven")