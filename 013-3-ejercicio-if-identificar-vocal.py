#Hacer un programa que pida un caracter e indique si es una vocal o no

'''
letra=input('Digite un caracter: ').lower() #Al poner ".lower()" estamos indicando que el caracter que ponga el usuario siempre le convierta a minuscula
#Tambien podemos transformar a mayuscula con ".upper()"

if letra=='a' or letra=='e' or letra=='i' or letra=='o' or letra=='u':
    print('Esto es una vocal')
else:
    print('Esto es una consonante')

'''

#otra forma de hacerlo seria con un array y un "membership operator":

letter=input('Digite un caracter: ').lower()
vowels=['a','e','i','o','u']

if letter in vowels: #En este caso "in" es un operador de membresia, y lo que esta preguntando es si la letra que almacena la variable "letter" esta en el array "vowels"
    print('This is a vowel')
else:
    print('This is a consonant')