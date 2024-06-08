# Context-Based Recommendation System

## Overview
The Context-Based Recommendation System leverages contextual information such as user mood and weather conditions to provide personalized recommendations. This project utilizes machine learning models to analyze these contexts and suggest appropriate content, specifically focusing on music recommendations.

## Features
- **Mood Detection**: Uses an emotion model to determine user mood.
- **Weather-Based Recommendations**: Suggests music based on current weather conditions.
- **Integrated API**: Utilizes a weather API to fetch real-time weather data.
- **User Interface**: Provides a simple web interface for users to interact with the system.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/pranishkedia/ContextBasedRecommendationSystem.git
   ```
2. Navigate to the project directory:
   ```bash
   cd ContextBasedRecommendationSystem
   ```
3. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the application:
   ```bash
   python app.py
   ```
2. Open your web browser and go to `http://localhost:5000` to interact with the system.

## Project Structure
- `app.py`: Main application file.
- `mood_recommender.py`: Contains the logic for mood-based recommendations.
- `weather_recommender.py`: Contains the logic for weather-based recommendations.
- `final_emotion_model.h5`: Pre-trained model for emotion detection.
- `static/`: Contains static files (CSS, JavaScript).
- `templates/`: Contains HTML templates.

## Contributing
Contributions are welcome! Please fork the repository and submit a pull request with your changes.

## License
This project is licensed under the MIT License. See the `LICENSE` file for more details.

## Contact
For any questions or suggestions, please open an issue or contact the repository owner at [pranishkedia](https://github.com/pranishkedia).
