import os

def MusicPlays():
    musiclist = []
    for x in os.listdir("C:\Users\nahm1\OneDrive\Documents\GitHub\Music-Player\Application\Music"):
        if x.endswith(".mp3"):
            # Prints only text file present in My Folder
            musiclist.append()