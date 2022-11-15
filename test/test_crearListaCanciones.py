import pytest
from programs.crearListaCanciones import crearListaCanciones

libreria = {"California Uber Alles":
                {"track-number": 2, "location": "./libreria/California_Uber_Alles.mp3"},
            "Elvis' Flaming Star": 
                {"track-number": 3,  "location": "./libreria/Elvis' Flaming Star.flac"},
            "King Kunta":
                {"track-number": 5, "location": "./libreria/King_Kunta.mp3"},
            "Against the moon":
                {"track-number": 1, "location": "./libreria/against the moon.mp3"},
            "Headless":
                {"track-number": 4,  "location": "./libreria/Headless.mp3"}
            }

@pytest.mark.crearListaCancionUno
def test_crearListaCanciones():

    assert crearListaCanciones(libreria) == ["California Uber Alles","Elvis' Flaming Star","King Kunta","Against the moon","Headless"]


