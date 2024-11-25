from flask import Flask, render_template
from static.Playlist import MusicPlays


MusicList = MusicPlays()
# Creating an HTML file 
Func = open("GFG-1.html","w") 
   
# Adding input data to the HTML file 
Func.write("<html>\n<head>\n<title> \n </title>\n </head> <body>" +
           "</head> <body><h1>Music Player</h1>\ \n")
for n in MusicList():
    Func.write("<audio> src=\""+ MusicList[n] +"\"</audio")

Func.write("\n</body></html>") 
              
# Saving the data into the HTML file 
Func.close()



app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html') # This makes the initial page the website go to index.

if __name__ == "__main__":
    app.run(debug=True)