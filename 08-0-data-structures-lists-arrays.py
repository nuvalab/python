#Data Structure: Listas/Arrays

'''

# Para declarar una lista/array

my_string=['Esteban',36,"Casado",1.75]

#Se puede imprimir todo el contenido, y se imprime como cualquier otra variable
print(my_string)


#Tambien podemos darnos cuenta que tipo de "Data Structure" es (Veremos que nos dira que en este caso es tipo "List"):
print(type(my_string))


#Podemos ver las diferentes funciones/metodos disponibles para este tipo de Estructura de Datos:
print(dir(my_string))


#Tambien podemos validar cual es el numero de indice que le corresponde a un determinado elemento:
print(my_string.index('Esteban'))

#Si queremos imprimir un elemento de nuestra lista, digamos el nombre "Esteban", tenemos en cuenta que en este ejemplo a "Esteban" le corresponde el numero de indice "0":
print(my_string[0])


#Si queremos imprimir el ultimo valor del arreglo, en este ejemplo podriamos hacerlo con "3" o con "-1"
print(my_string[-1])


#Digamos que queremos seleccionar la palabra "Casado" pero ademas de esto mostrar unicamente la letra "s" de dicha palabra:
print(my_string[2][2]) #El primer 2 correponde el indice  en el que esta la palabra "Casado", este caso el numero 2. Y el segundo "2" corresponde al indice en que se encuentra la letra
#"s" en la palabra "Casado" en este caso tambien el numero "2". Al final solo deberia imprimirnos una "s"


#Si queremos por ejemplo imprimir desde el elemento en el indice "1" en adelante, entonces ponemos:
print(my_string[1:])


#No se en que esto pueda ser util pero para imprimir todos los elementos de la lista tenemos tres opciones
# print(my_string)
# print(my_string[:])
# print(my_string[0:])

#Aqui vamos a imprimir desde el indice 1, y luego el numero despues de los dos puntos "3" lo restamos con el primer numero "1", osea 3-1=2. 
#Entonces se imprimiran dos indices a partir del numero de indice 1:

print(my_string[1:3])


#Vamos a modificar uno de los elementos de la coleccion, en este caso vamos a modificar el index 0, osea "Esteban":

my_string[0]='Marley'
print(my_string)

'''




#'''

#Definamos otra "Data Structure Variable" para que veamos otras cosas que podemos hacer:

my_list=[3,5,'Esteban',7,9,11,7,13,'Esteban',15,'Esteban']


#print(dir(my_list))
#print(my_list.index('Esteban')) #Aqui estamos preguntando cual es el valor del index, para el elemento de la lista "Esteban", en este ejemplo seria el "4"
print(f'Esto es: {my_list.index("Esteban", 8)}') #El primer argumento "Esteban" es lo que vamos a buscar, el segundo argumento "8", indica a partir de que indice vamos a buscar el elemento llamado "Esteban"


#Ahora veamos una forma para contar la cantidad de veces que se repite un elemento en la lista
print(my_list.count("Esteban"))


#Con "clear" podemos limpiar o vaciar el listado de datos que contiene la variable "my_list"
#my_list.clear() #Como vemos aqui no lo estamos haciendo directamente con un print porque estamos modificando/limpiando los datos del listado. Por tanto no podemos usar "print" cuando ese sea nuestro proposito
#print(my_list)


my_new_list=my_list #Aqui estamos creando una variable donde su valor asignado es el valor de la variable "my_list". Si lo hacemos de esta forma la variable ocupara el mismo espacio de memoria RAM que la variable "my_list"
my_new_new_list=my_list.copy() #En cambio si lo hacemos de esta forma, esta variable llamada "my_new_new_list" ocupara un espacio de memoria diferente
print(id(my_list),id(my_new_list),id(my_new_new_list)) #Con "id" podemos ver que espacio de memoria ocupa una variable

#Vamos a añadir un elemento mas, llamado "Samantha" a nuestro listado:
my_list.append('Samantha') #De esta forma nos añadira el elemento al final del listado, si lo queremos en un indice especifico veremos como hacerlo mas abajo
print(my_list)


#Si queremos añadir un elemento a la lista en un indice especifico lo podemos hacer con lo siguiente:
my_list.insert(1,'Juliana')
print(my_list)


#Si queremos añadir el valor de una "lista/array" a otra ya existente, podemos hacer lo siguiente:

new_list=[327,'Aries'] #Creamos la nueva variable donde su valor es un nuevo listado que queramos
my_list.extend(new_list) #Aqui ustilizamos la funcion "extend()". Incialmente ponemos el nombre de la variable que deseamos extender y entre parentesis la variable que contiene los nuevos elementos
print(my_list) #Llamamos a la variable inicial que ya fue modificada en la linea anterior


#Para eliminar algun elemento de la lista
# my_list.remove('Esteban') #Si el elemento esta repetido en la lista, elimina el que este mas a la izquierda
# print(my_list)



#Si queremos eliminar un elemento y queremos ser especificos en cual posicion está:
print(my_list.pop(1)) #Esta operacion es de las pocas que funciona con print ya que modifica la lista. En este caso va a imprimirnos el elemento que vamos a eliminar en la siguiente linea
my_list.pop(1) #Aqui le estamos diciendo que nos elimine especificamente el elemento en el indice numero "1"
print(my_list)



#Veamos como ordenar numeros de forma ascendente o descendente. ESTO SOLO FUNCIONA CUANDO EL LISTADO SOLO CONTIENE NUMEROS ENTEROS O FLOTANTES
my_number_list=[3,27,7,15,9,1,3.7] #Aqui tuvimos que crear una nueva variable porque con la que veniamos trabajando contenia STRINGS
#my_number_list.sort() #De esta forma los ordena de menor a mayor
my_number_list.sort(reverse=True) #Si queremos ordenarlos de mayor a menor podemos usar el parametro "reverse=True"
print(my_number_list)

#'''