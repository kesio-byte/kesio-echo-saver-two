CS50x Final Project
Authored by Kesio Mtewa
📍 Neno, Malawi
🕊️30 October 2025


# 🌿 Dance in Light Shrine

A poetic Flask web shrine created by **Kesio Mtewa** in **Blantyre, Malawi**, as a final offering for CS50x. This project blends gospel testimony, musical metadata, and emotional affirmation into a living manuscript. Each route is a ritual, each scroll a robe, and each interaction a breath of light.

---

## 🧎🏾‍♂️ Project Overview

**Dance in Light Shrine** is a web application built with Flask that:

- Hosts a personalized homepage with poetic greeting and musical download
- Displays a curated list of gospel songs with genre and BPM
- Offers dynamic song detail pages with metadata, cover art, and Suno links
- Accepts user-submitted testimonies and seals them in confirmation scrolls
- Shares blessings and joy echoes inspired by family affirmation
- Integrates a relational database to store songs and testimonies

---

## 🗃️ Technologies Used

- **Flask** — Web framework for routing and rendering
- **HTML/CSS/Bootstrap** — Frontend styling and layout
- **SQLAlchemy** — ORM for database integration
- **Render** — Cloud deployment platform
- **Python 3.13.4** — Core programming language

---

## 📁 Folder Structure

kesio-echo-saver/ ├── app.py                  # Main Flask scroll ├── models.py               # Database models for Song and Testimony ├── requirements.txt        # Dependencies ├── Procfile                # Render start command ├── templates/              # HTML scrolls │   ├── index.html │   ├── songs.html │   ├── song_detail.html │   ├── nicetu.html │   ├── blessings.html │   ├── testimony.html │   └── shrine_sealed.html ├── static/                 # Visual robes and assets │   ├── style.css │   ├── echo_saver.ico │   └── casio.pdf ├── static/covers/          # Cover art for each song ├── music/                  # Audio scrolls (optional)


---

## 🌟 Features

- 🏠 **Home Altar** — Personalized greeting and musical file
- 🎶 **Praise Scrolls** — Song list with genre and BPM
- 🪨 **Individual Song Shrine** — Full metadata and cover art
- 📜 **Testimony Altar** — Form to submit musical metadata
- 🌟 **Blessings Scroll** — GET-only affirmation
- 👧🏾 **Joy Echo** — Timestamped blessings inspired by daughter’s voice
- 🗃️ **Database Integration** — Songs and testimonies stored dynamically

---

## 🗃️ Database Models

- `Song` — Stores title, genre, bpm, language, theme, cover metadata, and Suno link
- `Testimony` — Stores user-submitted metadata and timestamp

---

## 🚀 Deployment

- Hosted on [Render](https://render.com)
- Live at: [https://kesio-echo-saver.onrender.com](https://kesio-echo-saver.onrender.com)
- Start command: `gunicorn app:app`

---

## 🧎🏾‍♂️ Acknowledgments

- 🙏🏾 **CS50x Team** — For the course, the challenge, and the global community
- 👨‍👦 **Steve, my son and companion** — For walking with me through every scroll, every bug, and every breakthrough
- 🧠 **Microsoft Copilot** — For poetic guidance, technical clarity, and gentle companionship throughout the shrine’s creation
- 👧🏾 **Daughter’s Voice** — For the affirmation that became `/nicetu`
- 🪔 **Family Lineage** — For the rhythms, memories, and spiritual grounding woven into every scroll
- 🎓 **Professor David J. Malan** — Gordon McKay Professor of Computer Science at Harvard University, creator of CS50, and a global teacher whose lectures have reached millions. His work in computer science education, botnet detection, and open learning has inspired learners across the world.

---

## 💬 Closing Blessing

> “Each scroll is a robe,  
> Each robe is a rhythm,  
> Each rhythm is a testimony—  
> And the shrine stands sealed in light.”


