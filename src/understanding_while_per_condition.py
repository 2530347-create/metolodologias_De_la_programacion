"""
    vamos a realizar un programa que deina un PIN para dar acceso al usuario


    El usuario va a tener que colocar un pin especifico con intentos para colocarlo bien

    si el ususario sobrepasa este maximo de intentos se le va a blowuera el accseso y cuenta
"""
CORRECT_PIN = "1234"
MAX_ATTEMPTS = 3
attempt = 0

while attempt < MAX_ATTEMPTS:

    user_input = input("ingresa tu PIN")

    if user_input == CORRECT_PIN:
        print("correcto")
        break
    else:
        attempt+=1
        reamining_attempts = MAX_ATTEMPTS - attempt
        if reamining_attempts > 0:
            print("ingresa un pin no valido")
            print(f"te queda {reamining_attempts} intentos")
        else:
            print("cuanta bloqueada")