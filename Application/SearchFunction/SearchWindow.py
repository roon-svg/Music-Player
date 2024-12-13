import tkinter as tk
from tkinter import *
import os

def SearchingWindow():
    global searching
    global search_list_box
    global search_input

    # This sets up tkinter and the search window
    searching = tk.Tk()
    fram = Frame(searching)
    searching.title("Search for Song")
    searching.geometry("500x500")

    # This sets up the variable the search box is going to go into
    search_input = tk.StringVar(fram)

    # These are the different elements in the searching window.
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

# This goes through all of the different songs in every folder and adds it to a list called allsongs
def PopulateListBox():
    global allsongs
    allsongs = []
    for album in os.listdir(r"Application\Music"):
        for song in os.listdir(r"Application\Music\\" + str(album)):
            if song.endswith(".mp3"):
                allsongs.append(album + "\\" + song)
                search_list_box.insert(END, str(song))

def Find():
    # This deletes everythin within the searchbox
    search_list_box.delete(0, END)
    # This gets whatever is inputted by the user in the search box
    entry_list = search_input.get()
    print(entry_list)
    # This goes through all of the songs individually
    for song in allsongs:
        # Whenever there is match with the searched string 
        # and the song name then it is inserted into the listbox
        if  (linear_search(song, entry_list)):
            search_list_box.insert(END, song)


# This does a linear search to find the similarity within strings
def linear_search(songname, search_entry):
    n = 0
    x = 0
    # This stops whenever there are no more letters to compare
    while (n < len(search_entry) and x < len(songname)):
        # Whenever there is a string that matches n gets bigger
        if (search_entry[n] == songname[x]):
            n += 1
        x += 1
    # When n is the same as whatever was inputted by the user
    return n == len(search_entry)