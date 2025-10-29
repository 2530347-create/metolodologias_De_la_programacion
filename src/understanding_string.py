"""
"Variables de tipo string

 Un string es de manera sencilla una serie de caracteres. En Python, todo es un string.Ejemplos:

"Esto es un string"

'Esto también es un string'

*Le dije a un amigo "Python es mi lenguaje favorito"

"El lenguaje 'Python' lleva el nombre de Monty Python, no de la serpiente."

name = "clase de programacion"
"""
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


frist_name = "charly"
last_name = "mercury"
full_name = frist_name + " " + last_name
print(full_name)
print(full_name.title())