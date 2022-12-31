def conseguirLugarCanciones(libreria):

    assert isinstance(libreria, dict)

    diccLugaresCancion = {}

    for cancion in libreria:

        cancionLocalizacion = libreria[cancion]["location"]
        diccLugaresCancion[cancion] = cancionLocalizacion
    
    return diccLugaresCancion

if __name__ == "__main__":

    libreria = {"California Uber Alles":
                {"track-number": 2, "location": "C:/Users/abelc/Desktop/PROYECTO-PYTHO/libreria/California_Uber_Alles.mp3"},
            "King_Kunta": 
                {"track-number": 5, "location": "C:/Users/abelc/Desktop/PROYECTO-PYTHO/libreria/King_Kunta.mp3"},
            "Against the moon":
                {"track-number": 1, "location": "C:/Users/abelc/Desktop/PROYECTO-PYTHO/libreria/against_the_moon.mp3"},
            "Headless":
                {"track-number": 4,  "location": "C:/Users/abelc/Desktop/PROYECTO-PYTHO/libreria/Headless.mp3"}
    }
    conseguirLugarCanciones(libreria)