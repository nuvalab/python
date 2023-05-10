#Estos operadores de comparación siempre nos arrojaran un valor booleano de "True" o "False"
a=5
b=3
result_number= a < b
print(result_number)


#Tambien podemos comparar strings

string_1='Esteban'
string_2='Samantha'
result_string= string_1 == string_2 #Aqui estamos preguntando que si el valor de la variable "string_1" es igual al valor de la variable "string_2"
print(result_string)


#Veamos como saber el valor ASCII de una letra o caracter
print(ord('a'))
print(ord('b'))


#Tambien podemos hacerlo a la inversa (Si ponemos el numero ASCII va a decirnos cual es el caracter que le corresponde):
print(chr(97)) #En este caso estamos preguntando a que letra corresponde el valor ASCII "97"

#De acuerdo a lo anterior podriamos entonces comparar dos letras de acuerdo a su valor ASCII, no se en que situaciones seria esto util, pero bueno...
letter_camparision='a' > 'b'
print(letter_camparision)