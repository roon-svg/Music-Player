import os

def MusicPlays():
    musiclist = []
    for x in os.listdir(r"C:\Users\nahm1\OneDrive\Documents\GitHub\Music-Player\Application\Music"):
        if x.endswith(".mp3"):
            # Saves only text file present in My Folder
            musiclist.append(x)
            #print(musiclist[x],"\n")
    return musiclist