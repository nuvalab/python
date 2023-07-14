
'''
# Otro ejemplo

def hello(): #Aqui estamos definiendo una funcion sencillita que imprimirá un mensaje que dice "Hello Esteban"
    print('Hello Esteban')


# Ahora veamos como llamar la funcion, porque de lo contrario no se nos mostrara nada:
hello() #Esta es una forma muy basica de llamar la funcion. Podemos llamarla todas veces que queramos, ejemplo:
hello()

#IMPORTANTE: La funcíón se llama despues de haberla definido. Recordar que el codigo se ejecuta de forma descendente entonces si primero llamamos la función
# y luego la definimos. Va a sacarnos un error. Debe hacerse de la forma que estamos viendo aqui: primero la definimos, luego la llamamos


#Voy a imprimir un espacio:
print("--------------------------------------")


#Ahora veamos que podemos llamar una función desde dentro de otra función

def otra_funcion():
    print("A continuación vamos a llamar otra función desde esta función:")
    hello()


# Como deciamos anteriormente, debemos llamar la función para que se ejecuten las lineas/la logica que tiene dentro
otra_funcion()


#Tambien podemos llamar una variable desde dentro de una función. Siempre y cuando esta variable sea global (Este por FUERA de una funcion)
print("--------------------------------------")

'''

'''

#Variables Locales y Variables Globales


#mi_variable=27 #Dado que esta variable esta por fuera de cualquier función, condición etc, se le llama "variable Global"

def llamando_variable():
    global mi_variable
    mi_variable=27 #Si esta variable estuviese aqui dentro, se le llama "variable local", y unicamente puede ser llamada por esta misma funcion. Sin embargo podemos volverla global con la linea anterior
    print(f'A continuación vamos a imprimir el valor de la variable "mi_variable": {mi_variable}')
    
#Llamamos la función que acabamos de crear:
llamando_variable()

def llamando_variable_dentro_funcion():
    print(f'Vamos a llamar la variable que hay dentro de la función "llamando_variable": {mi_variable}')
    
#Llamamos la función:
llamando_variable_dentro_funcion()


#IMPORTANTE: El profe dice que NO SIEMPRE ES BUENA IDEA convertir una variable dentro de una función a GLOBAL, porque no queremos que se pueda leeer desde cualquier función. 
'''




def get_add(a,b): #Aca le llamamos "Parametros" a "a" y "b"
    aresult=a+b
    print(f'The addition of {a} and {b} is: {aresult}')


def get_sub(a,b):
    sresult=a-b
    print(f'The sub of {a} and {b} is: {sresult}')


def main():
    a=eval(input('Enter your first num: '))
    b=eval(input('Enter your second num: '))
    get_add(a,b) #Aca le llamamos argumentos a "a" y "b"
    get_sub(7,3)

main()

