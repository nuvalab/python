'''
Aqui tenemos los diferentes operadores logicos existentes (Almenos los mas usados):

AND ---> Todas las condiciones deben ser cumplidas para obtener un TRUE
OR ---> Una de las condiciones debe cumplirse para obtener un TRUE
NOT ----> Niega el resultado final. Por ejemplo: si el resultado es TRUE lo pasa a FALSE y viceversa

Nota: estos siempre nos dan como resultado un valor booleano de "True" o "False"

'''

#Operador Logico AND

comparacion_1 = 2 < 3 and 1 < 5 and 3 < 7 #Dado que aqui todas las condiciones se cumplen, el resultado deberia ser entonces "True". Si alguna de las condiciones no se cumpliera seria "False"
print(comparacion_1)


#Otra forma de hacer el AND que vemos en la linea 14, y esta es para ahorrar codigo:
comparacion_2 = all([2<3,1<5,3<7]) #Aqui la palabra "all" equivaldria a un "AND"
print(comparacion_2)


#Operador logico OR

comparacion_3 = 2 < 3 or 10 < 5 or 3 < 7 #Aqui con que solo se cumpla una condicion nos daria un resultado "True". Vemos que la segunda condicion no es verdadera dado que 10 no es menor que
# 5, sin embargo nos retornara un "True"
print(comparacion_3)


# #Otra forma de hacer el OR que vemos en la linea 25, y esta es para ahorrar codigo:
comparacion_4 = any([2<3,10<5,3<7]) #Aqui la palabra "any" equivaldria a un "OR"
print(comparacion_4)


#Operador Logico NOT
#Si queremos por ejemplo negar el resultado de la variable "comparacion_4", el cual es "True" en el momento:
comparacion_4 = not any([2<3,10<5,3<7]) #Aqui como vemos estamos anteponiendo la palabra "not" antes de "any". Dado que el resultado original es "True", deberia darnos un "False"
print(comparacion_4)