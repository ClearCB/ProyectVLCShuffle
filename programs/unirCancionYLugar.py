def unirCancionYlugar(playlistRandom, diccionarioLugar):

    assert isinstance(playlistRandom,dict)

    playlistYLugar = {}
    playlistLugarYPos = {}

    for i in playlistRandom:

        tituloCancion = playlistRandom[i]

        lugarCancion = diccionarioLugar[tituloCancion]

        playlistYLugar[tituloCancion] = lugarCancion

    index = 1

    for i in playlistYLugar:

        playlistLugarYPos[index] = {i:playlistYLugar[i]}
        index += 1

    return playlistLugarYPos


if __name__ == "__main__":

    playlistRandom = {2: 'California Uber Alles', 1: "Elvis' Flaming Star", 3: 'King Kunta', 4: 'Against the moon', 5: 'Headless'}

    diccionarioLugar = {'California Uber Alles': '.\\libreria\\California_Uber_Alles.mp3', "Elvis' Flaming Star": ".\\libreria\\Elvis' Flaming Star.flac", 'King Kunta': '.\\libreria\\King_Kunta.mp3', 'Against the moon': '.\\libreria\\against the moon.mp3', 'Headless': '.\\libreria\\Headless.mp3'}

    unirCancionYlugar ( playlistRandom, diccionarioLugar)