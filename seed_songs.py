# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# 🌿 SEED SONGS — Populate the Shrine with Praise Scrolls
# 📍 Purpose: Insert 8 sacred songs into shrine.db
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

from flask import Flask
from models import db, Song

# 🌿 Minimal Flask app to access the shrine
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shrine.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 🧎🏾‍♂️ Seed ritual
with app.app_context():
    songs = [

        
    ]

    for song in songs:
            if not db.session.get(Song, song.id):
               db.session.add(song)
               print(f"🌟 Seeded: {song.title}")

    db.session.commit()
    print("✅ All songs seeded into shrine.db")

