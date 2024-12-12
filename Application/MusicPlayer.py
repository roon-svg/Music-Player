from tkinter import *
from static.Queue import *
from static.Controls import *
from SearchFunction.SearchWindow import SearchingWindow

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
    global playlist
    global album

    album = albumlist.get(albumlist.curselection())
    manysongs = MusicPlays(album)
    load_music(album)
    albumlist.delete(0,END)
    albumlist.insert(0, manysongs[0])
    for i in range(len(manysongs)):
        for song in manysongs:
            albumlist.insert(i, song)
    albumlist.pack()
    control_frame = Frame(root)
    control_frame.pack() 


# This is where all of the buttons are set up
playBtn = Button(control_frame,text=">", command=lambda: play_music(album), width=5)
pauseBtn = Button(control_frame,text="||", command=pause_song, width=5)
nextSongBtn = Button(control_frame,text=">>", command=lambda: next_song(album), width=5)
prevSongBtn = Button(control_frame,text="<<", command=lambda: prev_song(album), width=5)
ShuffleBtn = Button(control_frame,text="Shuffle", command=lambda: shuffle_songs(album), width=5)
SubmitBtn = Button(control_frame, text="Submit", command=onselect, width=5)
BackBtn = Button(control_frame, text="Back", command=albumListBox, width=5)
SearchBtn = Button(control_frame, text="Search for Song", command=SearchingWindow, width=15)

# This is where the buttons are set in the aplication window
prevSongBtn.grid(row=1,column=0)
playBtn.grid(row=1,column=1)
pauseBtn.grid(row=1,column=2)
nextSongBtn.grid(row=1,column=3)
ShuffleBtn.grid(row=1,column=4)
SubmitBtn.grid(row=2,column=2)
BackBtn.grid(row=2,column=1)
SearchBtn.grid(rowspan=3,columnspan=2)


root.mainloop()