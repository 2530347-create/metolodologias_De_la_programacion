# Empty Dictionary
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
# Listas de diccionarios
# Listas en diccionarios
# Diccionarios de diccionarios