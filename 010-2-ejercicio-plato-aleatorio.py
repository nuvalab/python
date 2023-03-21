# This code picks a random food item:
from random import choice #DON'T CHANGE!
food = choice(["cheese pizza", "quiche","morning bun","gummy bear","tea cake"]) #DON'T CHANGE! #Con el metodo "choice" que hace parte del modulo "random" se selecciona aleatoriamente un elemento de la lista

#Definimos el diccionario:
bakery_stock = {
    "almond croissant" : 12,
    "toffee cookie": 3,
    "morning bun": 1,
    "chocolate chunk cookie": 9,
    "tea cake": 25
}


# print(f'{"{} left".format(bakery_stock["tea cake"])}') #De esta forma se llama una clave de un diccionario usando el metodo "format()"

if food in bakery_stock: #Aqui estamos indicando que si el elemento seleccionado de la lista "food" (Aleatoriamente seleccionado con el metodo "choice") esta dentro del dccionacionario "bakery_stock", haga entonces lo siguiente:
    print(f'{food}: {"{} left".format(bakery_stock[food])}') #En esta linea 
else:
    print(f'We don\'t make "{food}"')