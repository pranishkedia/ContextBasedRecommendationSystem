import pandas as pd
import numpy as np
from datetime import datetime

# Load music data
music_data = pd.read_csv('music.csv')

def classify_songs():
    # Classify songs as 'Calm' or 'Upbeat' based on tempo and genre
    conditions = [
        (music_data['song.tempo'] < 100) | (music_data['artist.terms'].str.contains('classical|jazz|ambient|soul|chill-out|blues|easy listening|bosa nova')),
        (music_data['song.tempo'] >= 100) | (music_data['artist.terms'].str.contains('rock|pop|hip hop|electronic|metal|disco|pop rap'))
    ]
    choices = ['Calm', 'Upbeat']
    music_data['Mood'] = np.select(conditions, choices, default='Moderate')
    return music_data

music_data = classify_songs()

def make_recommendation(weather, current_time):
    # Determine part of the day (morning or evening)
    hour = datetime.strptime(current_time, '%H:%M:%S').hour
    part_of_day = 'Morning' if 6 <= hour < 12 else 'Evening'

    # Recommend based on weather and part of the day
    if part_of_day == 'Morning' and 'Sunny' in weather:
        mood = 'Upbeat'
    elif part_of_day == 'Morning' and 'Clouds' in weather:
        mood = 'Upbeat'
    elif part_of_day == 'Morning' and 'Clear' in weather:
        mood = 'Upbeat'
    elif part_of_day == 'Morning' and 'Rain' in weather:
        mood = 'Calm'
    
    elif part_of_day == 'Evening' and 'Sunny' in weather:
        mood = 'Upbeat'
    elif part_of_day == 'Evening' and 'Clear' in weather:
        mood = 'Upbeat'
    elif part_of_day == 'Evening' and 'Rain' in weather:
        mood = 'Calm'
    elif part_of_day == 'Evening' and 'Clouds' in weather:
        mood = 'Calm'
    else:
        mood = 'Calm'  # Default mood for other conditions

    filtered_artists = music_data[music_data['Mood'] == mood]['artist.name']
    recommended_artists = filtered_artists.head(10).tolist()  # Take only the first 10 artists

    return recommended_artists, part_of_day