#Vamos a ver la utilización de valores por defecto en los argumentos de las funciones

def saludo(apellido, nombre="esteban"):
    return f'Hola {nombre} {apellido}'

print(saludo("samantha"))

'''
def display(a=1):
    print('The value of a is: ', a)

display(5)
display(4)
display()
'''

'''
def add_num(a,b=1):
    result = a + b
    print(f'The result is: {result}')


add_num(5,3)
add_num(5)
add_num(4)
'''

# def db_user(user="root"):
#     print(f'Working with the user: {user}')
#     
# db_user("esteban")