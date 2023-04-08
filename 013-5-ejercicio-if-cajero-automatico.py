'''
Hacer un programa que simule un cajero automatico con un saldo
inicial de $1000 y tendra el siguiente menu de opciones:

1. Ingresar dinero en la cuenta
2. Retirar dinero de la cuenta
3. Mostrar dinero disponible
4. Salir

#Nota: Esto seria mejor hacerlo con bucles, pero en este caso estamos practicando la condicional IF

'''

saldo = 1000 #Dado que nos dicen que el saldo inicial es de 1000, creamos entonces una variable llamada "saldo" y su valor inicial va a ser 1000

#print('\t.:MENU:.') #Aqui el "\t" es una tabulación. El resto eso solo decoración
print('1. Ingresar dinero en la cuenta')
print('2. Retirar dinero de la cuenta')
print('3. Mostrar dinero disponible')
print('4. Salir')

opcion_seleccionada=eval(input('Digite una opción del menu: '))

print() #Con esto podemos incluir una linea vacia. Esto solo para darle formato al texto que se imprimira en pantalla

if opcion_seleccionada == 1:
    ingresar = eval(input('¿Cuanto dinero desea ingresar en la cuenta? '))
    saldo += ingresar #Aqui estamos sumandole al saldo el valor ingresado por el usuario.
    #En la linea anterior hemos usado un operador de asignación "+=" el cual equivaldria a "saldo = saldo + ingresar"
    print(f'Dinero ingresado correctamente. Ahora su saldo es de {saldo}')
elif opcion_seleccionada == 2:
    retirar = eval(input('¿Cuanto dinero desea retirar de la cuenta? '))
    if retirar > saldo: #Aqui estamos validando que la cantidad indicada NO sea mayor al saldo disponible
        print(f'La cantidad a retirar es mayor al saldo. Su saldo actual es {saldo}')
    else:
        saldo -= retirar #Aqui estamos restandole al saldo el valor ingresado por el usuario.
        #En la linea anterior hemos usado un operador de asignación "-=" el cual equivaldria a "saldo = saldo - retirar"
        print(f'Dinero retirado correctamente. Ahora su saldo es de {saldo}')
elif opcion_seleccionada == 3:
    print(f'Su saldo disponible es: {saldo}')
elif opcion_seleccionada == 4:
    print('Gracias por utilizar nuestro cajero automatico')
else:
    print('Has seleccionado una opcion que no esta en el menu. Vuelve a intentarlo')