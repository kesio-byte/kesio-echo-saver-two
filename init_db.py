# ┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
# 🌿 INIT_DB — Shrine Initialization Ritual
# 📍 Purpose: Create shrine.db and seal Song, Testimony, Visit models
# ┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛

from flask import Flask
from models import db, Song, Testimony, Visit

# 🌿 Shrine App Setup
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shrine.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

# 🧎🏾‍♂️ Ritual to Create Tables
with app.app_context():
    db.create_all()
    print("🌟 Shrine database initialized: shrine.db")

