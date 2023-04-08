#Vamos a crear un script que pedira a un usuario que ingrese dos numeros y validaremos los numeros que sean pares

#Definimos las variables de entrada:
number1=eval(input('Ingrese el primer numero:'))
number2=eval(input('Ingrese el segundo numero: '))


if number1 % 2 == 0 and number2 % 2 == 0: #Aqui estamos usando el operador "%" modulo y si al dividir el numero por 2 su residuo es cero, siempre entonces sera un numero par.
    print ('Ambos numeros son pares')
elif number1 % 2 == 0 and number2 % 2 != 0:
    print (f'El {number1} es par')
elif number1 % 2 != 0 and number2 % 2 == 0:
    print (f'El {number2} es par')
else:
    print ('Ninguno de los dos es par')