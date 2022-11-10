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

    return str(randomSong), "The song is not a key from the library dictionary"

# Now, we will start creating the playlist dictionary, in which keys are integrers and values the name of the song.

def playlistCreate(songNum):

    keyNumPlaylist = songNum

    # Now we create a functions that will append the song name at the playlist dict

    def songAppend (song, playlist):

        # Now we will check if the playlist is a dict and that the song is not already in the playlist

        listValuesPlaylist = list(playlist.values())

        assert isinstance(playlist, dict), "playlist is not a dictionary"
        assert song not in listValuesPlaylist

        # Now we will start adding numbers to the index dicc so we add in a different spot the song we get

        nonlocal keyNumPlaylist
        keyNumPlaylist += 1
        
        # Now we relate the value and the key to the playlist dict 
        playlist[keyNumPlaylist] = str(song)
        return keyNumPlaylist
        
    return songAppend

# Now we will print which songs are we going to use in our playlist

def printSongSelected(playlist):
    
    # We check if its a dict

    assert isinstance(playlist,dict)

    keysSorted = sorted(playlist.keys())

    # Now we iterate the keysSorted to print each song and its order

    for songNum in keysSorted:

        print(str(songNum + ": " + str(playlist[songNum])))


# Now we make the program to execute VLC

def launchVLC(library,playlist):

    # we need to find the songs at the "library" directory

    import subprocess
    import shlex
    import os
    
    windowsPathVLC = "C:\Users\xuloa\OneDrive\Escritorio\vlc"
    windowsCommandLine = windowsPathVLC
    separator = " "


    for numSong in sorted(playlist.keys()):

        randomSong = playlist[numSong]
        try:
            pathAcces = library[randomSong]["location"]
        except KeyError:
            print("the song is not at the library") 
        else:
            # we check if the path is correct
            if os.path.exists(str(pathAcces)):
                windowsCommandLine = windowsCommandLine + separator + str(pathAcces)
            else:
                pass
    args = shlex.split(windowsCommandLine)

    try:
        
        procesVlc = subprocess.Popen(args)
        
    except:
        print("the archive does not exist")

    except:
        print("Not valid arguments")
    else:
        print("Launching VLC with random playlist")

