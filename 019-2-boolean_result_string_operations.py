#Vamos a ver algunas validaciones en Python

my_str='Esteban'
print(my_str.startswith('E')) #Aqui estamos validando si el valor de la variable "my_srt" de tipo "string" inicia con "E" mayuscula. Si es asi el resultado debe ser "True", sino es "False"
print(my_str.endswith('AN')) #Esta es similar a la anterior, sino que unicamente estamos indicando que valide si termina en "AN" (Mayuscula)
print(my_str.islower()) #Valida si todo el valor del string está en minusculas
print(my_str.isupper()) #Valida si todo el valor del string está en mayusculas
print(my_str.istitle()) #Valida si la primer letra de nuestro "string" esta en mayuscula. En esta caso es "Esteban", entonces el resultado deberia ser "True". Si pusieramos "Esteban lopez" seria "False"
# porque una de las palabras NO esta inciando en mayuscula
print(my_str.isalpha()) #En este caso se valida que todo el string este compuesto de letras del alfabeto. Si contiene caracteres extraños, numeros o espacios, el resultado seria "False"
print(my_str.isnumeric()) #Este es similar al anterior pero valida que unicamente se esten usando numeros

#Podemos ver la explicación de cada una de estas funciones usando el siguiente comando (Aunque a decir verdad no son tan buenas las explicaciones, mejor usar CHATGPT):
# (help(str))