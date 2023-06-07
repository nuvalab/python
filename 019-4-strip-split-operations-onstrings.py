#Digamos que por ejemplo tenemos una variable cuyo valor tiene unos espacios y queremos borrar esos espacios al momento de imprimir
my_name='   Esteban Lopez'
print(my_name.strip()) #Aqui con la funcion strip estoy eliminando los espacios a la izquierda que vemos en el string en la linea 2

#Tambien puedo eliminar el caracter con el que inicia o termina un string, si el caracter no esta al inicio o final, esta funcion no sirve:

print(my_name.strip('z')) #Aqui elimina la "z" pero unicamente porque la cadena de caracteres termina en esa letra, si no no pasaria nada.
print(my_name.strip('Lopez'' ')) #Sin embargo si elimino "Lopez" si lo elimina porque son los ultimos caracteres del string. Es case sensitive, por eso puse la "L" en mayuscula tal cual y esta en el string
#Como vimos tambien pudimos eliminar los especios incluyendo en la función ademas de los caracteres un "' '"


#Digamos que tenemos un string que tiene la misma palabra al inicio y al final del string, veremos que podemos indicar cual de las dos vamos a borrar

my_string1='Python is Python'
print(my_string1.lstrip('Python')) #Aqui poniendo la "l" de "left" antes de strip le estamos diciendo que elimine la palabra que esta del todo a la izquierda
print(my_string1.rstrip('Python')) #Aqui poniendo la "r" de "right" antes de strip le estamos diciendo que elimine la palabra que esta del todo a la derecha


#Podemos ejecutar multiples veces esta funcion "strip"

print(my_string1.strip('P').strip('thon')) # Sin embargo me gusta mas la solucion: print(my_string.strip('P''thon')). Tambien podemos combinarlo con "lstrip" o "rstrip"


#Esta funcion "split()" pone cada palabra del string, como elemento en un array:
my_string2='Python is very easy'
print(my_string2.split())
print(my_string2.split('is')) #Aqui nos divide la oración en dos partes o dependiendo de cuantas veces se encuentre la palabra "is" en la oracion