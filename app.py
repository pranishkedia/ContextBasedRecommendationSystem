from flask import Flask, render_template, request
from datetime import datetime
from weather_api import get_weather
from weather_recommender import make_recommendation

app = Flask(__name__)

# OpenWeatherMap API key
API_KEY = 'e513208bf4d559b7d650a93d69d4c160'
DEFAULT_LOCATION = 'Newcastle upon Tyne'

@app.route('/')
def home():
    # Home page with just basic instructions and a link to the recommendations page
    return render_template('index.html')

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

if __name__ == '__main__':
    app.run(debug=True)

