import tkinter as tk
from tkinter import *
#import tkinter.messagebox
import os

def SearchingWindow():
    #searching =tk.Tk()
    global searching
    global search_list_box
    global search_input

    searching = tk.Tk()
    fram = Frame(searching)
    searching.title("Search for Song")
    searching.geometry("500x500")

    search_input = tk.StringVar(fram)

    Label(fram, text="Search for a song").pack(side=LEFT)
    search_entry = Entry(fram, textvariable=search_input)
    search_entry.pack(side=LEFT, fill=BOTH, expand=1)
    search_btn = Button(fram, text=("Find Song"), command=Find)
    search_btn.pack(side=RIGHT)
    fram.pack(side=TOP)
    search_list_box = Listbox(background="Navy", foreground="White", selectmode=SINGLE, width=100, height=25)
    PopulateListBox()
    search_list_box.pack(side=BOTTOM)
    go_to_btn = Button(text="Refresh", command=PopulateListBox)
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

def Find():
    search_list_box.delete(0, END)
    #a = list(allsongs[0])
    entry_list = search_input.get()
    print(entry_list)
    #b = entry_list.split()
    for song in allsongs:
        if  (linear_search(song, entry_list)):
            search_list_box.insert(END, song)


def linear_search(songname, search_entry):
    n = 0
    x = 0
    while (n < len(search_entry) and x < len(songname)):
        print(search_entry[n])
        if (search_entry[n] == songname[x]):
            n += 1
        x += 1
    return n == len(search_entry)