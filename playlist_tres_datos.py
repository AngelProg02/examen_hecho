canciones_feid = {
                "nombre": "Ferxxo Icon",
                "artista": "Feid",
                "genero": "Reggaeton"
            }


def cargar_lista(nombre_archivo):
    
    lista_playlist = []
   
    argumento = nombre_archivo + ".txt"
    
    try:
    
        with open(argumento, "r") as fichero:
        
            for linea in fichero:
                cancion, artista,genero = linea.strip().split("-")
                
                canciones = {
                    "nombre": cancion,
                    "artista": artista,
                    "genero":genero
                }
                
                lista_playlist.append(canciones)
    
    except FileNotFoundError:
        print("El archivo no se ha encontrado o no existe")
    except IOError:
        print("Erro al abrir el archivo")
        
            
    return lista_playlist
  

def agregar_cancion(playlist, diccionario_canciones):
    
    cancion_agregada = playlist.append(diccionario_canciones)
    
    #print("Diccionario de canciones agregado: " , diccionario_canciones.items())
    
    
    return cancion_agregada
    
    

def eliminar_cancion(playlist, cancion_eliminar):
    
    cancion_encontrada = False
    
    for i,diccionario in enumerate(playlist):
                
        if diccionario["nombre"].strip() == cancion_eliminar:
            
            playlist.remove(diccionario)
            cancion_encontrada = True
            print("Canción eliminada correctamente")
    
    if not cancion_encontrada:
            
        print("La canción no existe o no se encuentra en la lista")
    
    return playlist

def buscar_cancion(playlist,cancion):
    
    cancion_encontrada = False
    
    for diccionario in playlist:
        
        if diccionario["nombre"].strip() == cancion:
        
            print("Canción encontrada, mostrando datos: ")
            
            print(f"Nombre de la canción: {diccionario['nombre']}, artista: {diccionario['artista']}, género: {diccionario['genero']}")

            
            cancion_encontrada = True
    
    if not cancion_encontrada:
        
        print("Canción no encontrada")
    


    
playlist = cargar_lista("playlist")


#agregar_cancion(playlist,canciones_feid)

#resultado = eliminar_cancion(playlist, "Imagine")

buscar_cancion(playlist, "Imagine")