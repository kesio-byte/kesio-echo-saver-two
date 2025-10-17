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
        Song(id="dance-in-light", title="Dance in Light", genre="Gospel Anthem", bpm=92,
             language="Chichewa & English", theme="Spiritual transformation, communal joy, radiant praise",
             cover_caption="From ache to joy, sealed in light",
             cover_style="Golden rays, dancing silhouettes, glowing altar",
             music_file="dance-in-light.mp3"),

        Song(id="echo-of-mercy", title="Echo of Mercy", genre="Acoustic Gospel", bpm=76,
             language="English", theme="Grace, forgiveness, gentle restoration",
             cover_caption="Mercy echoes through broken places",
             cover_style="Soft strings, misty hills, sunrise tones",
             music_file="echo-of-mercy.mp3"),

        Song(id="rise-malawi", title="Rise Malawi", genre="Afrobeat Gospel", bpm=108,
             language="Chichewa & English", theme="National hope, unity, spiritual awakening",
             cover_caption="Malawi rises in rhythm and light",
             cover_style="Flag colors, dancing feet, radiant drums",
             music_file="rise-malawi.mp3"),

        Song(id="altar-call", title="Altar Call", genre="Worship Ballad", bpm=64,
             language="English", theme="Surrender, healing, sacred invitation",
             cover_caption="Come as you are, the altar is open",
             cover_style="Candlelight, open hands, soft robes",
             music_file="altar-call.mp3"),

        Song(id="nicetu-blessing", title="Nicetu Blessing", genre="Family Gospel", bpm=88,
             language="Chichewa", theme="Family joy, generational blessing, childlike praise",
             cover_caption="Her voice is the blessing",
             cover_style="Child’s smile, warm fabrics, ancestral glow",
             music_file="nicetu-blessing.mp3"),

        Song(id="testimony-rain", title="Testimony Rain", genre="Gospel Praise", bpm=100,
             language="English", theme="Overflowing gratitude, public praise, spiritual rain",
             cover_caption="Rain of praise, flood of joy",
             cover_style="Umbrellas, dancing crowd, radiant droplets",
             music_file="testimony-rain.mp3"),

        Song(id="sacred-visit", title="Sacred Visit", genre="Instrumental", bpm=72,
             language="Instrumental", theme="Divine encounter, quiet reverence, spiritual presence",
             cover_caption="He visited, and we were changed",
             cover_style="Empty chair, glowing doorway, soft light",
             music_file="sacred-visit.mp3"),

        Song(id="echo-saver-theme", title="Echo Saver Theme", genre="Gospel Tech", bpm=120,
             language="English", theme="Digital praise, archival joy, sacred memory preservation",
             cover_caption="Saving echoes, sealing joy",
             cover_style="Circuit board altar, glowing waveform, scrolls",
             music_file="echo-saver-theme.mp3"),
    ]

    for song in songs:
            if not db.session.get(Song, song.id):
               db.session.add(song)
               print(f"🌟 Seeded: {song.title}")

    db.session.commit()
    print("✅ All songs seeded into shrine.db")

