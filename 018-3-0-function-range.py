# Esta función crea una lista inmutable de numeros enteros (que no se modifica en el tiempo) en sucesión aritmetica.

# Vamos a definir un range del tipo "range(stop)"
print(range(5))
print(list(range(5)))

# A continuación veremos como con un ciclo FOR podemos recorrer un rango
# for i in range(5): #Aqui estamos indicando que el rango/array va a contener hasta el numero 5-1, osea hasta el 4.
#     print(i)

print(list(range(2,10))) #Aqui estamos indicando que vamos a iniciar desde 2 y que el rango/array va a ir hasta 10 -1, osea hasta 9.

# Ahora vamos a crear un rango/array donde indicamos que vamos a iniciar con el numero 1, vamos a imprimir hasta el numero 20-1, y vamos a imprimir con un intervalo de 2 en 2
print(list(range(1,20,2)))


print(list(range(10,2))) #Yo antes pensaba que el segundo numero, osea el "2" era la cantidad de elementos del array, pero esto muestra que no.
# Lo anterior porque sino se imprimiria el 10 y el 11, eso serian dos elementos. Sin embargo no muestra nada. Veamoslo mas claro:

#Debemos tener en cuenta que los elementos de un array se muestran de izquierda a derecha, osea que si le decimos que inicie desde el numero 10, y vaya
# hasta el numero 2-1, no tiene sentido. Veamos como es posible mostrar la lista pero en orden inverso:
print(list(range(10,2,-2))) # Con el "-2" al final, indicamos que vaya en orden inverso del 10 al 3, pero de dos en dos, sin embargo se imprimira hasta el 4, porque estamos indicando que vaya de dos en dos, y despues del 4 iria entonces, 2, pero 2 no se imprime.


print(list(range(-2,-10,-1))) #En este caso si quiero imprimir estos numeros negativos debo indicar el intervalo. De lo contrario si lo pongo de la siguiente forma, me tira una lista vacia:
print(list(range(-2,-10)))


# Si por ejemplo con un bucle FOR queremos validar cual es el index de cada elemento de un array podriamos hacer algo como lo siguiente:

my_array = [5,3,'Esteban',1,'Maria']

for i in range(len(my_array)): #Aqui cuando decimos (len(my_array)) estamos indicando que el rango corresponde al total de elementos que tiene el array al que llamamos "my_array   "
    print(f'El index {i} corresponde al elemento {my_array[i]}') #Cuando indicamos {my_array[i]} estamos diciendo que nos muestre el elemento que pertenece al indice en el que este la variable de control "i" en cada iteracion
    