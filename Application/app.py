from flask import Flask, render_template
from static.Playlist import MusicPlays


MusicList = MusicPlays()

for n in range(len(MusicList)):
    audio = MusicList[n]




app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', value=audio) # This makes the initial page the website go to index.

if __name__ == "__main__":
    app.run(debug=True)