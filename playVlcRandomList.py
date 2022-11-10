import random

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

# Now we will make a module to select a random song, but first we will check if the library is a dict
# so we can continue.
def selectRandomSong(library):

    assert isinstance (library,dict)

    # No we will take the title of the song from the library so we have a random song

    randomSong = random.choice(list(library.keys()))

    # After we selected a random song, we have to confirm that is actualy a song in the list and its not other

    assert songIsInList(randomSong, library)

    # And we return the name of the song

    return str(randomSong)

    