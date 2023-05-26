#Si por ejemplo queremos imprimir cada caracter de un cadena de string en un salto de linea por caracter, tenemos las siguientes opciones

#Definimos primeramente la cadena de caracteres:

# my_string = "This is my beautiful life"

#Podriamos lograrlo facilmentente con la funcion "join()":

# print("\n".join(my_string)) #Lo que pongamos entre las comillas, es lo que va a ir entre cada caracter. En este caso estamos incluyendo un salto de linea "\n"

#Tambien podemos lograrlo con un ciclo FOR

# for each_character in my_string: #Aqui ha la variable de control le hemos llamado "each_character", normalmente se le llama "i", pero como vemos podemos llamarla como queramos
#     print(each_character)
    
# Tambien podriamos hacer lo mismo para una lista/array:

# my_list_1 = [3,27,5,9,7]

# for each_element in my_list_1:
#     print(each_element)
    

# Tambien por ejemplo con una lista que dentro contiene tuplas

# my_list_2 = [(3,9),(1,7),(5,9)]

# for each_item in my_list_2:
#     print(each_item)
    

# Algo interesante con relación al FOR anterior es que podemos extraer de la tupla el primer o segundo valor si queremos, pero primero debemos entender lo siguiente:
# Vamos a declarar una variable de tipo Tupla, y veremos que al nombre le podemos asignar como dos nombres por decirlo asi:

# t1,t2 = (3,27) #En este caso t1 seria como el nombre del primer elemento "3", y t2 seria el nombre del segudo elemento "27", veamos mas claramente haciendo un "print":
# print(t2) #Aqui deberia imprimirse el elemento "27"


#Ahora veamos como lo anterior funciona con un FOR:

# my_list_3 = [(1,4),(3,7),(9,1)] #Veamos que aqui cada tupla contiene dos elementos. Si hay una que contenga mas de dos va a mostrarnos un error

# for t1,t2 in my_list_3:
#     print(t1) #Aqui se imprimiria el primer elemento de cada tupla, y se imprimiria como entero. Si quisieramos imprimir ambos seria algo como "print(t1,t2)"


#Veamos ahora como imprimir los key values (key+value) en los diccionarios haciendo uso de un FOR

#Si lo hicieramos de la siguiente forma unicamente va a imprimirse los keys:

# my_dic_1 = {'a':1,'b':2,'c':3}

# for each_keypair in my_dic_1:
#     print(each_keypair) #Aqui veremos que unicamente se imprimira el key

'''
Para solucionar lo anterior tenemos las siguientes funciones:

my_dic_1.keys() --> Esta muestra unicamente las claves, osea en este ejemplo: a, b, c # Como vemos al inicio de la funcion ponemos el nombre de la variable con la que queremos trabajar. En este caso yo habia nombrado una llamada "my_dic_1"
my_dic_1.values() --> esta muestra unicamente los valores, osea en este ejemplo: 1, 2, 3
Pero si queremos mostrar tanto el key como el value: my_dic_1.items()

'''

# for each_keypair in my_dic_1.items():
#     print(each_keypair) #Aqui se nos imprimiran como tuplas.
    
#Si quisieramos imprimirlo como string/entero y no como tupla podriamos hacerlo de la forma que ya habiamos visto

# for key,value in my_dic_1.items():
#     # print(key,value)
#     print(f'{key}: {value}')