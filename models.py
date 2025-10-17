# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# 🌿 MODELS — Shrine Scrolls of Memory
# 📍 Purpose: Define database structure for songs, testimonies, and visits
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

from flask_sqlalchemy import SQLAlchemy

# 🌿 Initialize SQLAlchemy instance before using it
db = SQLAlchemy()

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# 📜 Song Model — Represents each praise scroll in the shrine
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
class Song(db.Model):
    id = db.Column(db.String, primary_key=True)  # Unique identifier for each song
    title = db.Column(db.String, nullable=False)  # Display title of the song
    genre = db.Column(db.String)  # Musical genre (e.g., Gospel, Afrobeat)
    bpm = db.Column(db.Integer)  # Beats per minute (tempo)
    language = db.Column(db.String)  # Language(s) used in lyrics
    theme = db.Column(db.String)  # Emotional or spiritual theme
    cover_caption = db.Column(db.String)  # Caption for the song’s visual cover
    cover_style = db.Column(db.String)  # Description of the cover’s visual style
    music_file = db.Column(db.String)  # Filename of the associated audio file

# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# 📜 Testimony Model — Captures user-submitted reflections
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
class Testimony(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each testimony
    title = db.Column(db.String, nullable=False)  # Title of the offering
    caption = db.Column(db.String)                # Poetic caption or reflection
    bpm = db.Column(db.Integer)                   # Beats per minute (if musical)
    genre = db.Column(db.String)                  # Genre of the offering
    language = db.Column(db.String)               # Language(s) used
    timestamp = db.Column(db.DateTime)            # Time of submission
    ip_address = db.Column(db.String)             # IP address of the submitter
    audio_filename = db.Column(db.String(120))    #store the filename of the audio scroll
    song_id = db.Column(db.String(80))            #This lets each testimony link to its metadata.



# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# 📜 Visit Model — Records each visit to the shrine
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
class Visit(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Unique ID for each visit
    timestamp = db.Column(db.DateTime)            # Time of visit
    ip_address = db.Column(db.String)             # Visitor’s IP address


