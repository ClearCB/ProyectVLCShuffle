def unirCancionYlugar(playlistRandom, diccionarioLugar):

    assert isinstance(playlistRandom,dict)

    playlistYLugar = {}
    playlistLugarYPos = {}

    indexListRandom = list(playlistRandom.keys())
    index = 0
    indexSelect = indexListRandom[index]


    for i in playlistRandom:

        tituloCancion = playlistRandom[i]

        lugarCancion = diccionarioLugar[tituloCancion]

        playlistYLugar[tituloCancion] = lugarCancion


    for i in playlistYLugar:

        indexSelect = indexListRandom[index]
        playlistLugarYPos[indexSelect] = {i:playlistYLugar[i]}
        index +=1


    return playlistLugarYPos
