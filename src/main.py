
from funciones.crearListaCanciones import crearListaCanciones
from funciones.crearPlaylistCanciones import crearPlaylistCanciones
from funciones.ordenarPlaylistAleatorio import crearPlaylistRandom
from funciones.conseguirLugarCanciones import conseguirLugarCanciones
from funciones.unirCancionYLugar import unirCancionYlugar
from funciones.lanzarVLC import lanzarVLC

def playAll (libreriaVar):

    ListaCanciones = crearListaCanciones(libreriaVar) 
    PlaylistCanciones = crearPlaylistCanciones(ListaCanciones)
    PlaylistRandom = crearPlaylistRandom(PlaylistCanciones)
    LugarCanciones = conseguirLugarCanciones(libreriaVar)
    PlaylistFinal = unirCancionYlugar(PlaylistRandom,LugarCanciones)
    LanzarVLC = lanzarVLC (PlaylistFinal)
    



if __name__ == "__main__":

    libreriaVar = {"California Uber Alles":
                {"track-number": 2, "location": "C:\\Users\\abelc\\Desktop\\PROYECTO-PYTHO\\Proyect-VLC-shuffle\\libreria\\California_Uber_Alles.mp3"},
            "King_Kunta": 
                {"track-number": 5, "location": "C:\\Users\\abelc\\Desktop\\PROYECTO-PYTHO\\Proyect-VLC-shuffle\\libreria\\King_Kunta.mp3"},
            "Against the moon":
                {"track-number": 1, "location": "C:\\Users\\abelc\\Desktop\\PROYECTO-PYTHO\\Proyect-VLC-shuffle\\libreria\\against_the_moon.mp3"},
            "Headless":
                {"track-number": 4,  "location": "C:\\Users\\abelc\\Desktop\\PROYECTO-PYTHO\\Proyect-VLC-shuffle\\libreria\\Headless.mp3"}
            }
    playAll(libreriaVar)