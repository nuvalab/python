#Debemos determinar de los datos ingresados cual es el numero mayor
#Ejercicio: Hacer un programa que pida tres numeros y determine cual es el mayor

#Definimos las variables de entrada:
num1=eval(input('Ingrese el primer numero:'))
num2=eval(input('Ingrese el segundo numero: '))
num3=eval(input('Ingrese el tercer numero: '))

if num1>num2 and num1>num3:
    print(f'El numero {num1} es el numero mayor (op1)')
elif num2>num1 and num2>num3:
    print(f'El numero {num2} es el numero mayor (op2)')
elif num3>num1 and num3>num2:
    print(f'El numero {num3} es el numero mayor (op3)')
elif num1==num2 and num2==num3 and num3==num1:
    print('Todos los numeros son iguales')