'''
Escriba un programa que tenga 2 listas y que a continuacion cree las
siguientes listas en las que no debe haber repeticiones:

1. Lista de elementos que aparecen en las dos listas (Sin elementos repetidos)
2. Lista de elementos que aparecen en la primera lista, pero no en la segunda
3. Lista de elementos que aparecen en la segunda lista, pero no en la primera
4. Lista de elementos que aparecen en ambas listas (Osea, por ejemplo si el elemento "1" esta en las dos listas entonces se muestra)

'''
#Creamos las 2 listas:

lista1 = [1,3,5,4,7,1,3,2,1,3,7]
lista2 = [4,5,7,6,3,2,1,9,8,7,3]

#Eliminamos los elementos repetidos (Para ello vamos a convertir las listas en conjuntos como lo habiamos hecho en un ejercicio anterior):

set1 = set(lista1) #Aqui estamos convirtiendo la "lista1" en un "set". Recordar que los "sets" eliminan los elementos repetidos
set2 = set(lista2) # Aqui estamos convirtiendo la "lista2" en un "set"


#RESOLVAMOS CADA PUNTO:

# Vamos a cumplir el primer punto haciendo una union de los sets o conjuntos y convirtiendolos a una lista:

union = list(set1 | set2) #Aqui estamos indicando con el simbolo "|" que vamos a unir los dos sets antes creados. Tambien con "list()" estamos convirtiendo los sets en listas

#Vamos a cumplir el segundo punto donde mostraremos solo los elementos del "set1" pero NO los del "set2", y vamos a mostrarlo como una lista/array:

solo_set1 = list(set1 - set2) #Aqui con el signo "-" estamos indicando que se muestre el "set1", pero no el "set2"


#Vamos a cumplir el tercer punto donde mostraremos solo los elementos del "set2" pero NO los del "set1", y vamos a mostrarlo como una lista/array:

solo_set2 = list(set2 - set1) #Aqui es lo contrario a la linea anterior


#Ahora vamos a cumplir el cuarto punto

interseccion = list(set1 & set2) 


#Ahora vamos a imprimir los resultados:

print(f'Lista de elementos que aparecen en las dos listas (Sin elementos repetidos): {union}')
print(f'Lista de elementos que aparecen en la primera lista, pero no en la segunda: {solo_set1}')
print(f'Lista de elementos que aparecen en la segunda lista, pero no en la primera {solo_set2}')
print(f'Lista de elementos que aparecen en ambas listas (Osea, por ejemplo si el elemento "1" esta en las dos listas entonces se muestra) {interseccion}')