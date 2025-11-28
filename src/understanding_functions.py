### FUNCIONES
# Las funciones son bloques de codigos para realizar
# una tarea en especifico

# cuando queremos realizar tareas en especifico
# en la funcion, tenemos que llamr el nombre de la funcion que realiza la accion

"""
    sintaxis de una funcion

    def nombre_funcion():
        acciones

    Ejemplo: definir una accion que salude a alguien
"""
def gretting_Andrik():
    """
        funciona para saludar a una persona llama Andrik
    """
"""
    for i in range(0,5):
        print("hola Andrik")
"""
gretting_Andrik()

# Ejemplo de una funcion que genere el nombre completo de una persona y regresarlo


def create_full_name(first_name, last_name, middle_name=""):
    full_name = f"{first_name} {middle_name.strip()} {last_name.strip()}".title()
    return full_name 

first_name = input("Dame tu primer nombre: ")
middle_name = input("Dame tu segundo nombre: (ENTER si no tinenes segundo nombre)")
last_name = input("Dame tu apellido: ")

# parametrso posicionales
generate_fullname = create_full_name(
    user_frist_name.strip().lower(),
    user_last_name.strip().lower(),
    user_middle_name.strip().lower())
print(generate_fullname)

# argumento llave
generate_fullname_2 = create_full_name(
middle_name = user_middle_name,
first_name = user_frist_name,
last_name = user_last_name)
print(generate_fullname_2)

"""
manejo de datos (.txt, csv, json, excel, works, pdf)
argas via consola (sys)
click en python - comand line interface
testing - casos prueba (borde, validos, invalidos)
"""