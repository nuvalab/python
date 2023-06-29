'''

lista = []

for i in range(10):
    lista.append(i)

print(lista)

'''


'''

#Veamos lo que es un "comprenhension list"

# lista_a = list(range(10))
lista_a = [i for i in range(10)] #El primer "i" representa al valor que va a asignarse en la lista, y el segundo "i" es simplemente la variable de control que recorre la lista. Osea que el primer "i" es como cuando usamos "variable.append(i)". Tambien debemos tener en cuenta que debe llamarse igual que la variable iteradora

print(lista_a)

# Nota: Más información sobre "comprenhension lists": https://www.youtube.com/watch?v=Nm9WY64VHRA

'''

#Ahora si veamos como funciona la funcion "zip()"

list_a = [i for i in range (10)]
list_b = [i+1 for i in range (10)]


listas = zip(list_a,list_b)

# print(listas)

'''
El resultado de la función zip es un objeto zip. Este objeto no es directamente una lista o tupla, sino una estructura iterable que contiene los elementos emparejados. 
Puedes recorrer el objeto zip usando un bucle for o convertirlo en una lista o tupla usando la función list o tuple, respectivamente.

En este caso en lugar de ver los elementos emparejados directamente, ves la representación del objeto zip, que muestra la información de la ubicación en la memoria
donde se encuentra almacenado el objeto.

Podemos recorrer los elementos del objeto zip de la siguiente forma:

'''

# listas = list(zip(list_a, list_b)) #Aqui estamos convirtiendo el objeto a una lista utilizando la funcion "list()"


# print(listas)




#Veamos como funciona con un CICLO FOR


for a,b in zip(list_a,list_b): #Esta línea utiliza la función zip() para iterar simultáneamente sobre dos listas: "list_a" y "list_b".
    # print(a, b)
    print(a+b) #Podemos hacer tambien operaciones con los valores de ambas listas
    

