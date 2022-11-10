# The parametres is a song and a library in which one we will check it

def songIsInList(song, library):

    # Now we will make two preconditions to check if the parametres are correct
    # "isinstance" allows us to check if the parametres are the type we are giving

    assert isinstance(song, str)
    assert isinstance(library, dict)

    # Now we check if the song is in dict

    if song in library:
        return True
    else:
        return False

# Now we will make a new module in which we will check if the song is repetead or not

def songIsUnique(playlist):

    # We check if the playlist is a dictionary
    
    assert isinstance(playlist, dict)

    # Now we make a list with the values of the dict (songs names) and check if they are unique

    playlistValues = list(playlist.values())

    for i in playlist:

        iCount = playlist.count(i)
        if iCount > 1:
            return False
        else:
            return True
