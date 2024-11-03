import random

canciones = {}

def cargar_lista(nombre_archivo):
   
    argumento = nombre_archivo + ".txt"
    fichero = open(argumento,"r")
   
    for linea in fichero:
        cancion, artista = linea.strip().split("-")
        canciones[cancion] = artista.strip()
    
    fichero.close()

def agregar_cancion(diccionario_canciones,cancion,artista):

    diccionario_canciones[artista] = cancion
    
    print("Artista agregado: " , diccionario_canciones.items())

def eliminar_cancion(diccionario_canciones,titulo_canción):

    

    if titulo_canción in diccionario_canciones:
        del diccionario_canciones[titulo_canción]
        print("Canción eliminada")
        print(diccionario_canciones)
    else:
        print("No existente en el diccionario")

def ordenar_alfabeticamente(diccionario_canciones):

    #devuelve clave-valor, cancion-artista
    list_diccionario = list(diccionario_canciones.items())
    
    #ordena por el primer valor, en este caso, por la cancíon, sino sería otro índice[0]
    list_diccionario.sort(key= lambda cancion_artista : cancion_artista[1])

    return list_diccionario

def contar_canciones(diccionario_canciones):

    total_canciones = len(diccionario_canciones.values())

    total_salida = "Tenemos un total de " +  str(total_canciones) + " canciones en la lista"
    
    return total_salida

def crear_lista_aleatoria(diccionario_canciones,num_can_aleatorias):

    max_diccionario = len(diccionario_canciones)
    canciones_listadas = list(diccionario_canciones.keys())
    lista_canciones = []
    contador = 0

    if num_can_aleatorias > max_diccionario:

        print("No se encuentran tantas canciones dentro del diccionario de canciones")
        num_can_aleatorias = max_diccionario

    
    while contador < num_can_aleatorias:

        numero_aleatorio = random.randint(0,max_diccionario-1)
        cancion_aleatoria = canciones_listadas[numero_aleatorio]
        lista_canciones.append(cancion_aleatoria)
        contador += 1
    
    print(lista_canciones)
    
    return lista_canciones

def guardar_lista(diccionario_canciones,nombre):

    nombre_fichero = nombre + ".txt"
    fichero = open(nombre_fichero,"w")

    for cancion,artista in diccionario_canciones.items():
    
        fichero.write(f"{cancion} - {artista}\n")
    
    fichero.close()




    
cargar_lista("playlist")


#resultado = contar_canciones(canciones)
#print(resultado)

#eliminar_cancion(canciones, "Imagine")

#crear_lista_aleatoria(canciones,3)

#guardar_lista(canciones,"prueba_de_fichero")


