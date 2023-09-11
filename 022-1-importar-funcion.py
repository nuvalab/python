# Desde aqui vamos a IMPORTAR las funciones que definimos en el script llamado "funcionexporting.py"

#Llamamos la funcion utilizando el NOMBRE DEL SCRIPT. Este NOMBRE NO DEBE TENER CARACTERES EXTRAÑOS NI ESPACIOS. SOLO TEXTO.

# import funcionexporting #De esta forma nos traeriamos TODAS las funciones del script "funcionexporting.py", el tema es que para llamar las funciones deberiamos hacerlo asi:

# print(funcionexporting.substraction(9,3))
# print(funcionexporting.addition(9,3))
#Nota: La ventaja es que si en otro SCRIPT tuvieramos otra funcion que se llama igual a una de las de este SCRIPT, digamos "addition" entonces no tendriamos problema dado que al llamar la funcion del SCRIPT dicho SCRIPT tendria un nombre diferente


#Tambien podemos PONER UN ALIAS al nombre del SCRIPT de forma que sea mas facil llamarlo

# import funcionexporting as f
# print(f.addition(3,4))


#from funcionexporting import addition # Esto SOLO IMPORTARIA la funcion llamada "addition" del SCRIPT llamado "funcionexporting.py"

#print(addition(3,6)) #Cuando IMPORTAMOS las funciones como lo hicimos en la linea anterior y en las siguientes, podemos LLAMAR a la FUNCION como lo hariamos normalmente

# from funcionexporting import addition, substraction # Esto IMPORTARIA las funciones llamadas "addition" y "substraction" del SCRIPT llamado "funcionexporting.py"

# from funcionexporting import addition as add #De esta forma estamos RENOMBRANDO/O ASIGNANDO UN ALIAS con el nombre "add" a la funcion llamada "addition" 
# print(add(5,3))

# from funcionexporting import * # Esto IMPORTARIA todas las funciones del script llamado "funcionexporting.py"

print ("---------------------")


#Veamos como importar otra funcion:

from import_tutorial import *

countries = ["Spain", "Sweeden", "Germany", "Colombia", "Scotland", "Canada"]

print(filter_countries(countries, "C")) #Aqui estamos llamado a la PRIMER funcion

print(get_first_country(countries)) #Aqui estamos llamado a la SEGUNDA funcion