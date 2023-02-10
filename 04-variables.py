#De esta forma definimos las variables en Python
a=3 #En Python no es necesario especificar que tipo de variable es: entero, flotante, string, etc
b = 3.27

#De esta forma imprimimos el valor de las variables:
print(a) #Si vamos a imprimir una variable NO debemos encerrar el nombre de esta entre comillas

#Si quiero saber que tipo de variable tenemos (Entero, entero, flotante), podemos ejecutar lo siguiente:
print(type(a))
print(type(b))


a=7
print(a)
print(id(a)) #Con esto validamos en que espacio de memoria esta almacenada la variable

#Podemos eliminar una variable si no queremos que se almacene en memoria:
del a
# print(f'Intentemos imprimir el valor de la variable "a": {a}')