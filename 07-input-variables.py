#Vamos a crear una variable que le permita al usuario ingresar un valor

#number1=input('Enter the first number:') #Si declaramos esta variable de esta forma, no importa el tipo de valor que pongamos, el sistema lo interpretara como un "string"
#Una mejor forma de hacerlo es esta:
# number1=input('Enter the first name:') # Si el valor esperado es un "string" esta es la mejor forma de declarar la variable

 #usando "eval" cuando el usuario ingrese el valor, entonces Python identificará que tipo de variable se esta ingresando.
 #Esto es optimo cuando el valor esperado es de tipo "int" o "float"
number1=eval(input('Enter the first number:'))
number2=eval(input('Enter the second number:'))
#A continuación crearemos una variable donde su valor realiza una suma
result=number1+number2

# #Para verificar lo anterior vamos a validar que tipo de variable es "number1" cuando ingresamos un numero, o una cadena de texto, o un flotante:
# print(f"La variable \"number1\" es del tipo: {type(number1)}")

#Vamos a imprimir la variable result
print(f'The adittion of {number1} + {number2} is equal to: {result}')