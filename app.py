# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# 🌿 Shrine Initialization — Tuesday, 14 October 2025, 05:42 AM
# 📍 Location: Blantyre, Malawi
# 🧎🏾‍♂️ Purpose: Activate dynamic shrine, prevent duplicates, robe altar
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# 📜 Import Rituals
from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
import random
import os  # 🌿 For saving audio scrolls

from models import db, Song, Visit  # 👈 Testimony removed for now
from flask_migrate import Migrate

# 🌿 Shrine Setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shrine.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)
app.config['SECRET_KEY'] = 'echo-blessing'

# 🏠 Home Altar — Root route that records visits and robes the altar with latest scroll
@app.route("/")
def index_with_visit():
    name = request.args.get("name", "world")
    visit = Visit(timestamp=datetime.now(), ip_address=request.remote_addr)
    db.session.add(visit)
    db.session.commit()

    # 🎶 Robe the altar with the latest scroll
    latest_song = Song.query.order_by(Song.id.desc()).first()
    song_count = Song.query.count()

    return render_template(
        "index.html",
        name=name,
        title="Dance in Light Shrine",
        latest_song=latest_song,
        song_count=song_count
    )

# 🎶 Praise Scrolls Overview — Dynamic list from the shrine
@app.route("/songs")
def songs():
    all_songs = Song.query.order_by(Song.title.asc()).all()
    return render_template("songs.html", title="Praise Scrolls", songs=all_songs)

# 🧎🏾‍♂️ Submit Offering — Uploads new scrolls and prevents duplicates
@app.route("/submit", methods=["GET", "POST"])
def submit_testimony():
    if request.method == "POST":
        # 🧾 Gather form data from the altar
        title = request.form["title"]
        caption = request.form["caption"]  # 👈 Still collected, but not stored
        bpm = request.form.get("bpm", type=int)
        genre = request.form["genre"]
        language = request.form["language"]
        song_id = request.form["song_id"].lower().replace(" ", "-")
        audio = request.files["audio"]

        # 🛑 Check if song already exists in the shrine
        existing_song = Song.query.get(song_id)
        if existing_song:
            flash("🛑 This song already exists in the shrine. Upload skipped.")
            return redirect(url_for("submit_testimony"))

        # 🎧 Save the audio scroll
        if audio:
            filename = audio.filename.lower()
            music_path = os.path.join("static/music", filename)
            os.makedirs(os.path.dirname(music_path), exist_ok=True)
            audio.save(music_path)

        # 📜 Create the Song scroll
        new_song = Song(
            id=song_id,
            title=title,
            genre=genre,
            bpm=bpm,
            language=language,
            audio_filename=filename
        )
        db.session.add(new_song)
        db.session.commit()

        # 🌟 Bless the user and redirect
        flash("🌿 Scroll received and sealed in the shrine.")
        return redirect(url_for("songs"))

    # 🧎🏾‍♂️ If GET request, show the offering form
    return render_template("submit.html", title="Submit Testimony")

