#Ahora vamos a ver como definir y llamar una funcion. Estas son usadas cuando vamos a usar la misma logica multiples veces durante la ejecución de un programa

'''
La estructura/sintaxis basica para definir una función es la siguiente:

def nombre_de_la_funcion(): #Con la palabra reservada "def" creamos la función. En este caso el nombre que le hemos puesto es "nombre_de_la_funcion". Entre parentesis podemos asignar parametros a la funcion
    print("") #Debajo del nombre de la funcion y sus parametros, ponemos la lineas que se ejecutaran una vez llamemos la función
    
Nota: tal como vemos en la linea anterior, todas las lineas que esten por debajo del nombre de la función van indentadas

'''


#Definir función:

def suma(a,b,c): #Aqui establecemos los PARAMETROS de la función entre parentesis
    resultado = a + b + c
    return resultado
    # print(resultado)
    # print("Hola")

result = suma(7,3,2) #Aqui estamos creando una variable cuyo valor es el resultado de la función. Esto es util para el caso en el que queramos imprimir o trabajar con este resultado mas abajo en el codigo
print(result)


#LLamar función:
# print(suma(3,5,5)) #Aqui le pasamos los ARGUMENTOS a la función entre parentesis
# print(suma(5,1,1))
# suma(3,2,1)


'''
"print" se utiliza para mostrar información en la consola, mientras que "return" se utiliza para devolver un valor específico desde una 
función para ser utilizado más adelante en el programa. La elección entre ellos depende de si deseas simplemente mostrar información o almacenar 
y utilizar un valor en otro lugar del programa.

En conclusión:  el "return" nos va a devolver el valor de la función, y ese valor podemos utilizarlo mas adelante en el codigo, 
y el "print" solo nos va a imprimir el valor de la funcion en pantalla. Se recomienda entonces como buena practica usar "return" la mayoria del tiempo


#IMPORTANTE: La funcíón se llama despues de haberla definido. Recordar que el codigo se ejecuta de forma descendente entonces si primero llamamos la función
y luego la definimos. Va a sacarnos un error. Debe hacerse de la forma que estamos viendo aqui: primero la definimos, luego la llamamos

'''