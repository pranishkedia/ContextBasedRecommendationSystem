import pandas as pd
import random

# Load music model
def load_songs_data(file_path):
    songs_df = pd.read_csv(file_path)
    songs_data = songs_df.to_dict('records')
    return songs_data

# Load songs data at the start of your application
songs_data = load_songs_data('/Users/pk/ContextBasedRecommendationSystem/music.csv')  


def recommend_music_by_mood(mood, songs_data):
    mood_to_song_filters = {
        'happy': lambda song: float(song['song.tempo']) > 120 and int(song['song.mode']) == 1 and float(song['song.hotttnesss']) > 0.7 and float(song['song.loudness']) > -5,
        'sad': lambda song: float(song['song.tempo']) < 100 and int(song['song.mode']) == 0 and float(song['song.loudness']) < -10 and float(song['song.duration']) > 300,
        'angry': lambda song: float(song['song.tempo']) > 140 and float(song['song.loudness']) > -5,
        'fearful': lambda song: float(song['song.tempo']) < 80 and int(song['song.mode']) == 0 and float(song['song.loudness']) < -10 and float(song['song.duration']) > 300,
        'surprised': lambda song: (float(song['song.tempo']) > 150 or float(song['song.tempo']) < 80) or float(song['song.loudness']) > -5,
        'neutral': lambda song: 90 < float(song['song.tempo']) < 110,
        'disgusted': lambda song: float(song['song.tempo']) < 90 and int(song['song.mode']) == 0 and float(song['song.hotttnesss']) < 0.4
    }
    filter_func = mood_to_song_filters.get(mood.lower(), lambda song: True)  # Ensure mood keys are correctly matched
    filtered_songs = [song for song in songs_data if filter_func(song)]
    random.shuffle(filtered_songs)  # Shuffle to ensure different selections
    top_songs = filtered_songs[:10]  # Select the top 10 after shuffling
    return [song['artist.name'] for song in top_songs]
