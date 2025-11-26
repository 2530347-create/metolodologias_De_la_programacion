# Empty Dictionary
"""
homer_0 = {"color": "yellow",
 "bag": "maggie-bag",
  "hair": "black",
   "dress": "green",
    "mom": False }

print(homer_0)
print(type(homer_0))

marge = {"color": "yellow",
 "bag": "homer-donut",
 "hair": "black",
  "dress": "green",
   "mom": True}
gun:0= {"scar": "yellow-orange", "headshot": 1.5}
print(marge["headshot"])

# Modifying an elements of a diccionari
homer_0["color"]="blue"
## Add elements to a dictionary

homer_0["x-psition"]=15
homer_0["y-psition"]=25
homer_0["z-psition"]=10
homer_0["name"]="omer"

marge["x-psition"]=16
marge["y-psition"]=26
marge["z-psition"]=10
print(homer_0)

## Looping though items

for key, value in homer_0.items():
    print(f"The key {key} has value {value} ")


for key, value in homer_0.key():
    print(f"The key {key} has value {value} ")


## Looping though key
for key in homer_0.key():
    print(key)


## Looping though value
for value in homer_0.value():
    print(key)

# NESTING
## Listas de diccionarios
##Listas en diccionarios
## Diccionarios de diccionarios
"""

print("informacion del cobenant")

print()


covenant_grut = {
    "color": "orange",
    "weapon": "plasma-gun",
    "armament": "plasma.granade",
    "health":2,
}

covenant_elite = {
    "color": "orange",
    "weapon": "plasma-sword",
    "armament": "plasma.granade",
    "health":7,
}

covenant_jackal = {
    "color": "gray",
    "weapon": "plasma-sword",
    "armament": "plasma.granade",
    "health":5,
}

# Listas de diccionarios
covenants = [
    covenant_grut,
    covenant_elite,
    covenant_jackal
]

for covenant in covenants:
    print(covenant)
    for key, value in covenant.items():
        print(key,value)
    print()

##Listas en diccionarios
students = {
    "santiago":  ["reprobado", "prepa1", "rebelda"],
    "jorge-crack":  ["aprobado", "cbtis271", "goleador"],
    "gabriel":  ["aprobado", "119muerte", "crack-fornite"],
}

senesor = {
    "temperature": {
        "id": "temp_1",
        "location": "aula 105",
        "value": 25,
        "unit": "celsius",
    },
    "humedad": {
        "id": "hum",
        "location": "aula 103",
        "value": 60,
        "uniti":"percentaje",
    }
}

print("tempetatura")
