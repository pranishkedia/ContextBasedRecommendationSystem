from flask import Flask, render_template, request, jsonify
from datetime import datetime
from weather_api import get_weather
from weather_recommender import make_recommendation
import numpy as np
import cv2
import base64
from tensorflow.keras.models import load_model
from mood_recommender import recommend_music_by_mood, songs_data



app = Flask(__name__)

# OpenWeatherMap API key
API_KEY = 'SECRET_KEY'
DEFAULT_LOCATION = 'Newcastle upon Tyne'

@app.route('/')
def home():
    # Home page with just basic instructions and a link to the recommendations page
    return render_template('index.html')


# Weather recommendations
@app.route('/recommendations', methods=['GET', 'POST'])
def recommendations():
    if request.method == 'POST':
        location = request.form['location'] if 'location' in request.form else DEFAULT_LOCATION
    else:
        location = DEFAULT_LOCATION

    weather, temp = get_weather(API_KEY, location)
    current_time = datetime.now().strftime('%H:%M:%S')
    recommendations, part_of_day = make_recommendation(weather, current_time)

    return render_template('recommendations.html', location=location, weather=weather, temp=temp, time=current_time, recommendations=recommendations, part_of_day=part_of_day)



# Mood-based recommendations

# Load the model
model_path = 'final_emotion_model.h5'  # Update this path to where your .h5 file is stored
model = load_model(model_path)

@app.route('/mood')
def mood():
    return render_template('detect_mood.html')

# Define the emotion dictionary
emotion_dict = {0: 'Angry', 1: 'Disgusted', 2: 'Fearful', 3: 'Happy', 4: 'Neutral', 5: 'Sad', 6: 'Surprised'}

@app.route('/process_frame', methods=['POST'])
def process_frame():
    data = request.get_json()
    image_data = data['image']
    encoded_data = image_data.split(',')[1]
    nparr = np.frombuffer(base64.b64decode(encoded_data), np.uint8)
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)

    # Convert to grayscale and process for mood detection
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray_img = cv2.resize(gray_img, (48, 48))
    gray_img = np.expand_dims(gray_img, axis=-1)
    gray_img = np.expand_dims(gray_img, axis=0)
    gray_img = gray_img.astype('float32') / 255

    predictions = model.predict(gray_img)
    max_index = np.argmax(predictions[0])
    mood = emotion_dict[max_index]

    print("Detected Mood:", mood)  # Log the detected mood

    recommended_songs = recommend_music_by_mood(mood, songs_data)

    return jsonify({'emotion': mood, 'songs': recommended_songs})




if __name__ == '__main__':
    app.run(debug=True)

