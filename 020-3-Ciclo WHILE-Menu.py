#Veamos como crear un Menu con un WHILE anidado:

'''
Algunas anotaciones:

En la línea os.system('cls' if os.name == 'nt' else 'clear'), 'nt' se refiere a la abreviatura de "Windows NT" y se utiliza para verificar si el sistema operativo actual es Windows.

La función os.name devuelve el nombre del sistema operativo en el que se está ejecutando el código. En el caso de Windows, devuelve 'nt', mientras que en sistemas Unix y Linux, 
devuelve 'posix'.

La expresión 'cls' if os.name == 'nt' else 'clear' es una expresión condicional que se conoce como operador ternario. Si os.name es igual a 'nt' (es decir, si se está ejecutando 
en Windows), se utilizará 'cls' para limpiar la pantalla. Si no es igual a 'nt' (es decir, si se está ejecutando en Unix o Linux), se utilizará 'clear' para limpiar la pantalla.


En este caso, el bucle while True crea un bucle infinito que se ejecutará continuamente hasta que se encuentre una instrucción break. Dentro del bucle, solicitamos la opción 
al usuario y verificamos las condiciones utilizando if-elif-else, al igual que en el ejemplo anterior.

La diferencia principal es que al seleccionar la opción "4" (Salir), se ejecuta la instrucción break, lo que interrumpe el bucle while y se finaliza el programa. 
Esto permite al usuario salir del menú y terminar la ejecución cuando lo desee.

El uso del bucle while permite que el menú se repita indefinidamente hasta que se elija la opción de salida, brindando una experiencia interactiva al usuario.

'''



import os

# print(os.name)


while True:
    os.system('cls' if os.name == 'nt' else 'clear')  # Esta linea limpia el menú y la entrada del usuario

    print("Menu:\n(1) Frase del día\n(2) Curiosidad\n(3) Dato perturbador\n(4) Salir")

    respuesta = input("Ingrese alguno de los numeros del menu anterior: ")

    if respuesta == "1":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('\n"Lo que das a otros te lo das a ti mism@"\n')
    elif respuesta == "2":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('"Macchu Pichu es una ciudad a prueba de terremotos"')
    elif respuesta == "3":
        os.system('cls' if os.name == 'nt' else 'clear')
        print('"Cuando una persona muere, el último sentido en irse es el del oído"')
    elif respuesta == "4":
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Hasta luego. ¡Vuelve pronto!")
        break  # Con este "break" se interrumpe la iteración del bucle.
    else:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("Opción inválida. Por favor, ingrese un número válido del menú.")

    input("Presione Enter para continuar...")
