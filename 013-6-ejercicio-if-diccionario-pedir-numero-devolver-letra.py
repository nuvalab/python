#El programa solicitara al usuario ingrese un numero del 1 al 10, y devolvera dicho numero escrito en letras. Ejemplo: Si el usuario ingresa "1", el
#programa le devolvera "uno"

#Definimos la variable de entrada:
 
num=eval(input('Digite un numero del 1 al 10: '))   

#Establecemos un diccionario para realizar las bussquedas de acuerdo a la respuesta que nos de el usuario
num_word={1:'one',2:'two',3:'three',4:'four',5:'five',6:'six',7:'seven',8:'eight',9:'nine',10:'ten'}

if num in [1,2,3,4,5,6,7,8,9,10]: #Aqui estamos indicando que si el valor de la variable de entrada se encuentra cualquiera de los elementos del array (En este caso los numeros del 1 al 1o)
    print (num_word.get(num)) #Entonces que se acuerdo al numero ingresado en la variable "num", vaya y busque su respectivo valor en el diccionario "num_word"
else:
    print('Your number is out of range. Please try again')