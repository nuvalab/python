'''
Sentencia de control: break:  básicamente lo que va a hacer es frenar la iteración del LOOP


'''

# #Veamos un ejemplo con Brake:

# for i in [3,2,7]: #Sin el "brake" normalmente el loop imprimiria todos los elementos del array, sin embargo dado que vamos a poner un brake despues del print, solo se imprimira la primer iteracion
#     print(i)
#     #break # Este break interrumpiria la iteración del bucle FOR
# #Tambien podemos poner un IF anidado que indique que el bucle itere hasta llegar a cierto elemento
#     if i == 2:
#         break #En este caso entonces el loop itera hasta encontrar un elemento en el array que se llame "2" y una vez impreso se interrumpe la iteración del bucle
    
    
# '''
# Un muy buen ejemplo es el que vamos a ver a continuación, donde digamos tenemos un monton de PATHS, y yo con un BUCLE FOR voy a recorrerlos todos para
# buscar algo que necesito especificamente, y que cuando lo encuentre el bucle termine de iterar.

# '''

# #En el siguiente ejemplo quiero que el bucle me busque el PATH que contiene la palabra "httpd", luego de que lo encuentre queremos proceder a interrumpir la iteración del LOOP

# paths = ['/usr/bin','/usr/bin/httpd','/home/esteban/config.html'] #Digamos que este es el listado de PATHS que tengo

# for i in paths:
#     if 'httpd' in i: #Este IF es practicamente la primer vez que lo vemos y estamos usando algo llamado operador de pertenencia, en este caso el operador de pertenencia "in"
# #En la linea anterior estamos diciendo que si la palabra "httpd" esta en la variable "i" que la imprima. Caso contrario no va a imprimir nada mas. En ese caso no necesitamos entonces el "break"
#         print(i)
#         #break

# '''
# IMPORTANTE: Para aclarar lo de los operadores de pertenencia:

# "in" devuelve True si el valor especificado se encuentra en la secuencia. En caso contrario devuelve False.
# "not in" devuelve True si el valor especificado no se encuentra en la secuencia. En caso contrario devuelve False.

# '''

# #Tambien por ejemplo podriamos usar la condicional IF para excluir cierto elemento. Digamos que por ejemplo queremos excluir el numero 7 del siguiente rango

# for i in range(10):
#     if i != 7: #Aqui estamos indicando que siempre que el elemento sea  DIFERENTE a 7, que lo imprima.
#         print(i)
        
        

'''

Sentencia de control: continue

'''

for each in range(10):
    if each == 7:
        continue
    print(each)