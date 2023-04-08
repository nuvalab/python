'''
Construir un programa que simule el funcionamiento de una calculadora 
que puede realizar las cuatro operaciones aritmeticas basicas (suma, resta, multiplicacion y division).
El usuario debe especificar la operacion que desea realizar
'''

num1=eval(input('Ingrese el primer numero:'))
num2=eval(input('Ingrese el segundo numero: '))
operacion=input('Indique el tipo de operacion que desea realizar (suma, resta, multiplicacion, division): ').lower()

if operacion == 'suma':
    suma = num1 + num2
    print (f'El resultado de sumar {num1} y {num2} es {suma}')
elif operacion == 'resta':
    resta = num1 - num2
    print (f'El resultado de restar {num1} y {num2} es {resta}') 
elif operacion == 'multiplicacion':
    multiplicacion = num1 * num2
    print (f'El resultado de multiplicar {num1} y {num2} es {multiplicacion}') 
elif operacion == 'division':
    division = num1 / num2
    print (f'El resultado de multiplicar {num1} y {num2} es {division:.2f}') #Aqui utilice ":.2f" para que en el caso en que el resultado tenga decimales, me muestre maximo 2
else:
    print('Has seleccionado una opcion incorrecta')