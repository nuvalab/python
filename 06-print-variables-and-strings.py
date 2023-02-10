#Vamos a ver como imprimir varias variables

age=27
name='Melissa'
status='Soltera'

#Aqui vamos a imprimir incluyendo nuestro propio texto. A esto se le llamada concatenar texto con variables, y podemos hacerlo con ayuda de comas ","
print("Su nombre es:",name,"\nTiene:",age,"\nEsta:",status) # El "\n" es un caracter especial que imprime un salto de linea

#Tambien podemos imprimir de la siguiente forma que nos permite cambiar el orden en como se va a imprimir el valor de cada variable

print("{2}{1}{0}".format(age,name,status)) #Como veremos en este caso se imprimiria en el siguiente orden: status -> name -> age


#En la siguiente forma podemos imprimir al igual que en la linea "8": nuestro propio texto mas variables (Esta forma me parece mas simple, aunque solo esta diponible de Pyhon 3 en adelante):

print (f"Su nombre es: {name}\nSu edad es: {age}\nSu estado civil es: {status}") #Como vemos aqui las variables irian encerradas entre llaves "{}", lo demas es nuestro propio texto


#Incluso la forma anterior tambien puede ser usada para definirla como variable y luego imprimirla

informacion_ella=f"Su nombre es: {name}\nSu edad es: {age}\nSu estado civil es: {status}"
print(informacion_ella)