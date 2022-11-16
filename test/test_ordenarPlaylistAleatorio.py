import pytest
from src.funciones.ordenarPlaylistAleatorio import crearPlaylistRandom

playlistCanciones =  {1: 'California Uber Alles', 2: "Elvis' Flaming Star", 3: 'King Kunta', 4: 'Against the moon', 5: 'Headless'}
keysPlaylistCanciones = list(playlistCanciones.keys()) 

@pytest.mark.crearPlaylistRandomUno
def test_crearListaCanciones():

    newList = crearPlaylistRandom(playlistCanciones)

    keysNewList = list(newList.keys())

    assert (keysNewList) != keysPlaylistCanciones




