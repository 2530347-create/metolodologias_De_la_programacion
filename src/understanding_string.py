"""
"Variables de tipo string

 Un string es de manera sencilla una serie de caracteres. En Python, todo es un string.Ejemplos:

"Esto es un string"

'Esto también es un string'

*Le dije a un amigo "Python es mi lenguaje favorito"

"El lenguaje 'Python' lleva el nombre de Monty Python, no de la serpiente."


"""
name = "clase de programacion"
print(name)


"""
 Un metodo es una accion de python puede realizar en un fragmento
de datos o sobre una variable

 El punto . despues de una variable seguido de un metodo titel() 
dice que se tiene que ejecutar el metodo titel () de la variable name

 Todos los metodos van seguidos de parentesis porque en ocasiones
necesitan informacion adicional para funcionar, la cual iria dentro
de los parentesis.
En esta ocasion, el metodo . titel () no requiere informacioln 
adicional para funcionar.
"""

print("metodo upper: ", name.upper())
print("metodo lower: ", name.lower())

# Concatenación

frist_name = "charly"
last_name = "mercury"
full_name = frist_name + " " + last_name
print(full_name)
print(full_name.title())

"""
 UN whithespace se refiere a cualquier carcacter que no 
 se imprime, es decir, un espacio, tabuladores y finales de linea.
 Los whithespace se utiliazan comunmente para organizar 
 las salidas de tal manera que sea amigable de leer o ver 
 para el usuario.

  Ejemplos:
   -Tabuladores: \t
   .salto de lineas: \n 
"""

print("whitespace Tabulador")
print("python")
print("\tpython")
print("\t\tpython")
print("whitespace Salto de linea")
print("Languages: \n\tPyhon\nC\n\tJavascript")


# Eliminacion de espacios en blanco
print("\nEliminacion de espacios en blanco")
programming_languages = " Pyrthon "
print(programming_languages)
print(programming_languages.rstrip())
print(programming_languages.lstrip())
print(programming_languages.strip())

# Syntax Error con String
message = "Una fortaleza de python es su comunidad"
print(message)
message = "Una fortaleza de python es su comunidad"
print(message)


# f-strings
famous_person = "Taylor swift"
message = f"{famous_person} una vez dijo me voy al oxxo en avion"
print(message)  

print(f"{famous_person.upper()} una vez dijo me voy al oxxo en avion")

#  Actividad

"""

 Elige el nombre de una persona famosa (quie quieras)
 Elige una cita famosa de esta persona
 iguala ambos strings a una variable.

 1) Realizar la cocatenacion utilizando el aigno de suma
 2) Realiza la cocatenacion utilizando fstrings

"""
famous_person = "Nikola tesla"
quote = "si tubiera el tiempo suficiente crearia una maquina del tiempo"
famous_message = famous_person + " " + quote
message = famous_person+ "" +quote
print(message) 

f_string_message = f"{famous_person}  {quote}"
print(f_string_message)
