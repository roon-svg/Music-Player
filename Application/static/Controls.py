from static.Playlist import MusicPlays
import pygame
from static.Queue import *

#This gets the music player ready and allows for the song to go an event when the song ends
pygame.mixer.init()
Song_End = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(Song_End)
global manysongs


def load_music(songlist):
    #global currentSong
    global album
    global manysongs

    album = MusicPlays()
    manysongs = Queue(len(album))
    for song in album:
        songlist.insert("end", song)
        manysongs.enqueue(song)
    songlist.selection_set(0)

def play_music(event=None):
    global currentSong

    # currentSong = album[songlist.curselection()[0]]
    # pygame.mixer.music.load("Application\\Music\\" + currentSong)
    pygame.mixer.music.load("Application\\Music\\" + manysongs.element_pointer())
    pygame.mixer.music.play()

def pause_song(event=None):
    pygame.mixer.music.pause()

def next_song(event=None):
    pygame.mixer.music.load("Application\\Music\\" + manysongs.next_element())
    pygame.mixer.music.play()

def prev_song(event=None):
    pygame.mixer.music.load("Application\\Music\\" + manysongs.previous_element())
    pygame.mixer.music.play()

def shuffle_songs(event=None):
    pass