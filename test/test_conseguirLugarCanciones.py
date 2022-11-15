import pytest
from programs.conseguirLugarCanciones import conseguirLugarCanciones

libreria = {"California Uber Alles":
                {"track-number": 2, "location": "..\\libreria\\California_Uber_Alles.mp3"},
            "Elvis' Flaming Star": 
                {"track-number": 3,  "location": "..\\libreria\\Elvis' Flaming Star.flac"},
            "King Kunta":
                {"track-number": 5, "location": "..\\libreria\\King_Kunta.mp3"},
            "Against the moon":
                {"track-number": 1, "location": "..\\libreria\\against the moon.mp3"},
            "Headless":
                {"track-number": 4,  "location": "..\\libreria\\Headless.mp3"}
            }

# @pytest.mark.conseguirLugarCanciones
def test_conseguirLugarCanciones():

    rutaDicc = {'California Uber Alles':'..\\libreria\\California_Uber_Alles.mp3', 
"Elvis' Flaming Star":"..\\libreria\\Elvis' Flaming Star.flac", 
'King Kunta':'..\\libreria\\King_Kunta.mp3', 
'Against the moon':'..\\libreria\\against the moon.mp3',
 'Headless':'..\\libreria\\Headless.mp3'}

    assert conseguirLugarCanciones(libreria) == rutaDicc


