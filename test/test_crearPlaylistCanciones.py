import pytest
from programs.crearPlaylistCanciones import crearPlaylistCanciones

listaCanciones =  ["California Uber Alles","Elvis' Flaming Star","King Kunta","Against the moon","Headless"]

@pytest.mark.crearPlaylistCancionesUno
def test_crearListaCanciones():

    assert crearPlaylistCanciones(listaCanciones) == {1:"California Uber Alles",2:"Elvis' Flaming Star",3:"King Kunta",4:"Against the moon",5:"Headless"}


