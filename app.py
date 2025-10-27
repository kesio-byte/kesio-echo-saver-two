# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# 🌿 Shrine Initialization — Saturday, 25 October 2025, 10:32 AM
# 📍 Location: Zomba & Blantyre, Malawi
# 🧎🏾‍♂️ Purpose: Activate dynamic shrine, prevent duplicates, robe altar
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

# 📜 Import Rituals
from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
import random
import os  # 🌿 For saving audio scrolls

from models import db, Song, Visit, Testimony
from flask_migrate import Migrate

# 🌿 Shrine Setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shrine.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'echo-blessing'

db.init_app(app)
migrate = Migrate(app, db)

# 🏠 Home Altar — renders shrine homepage, robes selected scroll if searched
@app.route("/")
def index():
    name = request.args.get("name", "world")
    query = request.args.get("q", "")

    # 🧎🏾‍♂️ Record visit to the shrine
    visit = Visit(timestamp=datetime.now(), ip_address=request.remote_addr)
    db.session.add(visit)
    db.session.commit()

    # 🎶 Robe the altar with the latest scroll
    latest_song = Song.query.order_by(Song.id.desc()).first()
    song_count = Song.query.count()

    # 🔍 If seeker whispered a phrase, robe the first matching scroll
    selected_song = None
    if query:
        selected_song = Song.query.filter(Song.title.contains(query)).first()

    # 🪶 Render the homepage altar with optional scroll
    return render_template(
        "index.html",
        name=name,
        title="Dance in Light Shrine",
        latest_song=latest_song,
        song_count=song_count,
        selected_song=selected_song,
        query=query
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
        # 🧾 Gather form data
        title = request.form["title"]
        caption = request.form["caption"]
        bpm = request.form.get("bpm", type=int)
        genre = request.form["genre"]
        language = request.form["language"]
        song_id = request.form["song_id"].lower().replace(" ", "-")
        audio = request.files["audio"]
        cover = request.files.get("cover")  # 🖼️ Optional cover scroll

        # 🌿 Validate required fields
        if not title or not genre or not language or not song_id or not audio:
            flash("🛑 All required fields must be filled.")
            return redirect(url_for("submit_testimony"))

        # 💓 Validate BPM
        if bpm is not None and bpm <= 0:
            flash("🛑 BPM must be a positive number.")
            return redirect(url_for("submit_testimony"))

        # 🔤 Validate song_id format
        import re
        if not re.match(r'^[a-z0-9\-]+$', song_id):
            flash("🛑 Song ID must use lowercase letters, numbers, and dashes only.")
            return redirect(url_for("submit_testimony"))

        # 🛑 Check for duplicates
        existing_song = Song.query.get(song_id)
        if existing_song:
            flash("🛑 This song already exists in the shrine. Upload skipped.")
            return redirect(url_for("submit_testimony"))

        # 🎧 Save the audio scroll
        filename = audio.filename.lower()
        music_path = os.path.join("static/music", filename)
        os.makedirs(os.path.dirname(music_path), exist_ok=True)
        audio.save(music_path)

        # 🖼️ Save the cover scroll (if provided)
        if cover and cover.filename != "":
            cover_ext = os.path.splitext(cover.filename)[1]
            cover_filename = os.path.splitext(filename)[0] + cover_ext
            cover_path = os.path.join("static/covers", cover_filename)
            os.makedirs(os.path.dirname(cover_path), exist_ok=True)
            cover.save(cover_path)

        # 📜 Create the Song scroll
        new_song = Song(
            id=song_id,
            title=title,
            caption=caption,
            genre=genre,
            bpm=bpm,
            language=language,
            music_file=filename
        )
        db.session.add(new_song)
        db.session.commit()

        # 🌟 Bless the user and redirect
        flash("🌿 Scroll received and sealed in the shrine.")
        return redirect(url_for("songs"))

    # 🧎🏾‍♂️ If GET request, show the offering form
    return render_template("submit.html", title="Submit Testimony")

# 📜 Testimony Chamber — displays all offerings with linked metadata
@app.route("/testimonies")
def testimonies():
    all_testimonies = Testimony.query.order_by(Testimony.timestamp.desc()).all()
    for t in all_testimonies:
        t.metadata = Song.query.filter_by(id=t.song_id).first()
    return render_template("testimonies.html", title="Testimonies", testimonies=all_testimonies)

