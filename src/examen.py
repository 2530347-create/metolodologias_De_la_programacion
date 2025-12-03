"""
sep de python
"""


numer =0
cantidad=0.0
minimo= None
maximo=None

while True:
    print("para salir escreibe exit: ")
    user_input = input("Ingresa una cantidad : ")

    if user_input == "exit":
        break
    
    try:
        value = float(user_input)
    except ValueError:
        print("ERROR")
        continue
    except KeyboardInterrupt:
        print("Salida")
        break

    numer+=1 
    cantidad += value

    if minimo is None or value < minimo :
        minimo = value


    if maximo is None or value > maximo :
        maximo = value


print("cantidad ingresada de numeros: ", numer)
print("suma: ", cantidad)
print("minimo: ", minimo)
print("maximo: ", maximo)