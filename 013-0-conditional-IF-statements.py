'''
Aqui veremos como es la utilización del condicional IF en Python

'''
#Vamos a declarar una variable la cual pedira un dato de entrada:
number1=eval(input('Enter one number:')) #Recordar que "eval" lo utilizamos cuando la variable NO es de tipo "string"
#Si la variable fuera de tipo "string" la variable se declararia de la siguiente forma:
#number1=input('Enter one number: ')


#De esta forma declaramos una condicional IF y un ELSE en Python que validara si el numero ingresado es positivo o negativo.

if number1 > 0:
        print(f'El numero es positivo. {number1} es un numero es positivo')
elif number1 == 0: #Con ELIF podemos indicar condiciones adicionales.
        print('El numero es igual a cero')
else:
        print('El numero es negativo')