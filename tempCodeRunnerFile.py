canciones = {}

def cargar_lista(nombre_archivo):
   
    argumento = nombre_archivo + ".txt"
    fichero = open(argumento,"r")
   
    for linea in fichero:
        cancion, artista = linea.strip().split("-")
        canciones[cancion] = artista
    
    fichero.close()

def agregar_cancion(diccionario_canciones,cancion,artista):

    diccionario_canciones[artista] = cancion
    
    print("Artista agregado: " , diccionario_canciones.items())

#Escribe una función llamada eliminar_cancion que tome 
# un diccionario de canciones y el título de una canción como argumentos, 
# y elimine la canción del diccionario si está presente.


def eliminar_cancion(diccionario_canciones,titulo_canción):

    for autor,canciones in diccionario_canciones.items():
        if titulo_canción in canciones:
           canciones.remove(titulo_canción)
           print("Canción eliminada")
           return
       



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
    
cargar_lista("playlist")

#resultado = contar_canciones(canciones)
#print(resultado)

resultado2 =  eliminar_cancion(canciones, "Wonderwall")
print(resultado2)




