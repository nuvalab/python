'''
El siguiente ejercicio consiste en solicitar al usuario ingrese un string, y mostrarlo de la siguiente forma. Ejemplo: Si el usuario ingresa la palabra "python"

p --> 0
y --> 1
t --> 2
h --> 3
o --> 4
n --> 5

'''

my_string = input('Enter the string:') # Si el valor esperado es un "string" esta es la mejor forma de declarar la variable

index = 0 #establecemos uaa variable de inicialización para mostrar el numero de indice frente a cada palabra tal cual y como pide el ejercicio. Este valor como vemos debe esta por fuera del loop
for i in my_string:
    print(f'{i} --> {index}')
    index += 1 #Esto equivale a decir "index = index + 1". Esto le sumará un 1 en cada iteración a la variable "index"

#IMPORTANTE: Tener en cuenta que si la cadena de caracteres ingresada contiene espacios, cada espacio es considerado como un caracter