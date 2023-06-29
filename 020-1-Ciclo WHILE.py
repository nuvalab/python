#A continuación vamos a ver un ejemplo del bucle While. En Python existen dos bucles el "while" y el "for"

# El bucle se ejecutará siempre y cuando la condicion sea verdadera. La estructura basica seria algo como:

# sourcery skip: while-to-for
'''
while True: #Mientras que la condicion sea verdadera, ejecute el siguiente codigo/itere
    codigo a ejecutar
'''

#Veamos un WHILE basico:

# i = 0

# while i < 5:
#     print(f"El valor de 'i' es: {i}")
#     i += 1 #En este caso modificamos el valor de "i" en cada iteración para evitar un BUCLE INFINITO



#Vamos a crear un codigo donde preguntamos a un usuario algo, y hasta que no responda correctamente no salimos del BUCLE WHILE (Entonces vamos a iterar un numero INDETERMINADO de veces):

# pregunta = input("¿Cual es la capital de Canada?: ")

# while pregunta.lower() != "ottawa":
#     pregunta = input("Respuesta equivocada, vuelve a intentar: ")

# print("Felicitaciones, has dicho la respuesta correcta!")


pregunta = input("¿Cuantos dias tiene un año?: ")

while pregunta != "365":
    pregunta = input("Respuesta equivocada, vuelve a intentar: ")

print("Felicitaciones, has dicho la respuesta correcta!")
