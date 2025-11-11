"""
    Slicing a list
"""

players = ['charles', 'martina', 'michael', 'florence', 'eli']
print("Lista Original: ", players)

print("lista original: ", players[0:3])
print("lista original: ", players[1:4])
print("lista original: ", players[:4])
print("lista original: ", players[2:])
print("lista original: ", players[-3:])
print("lista original: ", players[5:2])
print("lista original: ", players[-3:-1])

"""
    Slinsing en un for
"""
players= ['charles', 'martina', 'michael', 'florence', 'eli']
print("Aqui se presenta los primeros 3 jugadores del equipo")
for players in players[0:3]:
    print(players.title())

"""
    copiando una lista
"""
my_foods = ["pizza", "tacos", "falutas", "gorditas"]
# my_foods = my_foods # Error: no es la manera de copiar
my_foods_1 = my_foods[:]
my_foods_2 = my_foods.copy()
my_foods_3 = list(my_foods)