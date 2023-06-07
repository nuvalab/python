#Podemos contar cuantas veces se repita una letra o fragmento de letras en un string
my_string1='I love the forest because is full of nature and is usually lonely'
print(my_string1.count('is')) #Aqui va a buscar cuantas veces aparece la palabra "is" en el string
print(my_string1.count('e')) #Podemos contar cuantas veces esta una letra en especifica, en este caso la letra "e"

#Podemos tambien encontrar el index de algun elemento de nuestros strings (Recordar la teoria de listas/arreglos)
my_string2='My life is full of inner peace, prosperity and health'
print(my_string2.find('p', 27, 33)) #Aqui le estamos diciendo que busque la letra entre el index 27 y el index 33, si esta en en el 27 o en el 33, lo considera como si no existiera, porque debe ester ENTRE esos dos
print(my_string2.find('iti')) #Cuanto no encuentra el caracter o cadena indicada el resultado sera siempre "-1"
print(my_string2.find('p', 33)) #Aqui le estamos indicando que nos busque la letra "p" despues del index numero 33

#Lo siguiente vamos a verlo tambien mas adelante
print('life' in my_string2) #Aqui estamos preguntando que si la palabra life se encuentra en el valor de la variable "my_string2", si es asi nos devuelve un "true" sino un  "false"