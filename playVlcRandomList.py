def playShuffle(library, playlist):

    assert isinstance(library,dict)
    songNum = 0
    updatePlaylist = playlistCreate(songNum)
    inputCommand = "p" 
    continueRep = True

    while inputCommand == "p" and continueRep == True:

        song = selectRandomSong(library)

        if song not in list (playlist.values()):
            actualSongNum = updatePlaylist(song,playlist)
            print ("Selected: " + str(playlist[actualSongNum]))
        else:
            inputCommand == "p"
        if len(library) == len(playlist):
            continueRep = False
            print("All songs included")
    assert songIsUnique(playlist)

    return True