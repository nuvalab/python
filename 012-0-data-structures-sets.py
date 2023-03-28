#Veamos como definir un SET
my_set={"Esteban",27,'Single',327,'Rich'} #Lo que lo diferencia de un diccionario es que aqui no especificamos un key/value
print(type(my_set)) #Con esto podemos validar que tipo de colección o variable es esta

#Si quisieremos que nuestro set fuese inmutable, podemos hacer lo siguiente:
my_set=frozenset({"Esteban",27,'Single',327,'Rich'})

my_set.add("Colombian") #Con el metodo ".add()" podemos añadir nuevos elementos/items al set. Si el elemento ya existe, no lo agrega dado que los sets no muestran elementos repetidos
# my_set.remove("dog") #Si queremos eliminar alguno elemento/item del set, usamos el metodo ".remove"
# IMPORTANTE: Si ponemos como argumento un item que no existe, haciendo uso del metodo ".remove", se interrumpira, la ejecucion del script y nos sacara un error. Por ello es mejor esta otra opcion:
my_set.discard(27) #Con ".discard()" aun cuando el elemento/item puesto como argumento, no exista, este NO interrumpira la ejecucion del script. Tampoco muestra errror alguno
my_set_copy = my_set.copy # De esta forma podemos copiar el contenido de un set a otro. En este caso el contenido de "my_set" a "my_set_copy". Ambos estan en espacios de memoria diferente como veremos a continuación:
print(id(my_set), id(my_set_copy)) #Esto muestra el espacio de memoria en el que esta ubicada cada variable/set 
my_set.clear() #Si quisieramos eliminar todos los elementos de un "set", utilzariamos el metodo ".clear()"
print(my_set)
print("Esteban" in my_set) #Esto buscaria si el elemento llamado "Esteban" existe dentro del set llamado "my_set"


#Veamos como establecer un SET vacio
my_new_set=set({})
print(my_new_set)
print(type(my_new_set)) #Veamos que tipo de variable/coleccion nos indica Python
print(bool(my_new_set)) #Validemos si la coleccion contiene elementos o no

#Podemos convertir una "lista/array" en un "set"
my_list=[4,5,9,3]
my_set=set(my_list) #Aqui estamos convirtiendo la lista/array a un set
print(my_set)

#Podemos ver las diferentes operaciones disponibles para este tipo de colección (Un "set" es un tipo de colección. Al igual que los diccionarios, listas, tuplas...):
#print(dir(set))

#Por ejemplo declaremos dos "sets" y luego utilicemos una de las operaciones para unirlos
set_a={7,5,9}
set_b={5,15,7}
print(f"{set_a.union(set_b)}")

#Podemos hacer lo mismo que acabamos de hacer, de la siguiente forma:

union=set_a | set_b #Como vemos estamos usando el simbolo "|" para unir el contenido de ambos sets. Tener en cuenta que si por ejemplo en este caso se repite un mismo numero en ambos sets
# este numero será mostrado solo una vez ya que como sabemos en los sets no se permiten valores duplicados.
print(union)

#Tambien podemos definir la intersección entre ambos sets. Esto nos indicara los elementos en comun que hay entre ambos sets. Tener en cuenta que tambien existen operaciones propias de Python
#que logran lo mismo
intersection=set_a & set_b
print(intersection)


#Tambien podemos usar la diferencia. Osea elementos que estan en el "set_a" que no estan en el "set_b"
diferencia_1=set_a - set_b #Aqui mostrariamos los elementos que estan en "set_a" pero que no estan en "set_b". Pero tambien podemos mostrar lo contrario: Elementos que estan en "set_b" pero no en "set_a"
diferencia_2=set_b - set_a
print(diferencia_1)
print(diferencia_2)


#Si queremos ver cuales valores estan en "set_a" y en "set_b" pero que no estan en ambos sets:
diferecia_simetrica = set_a ^ set_b
print(diferecia_simetrica)