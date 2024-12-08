import tkinter as tk
import tkinter

def SearchingWindow():
    #searching =tk.Tk()
    searching = tkinter()
    searching.title("Search for Song")
    searching.geometry("500x500")

    search_label = searching.Label(text="Search for a song")
    search_label.pack()
    search_entry = searching.Entry(searching, width=40)
    search_entry.pack()

    searching.mainloop()

SearchingWindow()
