import random

def crearPlaylistRandom(playlistCanciones):

    assert isinstance(playlistCanciones, dict)

    keysPlaylist = list(playlistCanciones.keys())

    finPlaylist = {}


    for key in playlistCanciones:

        cancion = playlistCanciones[key]
        indice = random.choice(keysPlaylist)
        finPlaylist[indice] = cancion
        keysPlaylist.remove(indice)
    
    return finPlaylist

if __name__ == "__main__":

    playlistCanciones =  {1: 'California Uber Alles', 2: "Elvis' Flaming Star", 3: 'King Kunta', 4: 'Against the moon', 5: 'Headless'}
    
    crearPlaylistRandom(playlistCanciones)