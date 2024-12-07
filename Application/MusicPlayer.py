from tkinter import *
import pygame
import os
from static.Playlist import MusicPlays, AlbumsList
from static.Queue import *
from static.Controls import *
from functools import partial

# This initialises the tkinter application
root = Tk()
root.title("Music Player")
# This sets the initial geometry tkinter goes into. You can change the size afterwards
root.geometry("500x500")


#This gets the music player ready and allows for the song to go an event when the song ends
pygame.mixer.init()
Song_End = pygame.USEREVENT + 1 # This allows for the song to loop
pygame.mixer.music.set_endevent(Song_End)

# This sets up the loop box
albumlist = Listbox(root, background="Navy", foreground="White", selectmode=SINGLE, width=100, height=25)

# This puts the folders in the Music folder into the listbox
def albumListBox():
    global albumlist

    albumlist.delete(0,END) # Clears everything in the listbox
    folder = AlbumsList()
    for i in range(len(folder)):
        for album in folder:
            albumlist.insert(i, album)
    albumlist.pack()
    albumlist.curselection()

# This makes an area to put the GUI elements into
albumListBox()
control_frame = Frame(root)
control_frame.pack()

# When you submit an album then it gets all of the songs from that album into the listbox.
def onselect():
    global albumlist
    global manysongs

    folder = MusicPlays(albumlist.get(albumlist.curselection()))
    albumlist.delete(0,END)
    albumlist.insert(0, folder.element_pointer())
    for i in range(folder.QueueSize()):
        song = folder.next_element()
        albumlist.insert(i, song)
    AlbumTitle = Label(text=albumlist.get(albumlist.curselection()))
    albumlist.pack()
    manysongs = load_music(folder)
    control_frame = Frame(root)
    control_frame.pack()

MusicPlayer = play_music(manysongs)

playBtn = Button(control_frame,text=">", command=MusicPlayer, width=5)
pauseBtn = Button(control_frame,text="||", command=pause_song, width=5)
nextSongBtn = Button(control_frame,text=">>", command=next_song, width=5)
prevSongBtn = Button(control_frame,text="<<", command=prev_song, width=5)
ShuffleBtn = Button(control_frame,text="Shuffle", command=shuffle_songs, width=5)
SubmitBtn = Button(control_frame, text="Submit", command=onselect, width=5)
BackBtn = Button(control_frame, text="Back", command=albumListBox, width=5)

prevSongBtn.grid(row=0,column=0)
playBtn.grid(row=0,column=1)
pauseBtn.grid(row=0,column=2)
nextSongBtn.grid(row=0,column=3)
ShuffleBtn.grid(row=0,column=4)
SubmitBtn.grid(row=2,column=3)
BackBtn.grid(row=2,column=2)

root.mainloop()