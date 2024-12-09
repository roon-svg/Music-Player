import os
from static.Queue import Queue

def MusicPlays(Album):
    playlist = Queue(100)
    for x in os.listdir(r"Application\Music\\" + str((Album))):
        if x.endswith(".mp3"):
            # Saves only text file present in My Folder
            playlist.enqueue(x)
            #print(musiclist[x],"\n")
    return playlist

def AlbumsList():
    albumlist = []
    for x in os.listdir(r"Application\Music"):
        albumlist.append(x)
        #print(musiclist[x],"\n")
    return albumlist
