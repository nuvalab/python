#Este tipo de coleccion se basa en clave/valor. Veamos como se define un diccionario
'''
dictionarie={}#Esto seria un diccionario vacio
print(type(dictionarie)) #Con esto podemos validar el tipo de variable. En este caso es de tipo diccionario
print(bool(dictionarie)) #Con esto podemos darnos cuenta si el diccionario esta vacio, si es asi nos apareceria un "False"

'''


'''
#Vamos a definir un diccionario con info dentro
my_dict={'fruit':'apple','animal':'fox','1':'one','2':'two'}
#Otra forma de crear un diccionario:
diccionario = dict(nombre="Esteban",nacionalidad="Colombiano",profesion="Marketer")

print(my_dict) #De esta forma imprimimos todo el diccinario
print(my_dict['fruit']) #Aqui estamos indicando el nombre de la clave/key que queremos consultar. Entonces nos mostrará su respectivo valor/value
print(my_dict.get('Color')) #Esta es otra forma de consultar alguna clave del diccionario, el resultado es el mismo de la linea anterior, pero si digamos la clave no existe en el diccionario
#el resultado impreso sera "None" en vez de un error de codigo. Tambien podemos especificar un mensaje a mostrar en caso de que la clave no exista. Ejemplo
# print(my_dict.get('Color',"Esta Clave no existe en el diccionario"))
# Tambien podemos buscar si una clave/key existe o no dentro de un diccionario, y que nos devuelva como respuesta un valor Booleano:
print(10 in my_dict) #Como indique en la linea anterior este solo sirve para los "Keys", si queremos validar en los "Values", debemos hacerlo de la siguiente forma:
print("apple" in my_dict.values())


#Si queremos ver todas las operaciones/metodos disponibles para los diccionarios:
#print(dir(my_dict))

#Si queremos eliminar todos los datos dentro de un diccionario tenemos el metodo "clear":
#my_dict.clear()
#print(my_dict)

#Si queremos añadirle una nueva clave/valor al diccionario:
my_dict['color']="blue" #En este caso "color" seria la nueva clave, y "blue" el nuevo valor
# Nota: Si queremos modificar alguna de las claves o valores existentes en el diccionario, lo hariamos de la misma forma que lo hicimos en la linea anterior
print(my_dict)

#Si quiero mas adelante puedo modificar el valor de la clave que acabo de añadir al diccionario
my_dict['color']="yellow"
print(my_dict)

'''


'''

#Si queremos imprimir el listado de claves que tenemos en nuestro diccionario:
print(my_dict.keys())

#Si queremos imprimir dichas claves en formato "String", podemos hacerlo con ayuda de un ciclo FOR:

for i in my_dict.keys(): #Dado que la funcion "keys()" muestra por defecto el resultado en una lista/array, podemos entonces recorrerla con un FOR
    print(i)

#Si queremos imprimir el listado de valores que tenemos en nuestro diccionario:
print(my_dict.values())
#Si queremos ver el listado de "items" el cual en este caso es como encerrar cada clave con su respectivo valor entre parentesis:
print(my_dict.items())

#Dado que el resultado de la linea anterior se nos muestra en Tuplas, podemos entonces con un LOOP recuperar la clave y valor de la siguiente forma:

for k,v in my_dict.items: #Las variables de control "k" y "v" pueden ser nombradas como queramos
    print(f'Key is {k} and Value is {v}')


#Si queremos saber cuantas claves/valores hay en el diccionario
print(len(my_dict))

'''



'''

#Si queremos copiar el contenido de la variable "my_dict" y almacenarlo en un espacio de memoria diferente:
my_new_dict=my_dict.copy()
print(id(my_dict),id(my_new_dict)) #De esta forma validamos que ambas variables estan en espacios de memoria diferente


#Si por ejemplo queremos crear un diccionario y añadir su contenido a un diccionario ya existente:
my_status={'name':'Esteban','status':'single'}
my_dict.update(my_status) #Aqui estamos indicando que el contenido de la variable/diccionario "my_status", se lo añadamos a la variable/diccionario "my_dict"
print(my_dict)


#Si queremos eliminar alguna de las key/value:
my_dict.pop('fruit') #Aqui estamos eliminando la clave llamada "fruit", esto por consiguiente eliminara tambien su valor "apple"
#Tambien podemos eliminar de la siguiente forma:
# del(my_dict["fruit"])
print(my_dict)

'''



'''

#Veamos como crear una lista y basados en ella crear un diccionario. Tambien veremos como asignar un valor a los elementos/keys de la lista
keys=['a','e','i','o','u']
new_dict=dict.fromkeys(keys) #Con esta linea estamos indicando de cual lista/array vamos a crear un diccionario. En este caso le estamos diciendo que de la lista llamada "keys"
print(new_dict)
new_dict['a']='First Alpha' #Aqui estamos asignando al "key" llamado "a" un valor llamado "First Alpha"
print(new_dict)

'''



'''

#Vamos a explicar el metodo "setdeafult()"

materiales = { #Aqui vemos una forma un poquito diferente de declarar diccionarios
    "cuadernos": 7,
    "lapices": 2,
    "borradores": 3,
}

articulo = input("Ingrese el nombre del articulo: ") #Esto es una variable de entrada para que el usuario indique el nombre del articulo dentro de los materiales

unidades = materiales.get(articulo, 0) #Aqui cuando le ponemos como argumento ola variable "articulo", a la funcion "get()", le estamos indicando que busque en el diccionario la clave indicada por el usuario.
# Adicional a lo anterior, el argumento "0" significa que si el usuario ingresa una clave que no existe en el diccionario, el valor por defecto a mostrar sera cero

#Si queremos que el valor ingresado por el usuario se convierta en una clave del diccionario, podemos hacer entonces uso de la funcion "setdefault()":
# unidades = materiales.setdefault(articulo, 0)


print("Hay {} unidades de {}".format(unidades, articulo))

'''




'''

#Dentro de un diccionario podemos almacenar, listas, tuplas, otros diccionarios:

mi_diccionario = {"Esteban":{"Estado":"Soltero","Nacionalidad":"Colombiano"},"Maria":["Casada",21]}
print(mi_diccionario["Esteban"]) #Aqui se mostraria el valor de la clave "Esteban", el cual lo pusimos como diccionario
print(mi_diccionario["Maria"]) #Aqui se mostraria el valor de la clave "Maria", el cual lo pusimos como lista/array

'''