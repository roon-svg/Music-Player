import tkinter as tk
from tkinter import *
#import tkinter.messagebox
import os

def SearchingWindow():
    #searching =tk.Tk()
    global searching
    global search_list_box

    searching = tk.Tk()
    fram = Frame(searching)
    searching.title("Search for Song")
    searching.geometry("500x500")

    Label(fram, text="Search for a song").pack(side=LEFT)
    search_entry = Entry(fram)
    search_entry.pack(side=LEFT, fill=BOTH, expand=1)
    search_btn = Button(fram, text=("Find Song"), command=lambda: Find(search_entry))
    search_btn.pack(side=RIGHT)
    fram.pack(side=TOP)
    search_list_box = Listbox(background="Navy", foreground="White", selectmode=SINGLE, width=100, height=25)
    PopulateListBox()
    search_list_box.pack(side=BOTTOM)
    go_to_btn = Button(text="Song Folder", command=GoTo)
    go_to_btn.pack(side=BOTTOM)

    searching.mainloop()

def PopulateListBox():
    global allsongs
    x=-1
    allsongs = []
    for album in os.listdir(r"Application\Music"):
        for song in os.listdir(r"Application\Music\\" + str(album)):
            x +=1
            if song.endswith(".mp3"):
                allsongs.append(album + "\\" + song)
                search_list_box.insert(x, str(song))

def Find(search_entry):
    linear_search(allsongs, search_entry)
    search_list_box.delete(0, END)

def linear_search(list, search_entry):
    list
    pass

def GoTo():
    searching.messagebox.showinfo()

