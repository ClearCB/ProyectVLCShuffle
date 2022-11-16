import subprocess

def lanzarVLC(libreriaLugarPosYNombre):

    rutas = []
    comandoExeVlc = "C:\\Users\\xuloa\\OneDrive\\Escritorio\\vlc"
    lineaComando = comandoExeVlc
    separador = " "

    libreriaLugarPosYNombre = dict(sorted(libreriaLugarPosYNombre.items()))
    
    
    for cancion in libreriaLugarPosYNombre:

        dictCancion = libreriaLugarPosYNombre[cancion]
        dictCancionKeys = list(dictCancion.keys())

        for cancionNombre in dictCancionKeys:

            ruta = dictCancion[cancionNombre]
            lineaComando = lineaComando + separador + ruta

    args = lineaComando.split(" ")
    ejecutarVLC = subprocess.Popen(args)





if __name__ == "__main__":

    libreriaLugarPosYNombre =  {2: {'California Uber Alles': 'C:\\Users\\abelc\\Desktop\\PROYECTO-PYTHO\\libreria\\California_Uber_Alles.mp3'}, 3: {'King Kunta': 'C:\\Users\\abelc\\Desktop\\PROYECTO-PYTHO\\libreria\\King_Kunta.mp3'}, 4: {'Against the moon': 'C:\\Users\\abelc\\Desktop\\PROYECTO-PYTHO\\libreria\\against_the_moon.mp3'}, 5: {'Headless': 'C:\\Users\\abelc\\Desktop\\PROYECTO-PYTHO\\libreria\\Headless.mp3'}}

    lanzarVLC(libreriaLugarPosYNombre)