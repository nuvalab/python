#Funciones para modificar nuestros strings

my_string1='Hola Maria'
my_string2='HOLA ESTEBAN'
print(my_string1)
print(my_string1.lower()) #Con esta funcion puedo convertir todos los caracteres a minusculas
print(my_string1.upper()) #Con esta funcion puedo convertir todos los caracteres a mayusculas


#Como hemos visto en otras ocasiones tambien podemos crear una nueva variable donde su valor sea el metodo o funcion, y luego imprimir dicha variable
my_string_lower=my_string2.lower() #En esta variable estamos convirtiendo el valor de la variable "my_string2" a minusculas. En este caso el valor de dicha variable es un "string"
print(my_string_lower)


#Si queremos saber las diferentes funciones/metodos/operaciones que tenemos disponibles para variables de tipo string, podemos poner:
print(dir(my_string2))


#Utilicemos otro que nos va a mostrar unicamente la primer letra en mayuscula:
print(my_string2.title())