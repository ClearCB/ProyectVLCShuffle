import subprocess

def lanzarVLC(libreriaLugarPosYNombre):

    rutas = []
    comandoExeVlc = r"D:\vlc\vlc"
    lineaComando = comandoExeVlc
    separador = " "

    libreriaLugarPosYNombre = dict(sorted(libreriaLugarPosYNombre.items()))
    
    
    for cancion in libreriaLugarPosYNombre:

        dictCancion = libreriaLugarPosYNombre[cancion]
        dictCancionKeys = list(dictCancion.keys())

        for cancionNombre in dictCancionKeys:

            ruta = dictCancion[cancionNombre]
            lineaComando = lineaComando + separador + str(ruta)

    ejecutarVLC = subprocess.run(lineaComando)





if __name__ == "__main__":

    libreriaLugarPosYNombre =  {2: {'California Uber Alles': r'C:\Users\abelc\Desktop\PROYECTO-PYTHO\libreria\California_Uber_Alles.mp3'}, 3: {'King Kunta': r'C:\Users\abelc\Desktop\PROYECTO-PYTHO\libreria\King_Kunta.mp3'}, 4: {'Against the moon': r'C:\Users\abelc\Desktop\PROYECTO-PYTHO\libreria\against_the_moon.mp3'}, 5: {'Headless': r'C:\Users\abelc\Desktop\PROYECTO-PYTHO\libreria\Headless.mp3'}}

    lanzarVLC(libreriaLugarPosYNombre)