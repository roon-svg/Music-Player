from tkinter import *
import pygame
from static.Playlist import MusicPlays
from static.LinkedList import LinkedList

# This initialises the tkinter application
root = Tk()
root.title("Music Player")
root.geometry("500x500")

#This gets the music player ready and allows for the song to go an event when the song ends
pygame.mixer.init()
Song_End = pygame.USEREVENT + 1
pygame.mixer.music.set_endevent(Song_End)

def load_music():
    tempStorage = MusicPlays()
    for song in tempStorage:
        songlist.insert("end", song)
    songlist.selection_set(0)
    currentSong = tempStorage[songlist.curselection()[0]]

def play_music(event=None):
    tempStorage = MusicPlays()
    MusicList = LinkedList()
    for n in range(tempStorage):
        MusicList.append(tempStorage[n])

    pygame.mixer.music.load(MusicList.get_head_node)
    pygame.mixer.music.play()

songlist = Listbox(root, background="Navy", foreground="White", width=100, height=25)
songlist.pack()

control_frame = Frame(root)
control_frame.pack()

playBtn = Button(control_frame,text=">", command=play_music, width=10)
pauseBtn = Button(control_frame,text="||", command=play_music, width=10)
nextSongBtn = Button(control_frame,text=">>", command=play_music, width=10)
prevSongplayBtn = Button(control_frame,text="<<", command=play_music, width=10)
ShuffleBtn = Button(control_frame,text="Shuffle", command=play_music, width=10)
prevSongplayBtn.pack()
playBtn.pack()
pauseBtn.pack()
nextSongBtn.pack()
ShuffleBtn.pack()

root.mainloop()