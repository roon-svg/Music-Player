import os

def MusicPlays(Album):
    musiclist = []
    for x in os.listdir(r"Application\Music\\" + Album):
        if x.endswith(".mp3"):
            # Saves only text file present in My Folder
            musiclist.append(x)
            #print(musiclist[x],"\n")
    return musiclist

def Albums():
    albumlist = []
    for x in os.listdir(r"Application\Music"):
        albumlist.append(x)
        #print(musiclist[x],"\n")
    return albumlist
