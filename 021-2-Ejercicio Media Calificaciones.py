
# alumno1 = eval(input("Ingrese la nota del alumno 1: "))
# alumno2 = eval(input("Ingrese la nota del alumno 2: "))
# alumno3 = eval(input("Ingrese la nota del alumno 3: "))
# total_alumnos = eval(input("Ingrese el numero de alumnos a evaluar: "))

# def promedio(al1, al2, al3):
#     suma = al1 + al2 + al3
#     # media = suma / total_alumnos
#     # return media
#     return suma / total_alumnos

# print(promedio(alumno1, alumno2, alumno3, 7))

# # Crear una lista vacía
my_list = []

# Solicitar al usuario los valores y agregarlos a la lista
while True:
    value = input("Ingrese un valor (o 'stop' para detenerse): ")
    if value.lower() == 'stop': #En la linea anterior necesitamos que hasta este momento sea de tipo "string" para poder hacer esta evaluación.
        break #Si el usuario pone la palabra "stop" entonces el BUCLE deja de iterar gracias a este "break" 
    value = float(value) #Aqui estamos convirtiendo el valor de la variable "value" de "string" a "flotante"
    my_list.append(value) #La función "append()" va agregando los valores ingresados por el usuario a la variable de tipo array llamada "my_list"


def promedio(mi_lista):
    suma = sum(mi_lista)
    media = suma / len(mi_lista) #La función "len()" nos tira como resultado la cantidad de elementos que tiene un array en este caso
    return f'La media de acuerdo a los valores proporcionados es: {media}'
    # return suma / len(my_list)

print(promedio(my_list)) #Aqui estamos pasando como argumento el nombre de una variable/array, la cual contiene como elementos los numeros que queremos calcular
