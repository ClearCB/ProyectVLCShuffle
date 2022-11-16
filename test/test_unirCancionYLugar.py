import pytest
from src.funciones.unirCancionYLugar import unirCancionYlugar


@pytest.mark.unirCancionYLugar
def test_unirCancionYLugar():
    
    playlistRandom = {2: 'California Uber Alles', 1: "Elvis' Flaming Star", 3: 'King Kunta', 4: 'Against the moon', 5: 'Headless'}

    lugarCancion = {'California Uber Alles': '.\\libreria\\California_Uber_Alles.mp3', "Elvis' Flaming Star": ".\\libreria\\Elvis' Flaming Star.flac", 'King Kunta': '.\\libreria\\King_Kunta.mp3', 'Against the moon': '.\\libreria\\against the moon.mp3', 'Headless': '.\\libreria\\Headless.mp3'}


    assert (unirCancionYlugar(playlistRandom, lugarCancion)) == {2: {'California Uber Alles': '.\\libreria\\California_Uber_Alles.mp3'}, 1: {"Elvis' Flaming Star": ".\\libreria\\Elvis' Flaming Star.flac"}, 3: {'King Kunta': '.\\libreria\\King_Kunta.mp3'}, 4: {'Against the moon': '.\\libreria\\against the moon.mp3'}, 5: {'Headless': '.\\libreria\\Headless.mp3'}}

