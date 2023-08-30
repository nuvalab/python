'''

Vamos a crear un codigo que nos va a permitir copiar un archivo desde nuestra maquina local a multiples servidores remotos. Este tendra las siguientes caracteristicas:



- El programa preguntara al usuario cuales son las IP de los servidores donde vamos a copiar el archivo (Puede ingresar uno o mas de uno. Lo ideal es que fuera a mas de uno)
- El programa preguntara al usuario la ruta donde se encuentra el archivo en la maquina local
- El programa preguntara al usuario la ruta donde queremos copiar el archivo en el servidor remoto (Incluso permitira crear la ruta si no existe)



¿Que voy a necesitar para lograr esto?:

Debemos instalar "PARAMIKO", este modulo nos permite conectarnos a servidores remotos, y copiar archivos:

pip install paramiko


'''



import paramiko

# Creamos una lista para almacenar las conexiones SSH
conexiones_ssh = []
servidores = []


while True:
    # Solicitar entrada al usuario
    ip = input("Ingrese la IP del servidor: ")
    usuario = input("Ingrese el usuario (Usuario por defecto 'root'): ") or "root" # La parte "or "root"" pone como valor por defecto la palabra "root", para el caso en el que el usuario de enter sin introducir ningun usuario
    ruta_llave = input("Ingrese la ruta completa donde se encuentra la llave privada: ")
    
    # Crear el diccionario
    elemento = {"hostname": ip, "username": usuario, "key_filename": ruta_llave}
    
    # Agregar el diccionario a la lista
    servidores.append(elemento) #Aqui estamos añadiendo el contenido de la variable "elemento", la cual va a ir creando un diccionario en cada iteración. Estos diccionarios se agregarán como elementos en la variable de tipo lista llamada "servidores"
    
    # Preguntar al usuario si desea agregar otro elemento
    respuesta = input("¿Desea agregar otro servidor? (Si/No): ")
    if respuesta.lower() != "si":
        break

# Creamos una lista con los detalles de cada servidor
# servidores = [
#     {"hostname": "192.168.20.165", "username": "root", "key_filename": "G:\\Other computers\\My Laptop\\PROYECTOS +++\\NUVALAB\\LLAVES PRIVADAS MAQUINA LOCAL\\docker.pem"},
#     {"hostname": "192.168.20.160", "username": "root", "key_filename": "G:\\Other computers\\My Laptop\\PROYECTOS +++\\NUVALAB\\LLAVES PRIVADAS MAQUINA LOCAL\\kubernetes.pem"}
# ]

# Creamos una conexión SSH para cada servidor en la lista
for servidor in servidores:
    # Creamos una instancia de SSHClient:

    # En Python, una clase es una plantilla o modelo para crear objetos. Puedes pensar en una clase como un plano para construir objetos con características y 
    # comportamientos específicos. Para utilizar una clase y crear objetos de ella, necesitamos instanciarla, es decir, crear una instancia de la clase.
    
    # En resumen, crear una instancia de una clase significa crear un objeto basado en esa clase en particular, permitiéndonos utilizar sus funcionalidades y manipular 
    # sus datos. En el caso del código que mencionaste, la instancia de SSHClient nos permite establecer conexiones SSH y realizar operaciones relacionadas con la conexión 
    # en servidores remotos.
    

    ssh = paramiko.SSHClient() # Aqui este que estamos creando la instancia para la conexión SSH, dado que estamos usando el FOR, se creara para cada servidor de la lista que esamos recorriendo
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy()) #Esto es para que no se presente un error al intentar realizar la conexión al servidor remoto, si previamente no hemos agregado el host al "known_hosts":
    
    # Establecemos la conexión SSH (Por llave publica) utilizando los detalles de cada servidor
    ssh.connect(
        hostname=servidor["hostname"],
        username=servidor["username"],
        key_filename=servidor["key_filename"]
    )
    
    # Agregamos la conexión SSH a la lista llamada "conexiones_ssh"
    print(f'QUIERO VER QUE CONTIENE ESTA VARIABLE{ssh}')
    conexiones_ssh.append(ssh)




ruta_origen = input("Ingresa la ruta completa donde se encuentra el archivo origen: ")
ruta_destino = input("Ingresa la ruta completa donde quieres almacenar el archivo en el servidor remoto: ")

for servidor, ssh in zip(servidores, conexiones_ssh): #Esta línea utiliza la función zip() para iterar simultáneamente sobre dos listas: servidores y conexiones_ssh.

    # Creamos el cliente SFTP para cada servidor
    sftp_client = ssh.open_sftp()
    
    # Ejecutamos la operación SFTP en cada servidor
    sftp_client.put(ruta_origen, ruta_destino)
    
    # Cerramos la conexión SFTP y SSH
    sftp_client.close()
    ssh.close()