#En este caso vamos a validar si el tipo de variable es una u otra, si un elemento existe por ejemplo dentro de un array,

x=6
y='Hi'

#Recordemos que podemos validar el tipo de variable de la siguiente forma

print(type(x))
print(type(y))


#Entonces para comparar el tipo de variable podemos hacerlo de la siguiente forma:

type_comparision=type(x) is type(y) #Aqui estamos preguntando que si el tipo de la variable "x" es igual que el tipo de la variable "y"
print(type_comparision) #Aqui estamos llamando a la variable que declaramos en la linea anterior, esto debe darnos un valor de "true" o "false"

#Tambien podemos preguntar si un tipo de variable es diferente a otra

type_difference=type(x) is not type(y) #En este caso como si son diferentes los tipos de estas dos variables, entonces deberia darnos un "True"
print(type_difference)


#Veamos entonces ahora los Membership Operators

w=[5,9,7,3,1] #Definimos esta variable de tipo array
membership_1 = 6 in w #Aqui estamos declarando una variable cuyo valor esta preguntando si el numero "6" esta en la variable/array "w"
print(membership_1)

#Veamos otro ejemplo:

valida_java_versions=['1.6','1.7','1.8','1.9'] #Definimos el array
host_java='1.5' #Aqui estamos declarando una variable con un valor que vamos a buscar en el array anterior, haciendo uso de la siguiente linea
search_valid_java_version = host_java in valida_java_versions #Aqui estamos diciendo literalmente que si "1.5" existe en el array "valida_java_versions"
search_invalid_java_version = host_java not in valida_java_versions #Al igual que en el ejemplo anterior tambien podemos usar: "not in"
print(search_valid_java_version)
print(search_invalid_java_version)
