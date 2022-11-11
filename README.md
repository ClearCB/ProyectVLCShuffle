# Proyect-VLC-shuffle

Make a program in python that creates a random song list and reproduces it at VLC.

I'll follow the code of my teacher and i'll try to implement everychange with git.

Firts i will try to replicate his code and then ill make it bymyself, this exercise is to train git and their commands.

## First step

First of all i'll create modules that will allow me to check if the input is the correct one.

The first module will be called "songIsInList" and it will check if the song is acctually at the list.

Then ill make a module called "songIsUnique" and it will check if the song is repeated or not.

Since i forgot to import random and it will be needed later, ill import at this commit and add a new feature that will select a random song from the library.

We add a new featur which consist on creating a playlist so we have our dictionary with the songs

Then we will add the number of the song and each title.

After all this, we will make a program to executa VLC and to get all the songs. So we need to create a folder called "library" in which we will have the songs we have to make the list. 

To make this proces, we will have to import three basics libraries from python to execute the program (subprocess, shlex and os)