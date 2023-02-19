'''
Escriba un programa donde tenga una lista y que a continuación elimine
los elementos repetidos. Por ultimo mostrar la lista.

'''

my_list = [1,5,3,'Esteban',7,3,5] #Creamos la lista con algunos elementos repetidos


'''
#Dado que los sets/conjuntos, no permiten la repeticion de elementos, entonces vamos a convertir nuestra lista/array en un conjunto

my_set = set(my_list) #Aqui estamos convirtiendo el array "my_list" a un set

#Imprimimos el set/conjunto, y no deberiamos ver los elementos repetidos:

# print(my_set) #Sin embargo de esta forma se imprimirian los elementos como un "set". Si queremos imprimirlo como un array, debemos hacer lo siguiente:

# Convertimos el "set" nuevamente a un "array/lista":

my_list = list(my_set) #Aqui estamos convirtiendo el "set" a una "lista/array"

print(my_list) #Deberiamos ver entonces el set impreso como una lista/array (Sin elementos repetidos y entre corchetes).

'''

#Una forma de hacer todo lo anterior de forma mas facil y en una sola linea es:

my_list = list(set(my_list)) #Aqui inicialmente estamos convirtiendo "my_list" a un set/conjunto (Esto porque tiene prioridad lo que este dentro de parentesis), y luego
# estamos convirtiendo "my_list" nuevamente a una lista/array. Entonces en una linea estamos logrando lo que antes nos habia tomado dos lineas

print(my_list) #Imprimimos el resultado el cual no debe contener elementos repetidos, y sus elementos se muestran en el orden que el conjunto desee ya que este imprime
#de forma "desordenada"
