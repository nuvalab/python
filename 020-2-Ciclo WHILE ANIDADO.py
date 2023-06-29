#Veamos como funciona un ciclo WHILE anidado


# Ejemplo basico de un while anidado
# numero = 1

# while numero <= 3:
#     print("Iteración externa:", numero)

       
#     contador = 1
#     while contador <= 3:
#         print("   Iteración interna:", contador)
#         contador += 1
    
#     numero += 1
    

#Otro ejemplo:



servers = ["server1", "server2", "server3"]
tasks = ["task1", "task2", "task3"]

index_servers = 0
while index_servers < len(servers):
    current_server = servers[index_servers]
    print(f"Procesando el servidor: {current_server}")

    index_tasks = 0
    while index_tasks < len(tasks):
        current_task = tasks[index_tasks]
        print(f"Ejecutando la tarea: {current_task} en el servidor: {current_server}")

        # Aquí iría el código para realizar la tarea en el servidor

        index_tasks += 1

    index_servers += 1
    
#Nota: creo que para el ejemplo anterior seria mejor utilizar un FOR ya que tenemos claro cuanto es la cantidad de elementos que vamos a recorrer. Sin embargo sorve para entender el concepto de WHILE anidado
