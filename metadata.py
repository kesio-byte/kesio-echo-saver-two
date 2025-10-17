# 📖 Song Metadata Archive — Dictionary of poetic metadata for each song
def get_song_by_id(song_id):
    songs = {
        "dance-in-light": {
            "title": "Dance in Light",
            "subtitle": "A gospel anthem of joy and deliverance",
            "authors": "Kesiomtewa",
            "genre": "Gospel Anthem",
            "bpm": 92,
            "language": "Chichewa & English",
            "theme": "Spiritual transformation, communal joy, radiant praise",
            "cover_caption": "From ache to joy, sealed in light",
            "cover_style": "Golden rays, dancing silhouettes, glowing altar",
            "suno_link": "https://suno.com"
        },
        "imbirani-yahve": {
            "title": "Imbirani Yahve",
            "subtitle": "Sing to Yahweh with joy",
            "authors": "Kesiomtewa & Neno Choir",
            "genre": "Gospel Praise",
            "bpm": 96,
            "language": "Chichewa",
            "theme": "Joyful worship, sacred rhythm, communal praise",
            "cover_caption": "Voices rise in praise to Yahweh",
            "cover_style": "Village choir, radiant sky, joyful silhouettes",
            "suno_link": "https://suno.com"
        },
        "khalani": {
            "title": "Khalani",
            "subtitle": "Remain in grace, walk in light",
            "authors": "Kesiomtewa",
            "genre": "Gospel Ballad",
            "bpm": 84,
            "language": "Chichewa",
            "theme": "Spiritual stillness, emotional grounding, sacred presence",
            "cover_caption": "Remain in grace, walk in light",
            "cover_style": "Still waters, glowing path, soft robes",
            "suno_link": "https://suno.com"
        }
    }
    return songs.get(song_id, {"title": "Unknown Song"})

