    x=-1
    allsongs = []
    for album in os.listdir(r"Application\Music"):
        for song in os.listdir(r"Application\Music\\" + str(album)):
            x +=1
            if song.endswith(".mp3"):
                allsongs.append(album + "\\" + song)
                search_list_box.insert(x, str(song))
