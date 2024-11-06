import random

canciones = {}

def cargar_lista(nombre_archivo):
   
    diccionario = {}
    argumento = nombre_archivo + ".txt"
    with open(argumento, "r") as fichero:
    
        for linea in fichero:
            cancion, artista = linea.strip().split("-")
            diccionario[cancion] = artista.strip()
    
    return diccionario
  

def agregar_cancion(diccionario_canciones,cancion,artista):

    diccionario_canciones[cancion] = artista
    
    print("Artista agregado: " , diccionario_canciones.items())

def eliminar_cancion(diccionario_canciones,titulo_canción):

    

    if titulo_canción in diccionario_canciones:
        del diccionario_canciones[titulo_canción]
        print("Canción eliminada")
        print(diccionario_canciones)
    else:
        print("No existe en el diccionario")

def ordenar_alfabeticamente(diccionario_canciones):

    #devuelve clave-valor, cancion-artista
    list_diccionario = list(diccionario_canciones.items())
    
    #ordena por el primer valor, en este caso, por la cancíon
    list_diccionario.sort(key= lambda cancion_artista : cancion_artista[1])

    return list_diccionario

def contar_canciones(diccionario_canciones):

    total_canciones = len(diccionario_canciones.values())

    total_salida = "Tenemos un total de " +  str(total_canciones) + " canciones en la lista"
    
    return total_salida

def crear_lista_aleatoria(diccionario_canciones,num_can_aleatorias):
    
    n = min(num_can_aleatorias, len(diccionario_canciones))
    lista = random.sample(diccionario_canciones.items(),n)
    
    return lista

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


