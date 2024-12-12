from static.Playlist import MusicPlays, AlbumsList
from static.Queue import *
import random, os, pygame

#This gets the music player ready and allows for the song to go an event when the song ends
pygame.mixer.init()
Song_End = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(Song_End)

# This mnakes a list with all of the mp3 files in a specified folder.
def MusicPlays(album):

    song_list = []
    for x in os.listdir(r"Application\Music\\" + str(album)):
        if x.endswith(".mp3"):
            # Saves only text file present in My Folder
            song_list.append(x)
            #print(musiclist[x],"\n")
    return song_list

# This gets all of the folders in the Music folder
def AlbumsList():
    albumlist = []
    for x in os.listdir(r"Application\Music"):
        albumlist.append(x)
    return albumlist

# This puts the songs in a selected album into the Queue
def load_music(album):
    global playlist

    album = MusicPlays(album)
    playlist = Queue(len(album))
    for song in album:
        playlist.enqueue(song)
    return playlist

# This plays the song using the pygames mixer module.
def play_music(album, event=None):
    pygame.mixer.music.load("Application\\Music\\" + album + "\\" + playlist.element_pointer())
    pygame.mixer.music.play()

# This pauses the song
def pause_song(event=None):
    pygame.mixer.music.pause()

# This changes the pointer into the next element and plays that.
def next_song(album, event=None):
    pygame.mixer.music.load("Application\\Music\\" + album + "\\" + playlist.next_element())
    pygame.mixer.music.play()

# This changes the pointer into the previous element and plays that.
def prev_song(album, event=None):
    pygame.mixer.music.load("Application\\Music\\" + album + "\\" + playlist.previous_element())
    pygame.mixer.music.play()

#This suffles the songs in the folder and puts it back into the queue
def shuffle_songs(event=None):
    shuffledlist = random.shuffle(playlist.queue_elements)
    for n in shuffledlist:    
        playlist.dequeue()
        playlist.enqueue(n)