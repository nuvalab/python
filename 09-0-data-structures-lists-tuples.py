#Las tuplas son muy parecidas a las listas, lo diferente es que estas NO SON modificables y que se encierran entre parentesis.
# En conclusion como dice en la siguiente linea las listas son mutables/modificales, pero las tuplas son inmutables/NO modificables
#Tuples and strings are inmutable: it means that once defined you can't modify a part o them.


#Veamos como declarar las Tuplas:
my_empty_tuple=()
my_tuple=(3,4,5,['Esteban',327,7],3) #Como vems aqui estamos almacenenado una lista dentro de una Tupla

#Imprimimos el valor de la tupla
print(my_tuple)

#Si queremos saber si un elemento existe o no en la tupla, podemos hacer lo siguiente:
print(3 in my_tuple) #Nos arrojara un "True" si el valor existe, y un "False" si NO existe 


#Tambien podemos usar la funcion "len()", la cual nos indica cuantos elementos tiene la Tupla:
print(len(my_tuple))


#Podemos darnos cuenta si una tupla esta vacia o no, conviertiendo el valor de la variable en Booleano
print(bool(my_empty_tuple)) #Esta deberia retornarnos "False" ya que la lista está vacia
print(bool(my_tuple)) #Aqui deberia retornanos un "True" ya que esta contiene elementos en la lista

print(my_tuple[3]) #Aqui estamos imprimiendo el index 3 de la tupla llamada "my_tuple"
print(my_tuple[2:]) #Aqui estaria imprimiendo desde el indice 2 en adelante
print(my_tuple[:4]) #Aqui estaria imprimiendo 4 elementos de la lista
print("Test",my_tuple[2:5]) #Aqui le estamos diciendo que inicie desde el indice 2, y el segundo numero "5", se le resta a 2 (5 - 2 = 3), entonces se imprimen 3 elementos a partir del segundo indice



#Si queremos imprimir un unico elemento de la lista que incluimos dentro la tupla, podemos hacer lo siguiente
print(my_tuple[3][0]) #En este caso queria imprimir el elemento llamado "Esteban" el cual dentro de la lista tiene el indice "0"

#Si queremos ver la cantidad de elementos que tiene una tupla:
print(f'La cantidad de elementos que tiene la tupla llamada "my_tuple", son: {len(my_tuple)}')


#Para imprimir los diferentes metodos que tenemos disponbles para las tuplas:

#print(dir(my_tuple))

#Cuantas veces se repite un elemento con el mismo nombre en la lista
print(f"La cantidad de veces que se repite el numero 3 es: {my_tuple.count(3)}") #Dado que en la lista de ejemplo el numero 3 se repite dos veces, deberia darnos como resultado "2"
print('El numero de index del elemento llamado "3" (pero el 3 del final) es:',my_tuple.index(3,1)) #Aca pusimos (3,1) porque queremos saber el numero de index del "3" que esta al final ya que se repite
# entonces le indicamos que busque a partir del index "1" ya que en el index "0" esta el primer "3"

print(len(my_tuple))


#IMPORTANTE: Tambien podemos definir una tupla de la siguiente forma:
# mi_tupla = 7, #Esta seria una tupla de un unico valor
mi_tupla = 3,2,7 #Como vemos lo estamos haciendo sin los parentesis, igual con la linea mas abajo veremos que Python lo interpreta como una Tupla
print(type(mi_tupla))


#Tambien podemos convertir Tuplas a listas de la siguiente forma:

lista = list(my_tuple)
print(lista)



#Por ahi derecho veamos como convertir listas a Tuplas:

mi_lista = [3,2,7]
tupla = tuple(mi_lista)
print(tupla)