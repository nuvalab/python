#Si por ejemplo necesitamos poner un espacio o cualquier caracter entre cada letra de un String
from tkinter import CENTER


my_name='Esteban'
my_status='Single'
my_job='Support Engineer'
modify_string=" ".join(my_name)
print(modify_string)

#Tambien podemos modificar el valor de una variable sin necesidad de crear una nueva variable, solo desde el "print" podemos hacerlo

print("\n".join(my_name)) #Como vemos aqui estamos insertando un salto de linea "\n" entre cada caracter del string
print("\t".join(my_name)) #Aqui estamos añadiendo una tabulacion

#Ahora vamos a ver como podemos centrar el valor de nuestras variable de tipo string
print(f"{my_name.center(20)}\n{my_status.center(20)}\n{my_job.center(20)}") #A decir verdad hay veces en que no quedan perfectamente centrados, el numero "20" indica la posicion en la pantalla


#Luego tambien podemos tomar un string e indica como un monton de ceros, a decir verdad no tengo idea de para que servira esto:
print(my_name.zfill(10)) #Dado que "Esteban" tiene 7 caracteres y yo estoy indicando "10", el resto de caracteres me los llena con ceros a la izquierda hasta completar 10 caracteres en total