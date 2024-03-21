# Importa el modulo json que proporciona funciones para trabahar con datps Python
import json

# Almacena el nombre del archivo JSON que vamos a abrir y leer
file_name = "data.json"

# Abre el archivo JSON especificado en el modo de lectura ('r') 
# utilizando un contexto with. El archivo se abrirá como data.
with open(file_name) as data:

# Carga el contenido del archivo JSON en el diccionario datos 
# utilizando la función json.load()
    datos = json.load(data)

#for key, value in datos.items():
#    if key == "version":
#        print(f"{key}: {value[0]}")
#    else:
#       print(f"{key}: {value}")

#for key, value in datos.items():
#    print(f"{key}: {value[0] if key == 'version' else value}")

# itera sobre cada par clave-valor en el diccionario datos utilizando 
# un bucle for  
for key, value in datos.items():

# Imprime el valor después de los dos puntos (:) en cada valor del diccionario datos
    print(value.split(": ", 1)[1] if ": " in value else value)