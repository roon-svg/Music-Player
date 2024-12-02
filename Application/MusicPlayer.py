from tkinter import *
import pygame
import os
from static.Playlist import MusicPlays
from static.Queue import *
from static.Controls import *

# This initialises the tkinter application
root = Tk()
root.title("Music Player")
root.geometry("500x500")

#This gets the music player ready and allows for the song to go an event when the song ends
pygame.mixer.init()
Song_End = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(Song_End)

"""
def load_music():
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
    global manysongs

    # currentSong = album[songlist.curselection()[0]]
    # pygame.mixer.music.load("Application\\Music\\" + currentSong)
    pygame.mixer.music.load(manysongs.next_element())
    pygame.mixer.music.play()
"""
album = MusicPlays()
songlist = Listbox(root, background="Navy", foreground="White", width=100, height=25)
for i in range(len(album)):
    for song in album:
        songlist.insert(i, song)
songlist.pack()

control_frame = Frame(root)
control_frame.pack()

playBtn = Button(control_frame,text=">", command=play_music, width=10)
pauseBtn = Button(control_frame,text="||", command=play_music, width=10)
nextSongBtn = Button(control_frame,text=">>", command=next_song, width=10)
prevSongBtn = Button(control_frame,text="<<", command=prev_song, width=10)
ShuffleBtn = Button(control_frame,text="Shuffle", command=shuffle_songs, width=10)
prevSongBtn.pack()
playBtn.pack()
pauseBtn.pack()
nextSongBtn.pack()
ShuffleBtn.pack()

root.mainloop()