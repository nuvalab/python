'''
Este es un SCRIPT para buscar un archivo especifico en un directorio
'''

import os

#Indicamos cual es la ruta en la que vamos a buscar
target_directory = r"G:\Other computers\My Laptop\PROYECTOS +++\TI\Aprendiendo Python\MY SCRIPTS\ARCHIVOS DE PRUEBA"


#Indicamos el nombre del archivo que vamos a buscar:
target_file = "direccionesip.txt"


#Para que entendamos bien como el FOR recorre los directorios teniendo diferentes variables de control, veamos que es lo que imprime la función "os.walk()":
# print(  list(os.walk(target_directory)) ) #Esto nos muestra una chorrera de cosas, pero vamos a entender como itera el FOR



#Esto entonces me muestra una chorrera de cosas, pero basicamente en cada iteración el FOR de mas abajo va a
for root,dirs,files in os.walk(target_directory): #Vemos que le pasamos como argumento a la funcion  "os.walk()" la variable donde se encuentra la ruta del directorio. Al final para eso sirve esa funcion, para recorrer directorios recursivamente
    print(root)
    print(dirs)
    print(files)
    print("=======================================")

'''
CONCLUSION: Entonces el FOR nos va a mostrar cada ITERACIÓN separa por "=======================================", pa eso puse eso ahi, para diferenciar cada iteración. 

--
En la PRIMER ITERACIÓN me muestra la RUTA inicial desde donde parte, la cual es la indicada en la variable "target_directory", entonces:
Me lista la ruta inicial
Me lista los nombres de directorios que hay dentro (Si exixten)
Me muestra los archivos que hay en la ruta incial:
--


--
En la SEGUNDA ITERACIÓN va y recorre unos de los directorios que encontró en la ruta inicial, y lista:
Dicha ruta
Los directorios que haya dentro (Si no hay me muestra una lista vacia)
Los archivos que existan (Si no hay me muestra una lista vacia)

---

Para el resto de iteraciones aplica lo mismo. La cantidad de iteraciones del bucle, dependerá de cuantas subcarpetas hayan dentro de la carpeta raiz (O para ser mas claros: dentro
de la carpeta que le pasamos como argumento a la función "os.walk()")



'''


'''
Aquí comienza un bucle for. os.walk() es una función que recorre de manera recursiva un directorio y sus subdirectorios.
rePath ---> Muestra la ruta indicada en la variable "target_directory", ademas muestra tambien la ruta de otros directorios si existen directorios dentro
dirs ---> Muestra los directorios que hay dentro de la ruta especificada en la variable "target_directory"
files ---> Muestra los archivos que hay dentro de la ruta definida en la variavle "target_directory", y tambien muestra los archivos dentro de los directorios que estan dentro de esa ruta
IMPORTANTE: Estas variables de control antes mencionadas, pueden tener el nombre que nosotros queramos
'''

# file_found = False # Variable para seguir el estado de si el archivo fue encontrado

# for relPath,dirs,files in os.walk(target_directory):
#     # print(files)
#     if target_file in files: #Esta condición indica que si el nombre de archivo indicado en la variable "target_file" esta dentro de los "files/archivos que existen recursivamente dentro del directorio", entonces que haga lo de la siguiente linea
#         fullPath = os.path.join(target_directory, relPath, target_file) # Si encontramos una coincidencia, construimos la ruta completa del archivo utilizando os.path.join() y la imprimimos en la consola.
#         print(f'El archivo fue encontrado en la siguiente ruta: {fullPath}')
#         file_found = True # Cambiamos el estado a True para indicar que se encontró el archivo
# if not file_found: #Aqui este NOT quiere decir que si el valor de la variable "file_found" es "false", entonces imprima lo que sigue en la siguiente linea
#     print(f'El archivo {target_file} no existe en esta ruta')



        
'''
Tambien podemos crear un SCRIPT pero esta vez con una función

'''

# Las siguientes variables de entrada es por si queremos que el SCRIPT sea interactivo y queremos preguntar al usuario los datos para realizar la busqueda. Si vamos a usarlos, debemos pasarlos como argumentos al llamar la funcion

# buscar_en_directorio = input("Ingrese la ruta del sistema donde desea buscar el archivo: ")
# archivo_a_buscar = input("Ingrese el nombre del archivo que desea buscar: ")



def encontrar_archivo(target_directory, target_file):

    file_found = False
    
    for relPath,dirs,files in os.walk(target_directory):
        if target_file in files: #Esta condición indica que si el nombre de archivo indicado en la variable "target_file" esta dentro de los "files/archivos que existen recursivamente dentro del directorio", entonces que haga lo de la siguiente linea
            fullPath = os.path.join(target_directory, relPath, target_file) # Si encontramos una coincidencia, construimos la ruta completa del archivo utilizando os.path.join() y la imprimimos en la consola.
            print(f'El archivo fue encontrado en la siguiente ruta: {fullPath}')
            file_found = True
            break #Al agregar break después de encontrar el archivo, se interrumpe la ejecución del bucle for y el programa continúa después del bloque del bucle for. Esto evita que se sigan buscando archivos innecesariamente una vez que se ha encontrado el archivo buscado.

    if not file_found:
        print(f'El archivo {target_file} no fue encontrado')
        
encontrar_archivo(target_directory, target_file)


#NOTA: Lo siguiente muestra un MIERDERO de cosas. Lo dejo porque me gusta esa estructura del PRINT
# for dirpath, dirnames, filenames in os.walk(r'G:\\Other computers\\My Laptop\\PROYECTOS +++\\TI\Aprendiendo Python\\MY SCRIPTS\\ARCHIVOS DE PRUEBA'):
#     print(
#         f'Root: {dirpath}\n'
#         f'Sub-directories: {dirnames}\n'
#         f'Files: {filenames}'
#     )
