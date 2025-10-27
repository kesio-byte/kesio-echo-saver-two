# 🌿 Echo Saver Shrine — Changelog

> This project is a music distribution shrine for rural artists in Malawi.  
> It helps promote local talent by offering a digital space for praise songs, testimonies, and playback suggestions.

---

## 🔧 Core Python Files

- `app.py` — Main Flask application. Handles routing, form submission, and dynamic rendering of praise verses.
- `models.py` — Defines database models using SQLAlchemy. Structures how praise verses and motifs are stored.
- `echo.db` — SQLite database storing submitted praise verses and emotional metadata.

---

## 🎨 Static Assets

### CSS Robes

- `static/css/main-container.css` — Unified styling for layout containers and responsive playback suggestions.
- `static/main-container.css` — Duplicate or legacy robe; may be merged or removed.
- `static/style.css` — Deprecated robe; removed in favor of unified styling.

### Music Scrolls

- `static/music/idzani.mp3` — Praise song scroll.
- `static/music/lucy.mp3` — Testimony scroll.
- `static/music/rock-of-all-ages.mp3` — Communal resonance scroll.

### Covers & Icons

- `static/covers/default.png.png` — Default cover image for playback.
- `static/favicon.ico.ico` — Shrine icon for browser tab.

---

## 🏛️ Templates (HTML Chambers)

> These templates were removed during layout refinement and may be replaced by dynamic Jinja2 rendering.

- `templates/base.html` — Main layout template (removed).
- `templates/submit.html` — Praise submission form (removed).
- `templates/songs.html` — Playback chamber (removed).
- `templates/testimonies.html` — Testimony display chamber (removed).
- `templates/blessings.html` — Confirmation scroll (removed).
- `templates/testimony.html` — Individual praise verse view (removed).

---

## 🗃️ Other Files

- `README.md` — Project overview and ritual introduction.
- `CHANGELOG.md` — This scroll.
- `requirements.txt` — Python dependencies (removed).
- `metadata.py`, `seed_songs.py`, `init_db.py` — Setup and metadata scripts (removed).
- `Procfile` — Deployment config for Heroku (removed).
- `my web url.txt` — Legacy note (removed).

---

## 🌌 Notes

This changelog reflects the current state of the shrine after layout refinement and GitHub push. All removed files were part of earlier rituals and have been respectfully set aside.

