#El siguiente ejercicio pide almacenar y sumar todos los valores del diccionario en una variable llamada "Total Donations"

donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5, stan=150.0, lisa=50.25, harrison=10.0) #Esto como veiamos anteriormente es otra forma no muy usada de declarar diccionarios

total_donations = 0 #Iniciamos esta variable en cero ya que nos va a servir de variable de acumulación

for i in donations.values():
    total_donations += i # El "+=" se conoce como un operador de asignación y lo que indica es: "total_donations = total_donations + i". Entonces en cada iteración se ira sumandoa  la variable "total_donations" lo que valga "i"


#Lo anterior puede hacerse muy facil tambien con la funcion "sum()"
#total_donations = sum(donations.values())

print(total_donations)