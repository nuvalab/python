'''
"*args" se encarga de empaquetar todos los argumentos en una TUPLA. Es util cuando queremos que la funcion permita un numero INDETERMINADO de argumentos 
"**kwargs" se encarga de empaquetar todos los argumentos en un DICCIONARIO. Es util cuando queremos que la funcion permita un numero INDETERMINADO de argumentos de TIPO CLAVE VALOR

'''



'''
def suma(a,b,c):
    return a + b + c

print(suma(3,2,7))
'''

'''
def suma(*args): #"*args" almacena los argumentos en una TUPLA. Podemos asignarle el nombre que queramos a este PARAMETRO siempre y cuando lleve un asterisco delante del nombre
    # print(type(args))
    print(args)
    return sum(args)

print(suma(3,2,7))
'''

'''
def suma(a, b, *args):
    print(a)
    # print(type(args))
    return sum(args)

print(suma(3,2,7))
'''

'''
def saludo(*args):
    print(type(args))
    for i in args:
        print(i)

saludo("esteban", "juliana", "andres")
'''

#---


#Ahora veamos un ejemplo de **kwargs

'''
def say_hi(a, **kwargs): #"**kwargs" almacena los argumentos en un DICCIONARIO. Podemos asignarle el nombre que queramos a este PARAMETRO siempre y cuando lleve un asterisco delante del nombre
    # print(type(kwargs))
    # print(a)
    for i in kwargs:
        # print(i)
        print(f'Hi {kwargs[i]}')
        
say_hi("juan",name1="Esteban", name2="Samantha", name3="Daniela", name4="Matias")
'''


#Veamos un ejemplo similar donde usando la funcion "item()" nos permite listar el KEY y el VALUE de cada elemento en el diccionario
'''
def empleado(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')
        
empleado(nombre="Esteban",profesion="Marketer Diseñador")
'''

#Otro ejemplo mas:
'''
def fav_color(**kwargs):
    for person, color in kwargs.items():
        print(f'{person}\'s favorite color is: {color}')
        
fav_color(Esteban="Yellow",Juliana="Purple", Dani="Black")
'''