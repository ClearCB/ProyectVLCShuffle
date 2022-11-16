def crearPlaylistCanciones(listaCanciones):

    assert isinstance(listaCanciones, list)

    playList = {}
    index = 1
    for song in listaCanciones:

        playList[index] = song
        index += 1
    
    return playList







if __name__ == "__main__":

    listaCanciones =  ["California Uber Alles","Elvis' Flaming Star","King Kunta","Against the moon","Headless"]

    crearPlaylistCanciones(listaCanciones)