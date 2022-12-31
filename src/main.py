
from utilities.crearListaCanciones import crearListaCanciones
from utilities.crearPlaylistCanciones import crearPlaylistCanciones
from utilities.ordenarPlaylistAleatorio import crearPlaylistRandom
from utilities.conseguirLugarCanciones import conseguirLugarCanciones
from utilities.unirCancionYLugar import unirCancionYlugar
from utilities.lanzarVLC import lanzarVLC

def playAll (libreriaVar):

    ListaCanciones = crearListaCanciones(libreriaVar) 
    PlaylistCanciones = crearPlaylistCanciones(ListaCanciones)
    PlaylistRandom = crearPlaylistRandom(PlaylistCanciones)
    LugarCanciones = conseguirLugarCanciones(libreriaVar)
    PlaylistFinal = unirCancionYlugar(PlaylistRandom,LugarCanciones)
    LanzarVLC = lanzarVLC (PlaylistFinal)
    



if __name__ == "__main__":

    libreriaVar = {"California Uber Alles":
                {"track-number": 2, "location": ".\\libreria\\California_Uber_Alles.mp3"},
            "King_Kunta": 
                {"track-number": 5, "location": ".\\libreria\\King_Kunta.mp3"},
            "Against the moon":
                {"track-number": 1, "location": ".\\libreria\\against_the_moon.mp3"},
            "Headless":
                {"track-number": 4,  "location": ".\\libreria\\Headless.mp3"}
            }
    playAll(libreriaVar)