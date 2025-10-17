# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# 🌿 TEST SHRINE — app1.py
# 📍 Purpose: Read songs from shrine.db and display on /songs-from-db
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

from flask import Flask, render_template
from models import db, Song

# 🌿 Shrine Initialization
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shrine.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 🧎🏾‍♂️ Route to display all seeded songs
@app.route("/songs-from-db")
def songs_from_db():
    with app.app_context():
        songs = Song.query.all()
        return render_template("songs_from_db.html", songs=songs, title="Seeded Songs")

# 🔥 Shrine Activation
if __name__ == "__main__":
    app.run(debug=True)

