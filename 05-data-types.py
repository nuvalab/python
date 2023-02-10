# Podemos definir tambien las variables de esta forma
# x=3;y=5.6;z='Esteban' #Como vemos podemos declarar las variables verticalmente como es normal, o de esta forma horizontal separando cada variable con un ";"

#Lo mismo podemos hacer a continuación, podemos imprimir todas las variables de la sguiente forma:
# print(x,y,z) #Sin embargo no me gusta mucho porque la salida se ve tambien de forma horizontal

x=3
y=5.6
z='Esteban'

print(type(x)) #Aqui no estamos imprimiendo el valor de la variable, sino el tipo. En este caso es de tipo entero "int"
print(x,type(x)) #Si queremos imprimir tanto la variable como su tipo podemos hacerlo de esta forma
print(y)
print(z,type(z))

#Veamos como se definien los  booleanos

isActive=True #Las opciones "True" o "False", siempre deben iniciar con mayuscula, si no nos va dar un error al ejecutar el codigo. Tambien vemos que al igual
# que los numeros, estos valores booleanos NO se encierran entre comillas

print(isActive,type(isActive))


#Podems cambiar el tipo de unavariable de la siguiente forma:

w=27
v=str(w) #De esta forma estamos declarando una variable llamada "v" la cual le esta cambiando el tipo de "number" a "string" a la variable "w" 
print('w is',type(v)) #Veremos que al imprimir esto nos muestra que la variable w es de tipo string. LA VERDAD NO SE ESTO PA QUE PUEDA SER UTIL