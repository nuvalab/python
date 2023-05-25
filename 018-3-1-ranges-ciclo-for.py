'''
En este Script vamos a explicar lo que es la funcion "range()"

Algunos ejemplos:

range(7) Nos muestra los numeros del 0 al 6 (No incluye el numero 7).
range(1,8) Nos muestra los numeros del 1 al 7 (No incluye el 8)

Nota: Lo anterior indica que nunca se incluirá el numero mas a la derecha, osea que si pongo "range(1,9)", el rango ira del 1 al 8, osea que no se incluye el "9"

range(1,10,2) nos da numeros impares empezando del 1 al 9. En ese rango empezaria en 1, y luego imprime cada dos numeros. Entonces empieza con el 1, continua con el 3, luego con el 5, etc.
range(7,0,-1) este nos permite contar a la inversa. En este caso imprime los numeros del 7 al 1, y no se incluye el "0". El "-1" sirve precisamente para imprimir 1 a 1 pero en orden inverso. Osea: 7,6,5,4,3,2,1


'''
#Veamos entonces como declarar "ranges":
# r1 = range(7,0,-1) #En este caso creamos una variable llamada "r1", a la cual le asignamos como valor un rango


#Para imprimir los valores de la funcion "range()" debemos usar otra funcion que se llama "list()"
# print(list(r1)) #Aqui vemos que como argumento para la funcion "list()" le estamos pasando el nombre de la variable "r1"



# Veamos otro ejemplo:
# r2 = range(1,10,2)
# print(list(r2))
#Nota: Hasta aqui vemos que el resultado que se imprime de estos rangos es una lista o array.


#Veamos entonces como podemos imprimir cada valor de esa lista con un FOR:
# for i in r1:
#     print(i)
    

#Incluso podemos definir el rango en el mismo FOR:
# for i in range(1,15,2):
#     print(i)

#Vemos que si ponemos un PRINT indicando un "STRING" nos imprime dicho "STRING" la cantidad de veces que especifiquemos en el "range()"
for i in range(3):
    print(f'FUCK! {i+1} times')
    