'''
En este tipo de bucle vamos a tener un numero determinado de iteraciones. A priori vamos a saber cuantas veces va a iterar.
Otro punto importantisimo es que trabaja con colecciones. Ejemplo: diccionarios, listas, tuplas, conjuntos. Tambien con strings 

'''

#Veamos un ejemplo sencillo. Vamos a declarar una variable de tipo array:

# my_list = ['Colombia','Islandia','Indonesia','Canada','Chile']


# for each_value in my_list: #Aqui la variable "each_value" es la "variable de control" que recorrera la lista desde el indice 0 hasta el ultimo indice
#     print(each_value) #Aqui imprimiriamos el valor que se almacene en la "variable de control" por cada iteracion hasta terminar la totalidad de elementos del array
#IMPORTANTE: Si en vez de poner que se imprima el contenido de la variable de control, pongo cualquier otro mensaje, este se imprimira la cantidad de elementos que tenga el array
# Quiere decir que si el array tiene 3 elementos, el mensaje se imprimira 3 veces
    
#Si por ejemplo lo hiciermos con strings el loop va a iterar la cantidad de caracteres que tenga el string

# for i in 'Esteban': #Aqui el string "Esteban" tiene 7 letras. Va a iterar entonces 7 veces
#     print(i) #Es muy normal que la variable de control en ciclos FOR se nombre como "i", sin embargo podemos llamarla como queramos
    #   print(f'{i}', end= "")  # Si quisieramos que todos los caracteres se imprimieran en una sola linea, podemos:

    

#Ahora vamos a crear un ciclo FOR con una condicional dentro que evalue si el elemento dentro de la lista es par o impar:
 
# my_numbers = [1,10,7,3,9,2,6,4]   
    
# for i in my_numbers:
#     rem = i % 2 #Aqui estamos usando el operador "%" modulo y si al dividir el numero por 2 su residuo es cero, siempre entonces sera un numero par.
#     if rem == 0:
#         print(f'{i} es par')
#     else:
#         print(f'{i} es impar')
        

#Tener en cuenta que aqui tambien podemos hacer uso de la funcion "range la cual veremos un poco mas adelante", entonces un ejemplo simple seria algo como:

for i in range(1,5):
    print(i)



# #Veamos como recorrer un diccionario
# mi_diccionario = {"nombre":"Samantha", "profesion":"publicista", "edad":33, "color de piel":"canela"}

# print(f'{mi_diccionario.items()}')
# for i in mi_diccionario:
#     print(f'{i}')


# for clave,valor in mi_diccionario.items():
#     print(f'La clave es {clave}, y el valor es {valor}')
    # print(f'{i} --> {mi_diccionario[i]}')