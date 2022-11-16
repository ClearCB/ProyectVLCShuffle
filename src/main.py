import subprocess
import random

from funciones.conseguirLugarCanciones import conseguirLugarCanciones
from funciones.crearListaCanciones import crearListaCanciones
from funciones.crearPlaylistCanciones import crearPlaylistCanciones
from funciones.lanzarVLC import lanzarVLC
from funciones.ordenarPlaylistAleatorio import crearPlaylistRandom
from funciones.unirCancionYLugar import unirCancionYlugar

def playAll (libreria):

    conseguirLugarCanciones(libreria)
    crearPlaylistRandom(libreria)
    crearPlaylistCanciones(libreria)
    crearListaCanciones(libreria)
    unirCancionYlugar(libreria)
    lanzarVLC(libreria)




if __name__ == "__main__":

    libreria = {"California Uber Alles":
                {"track-number": 2, "location": "C:/Users/abelc/Desktop/PROYECTO-PYTHO/libreria/California_Uber_Alles.mp3"},
            "Elvis' Flaming Star": 
                {"track-number": 5, "location": "C:/Users/abelc/Desktop/PROYECTO-PYTHO/libreria/King_Kunta.mp3"},
            "Against the moon":
                {"track-number": 1, "location": "C:/Users/abelc/Desktop/PROYECTO-PYTHO/libreria/against_the_moon.mp3"},
            "Headless":
                {"track-number": 4,  "location": "C:/Users/abelc/Desktop/PROYECTO-PYTHO/libreria/Headless.mp3"}
            }
    playAll(libreria)