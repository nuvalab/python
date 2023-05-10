'''

Vamos a recorrer los numeros del 1 al 20 con un ciclo FOR y debemos cumplir los siguientes puntos:

Para los numeros 7 y 13, imprimir un mensaje que diga "Eres super suertudo"
Para los numeros que son PARES imprimir un mensaje que diga "X numero es PAR"
Para los numeros que son IMPARES imprimir un mensaje que diga "X numero es IMPAR"

'''

# for i in range(1,21):
#     if i == 7 or i == 13: #Aqui tuve que poner esta condicion de primera dado que si la ponia de ultimas la primera condicion que coincide va a imprimirse... 
#         #En este caso el 7 y el 13 son numeros IMARES entonces si la condicion que evalua los impares esta de primera, se va a imprimir que son IMPARES, pero no que son numeros SUPER SUERTUDOS 
#         print (f'{i} es un numero SUPER SUERTUDO')
#     elif i % 2 == 0: #Aqui estamos usando el operador "%" modulo y si al dividir el numero por 2 su residuo es cero, siempre entonces sera un numero par.
#         print (f'{i} es PAR')
#     elif i % 2 != 0:
#         print (f'{i} es IMPAR')
    # else:
    #     print (f'{i} es IMPAR')


#Otra forma de hacerlo dado que los print tienen un string como con un patron similar seria:

for i in range(1,21):
    if i == 7 or i == 13:
        state = "es un numero SUPER SUERTUDO"
    elif i % 2 == 0:
        state = "es PAR"
    elif i % 2 != 0:
        state = "es IMPAR"
    print(f'{i} {state}') 