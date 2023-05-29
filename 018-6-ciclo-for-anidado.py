


# numeros = [1,2,3]
# letras = ["a","b","c"]

# for i in numeros:
#     print(i)
#     for j in letras: #Siempre el ciclo mas INTERNO itera mas rapido que el ciclo mas EXTERNO
#         print(j)
#     print("==============")



#Tabla de multiplicar con FOR anidado:

# for i in range(1,11):
#     for j in range(1,11):
#         # print(i,j)
#         print(f'{i} * {j} =', i*j)
#     print("==============")
    



#Ahora veamos como recorrer listas dentro de listas usando un FOR anidado

# lista = [["Juan","Maria","Peter"],[3,2,7],["amarillo","azul","rojo"]]

# for i in lista:
#     # print(i)
#     for j in i: #Aqui le estamos diciendo a la variable de control "j", que recorra los elementos de la lista que este recorriendo la variable de control "i"
#         print(j)
#     print("==============")

   
   

# Vamos a crear un ejercicio donde tenemos 3 departamentos: Marketing, Ventas, Operaciones, y tres listas con diferentes costos que debemos sumar:


lista_de_listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
departamentos = ['Marketing', 'Ventas', 'Operaciones']

resultados = []
for i in range(len(lista_de_listas)):  # Bucle externo para iterar sobre los índices de las listas. La funcion "len()" indica la cantidad de elementos de una lista. 
    # En este caso entonces entonces equivaldria a decir "for i in range(3)", lo que quiere decir que va del 0 al 2
    sublista = lista_de_listas[i]  # Accedemos a la sublista utilizando el índice

    suma = 0
    for num in sublista:  # Bucle interno para iterar sobre los números de cada sublista
        suma += num #Esto es lo mismo que decir que suma es igual a suma + num
        print(num)
    print("==========")
    print(suma)
    print("==========")


    departamento = departamentos[i]  # Accedemos al departamento correspondiente utilizando el índice
    resultados.append((departamento, suma)) # creamos una tupla con el nombre del departamento y el valor de la suma ((departamento, suma)), y la agregamos a la lista de resultados utilizando resultados.append().

print(resultados)

