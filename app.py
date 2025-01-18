# from flask import Flask, request, jsonify, render_template
# import requests

# app = Flask(__name__)

# API_KEY = "d60bcfc08bb611c7a05f91aac03105fe"  # Replace with your OpenWeatherMap API key
# BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

# @app.route('/')
# def index():
#     return render_template('index.html')

# @app.route('/get_weather', methods=['POST'])
# def get_weather():
#     city = request.form.get('city')
#     units = request.form.get('units', 'metric')
#     if not city:
#         return jsonify({"error": "City name is required"}), 400

#     response = requests.get(BASE_URL, params={
#         'q': city,
#         'appid': API_KEY,
#         'units': units
#     })
#     data = response.json()

#     if response.status_code == 200:
#         return jsonify(data)
#     else:
#         return jsonify({"error": "City not found"}), 404

# if __name__ == '__main__':
#     app.run(debug=True)

from flask import Flask, request, jsonify, render_template
import requests

app = Flask(__name__)

WEATHER_API_KEY = "d60bcfc08bb611c7a05f91aac03105fe"  # Replace with OpenWeatherMap API key
UNSPLASH_API_KEY = "y8R5QZebPLi5yDCTo1Wtje5q0TW-vtio6eJJ4JpRmtI"       # Replace with Unsplash API key
WEATHER_BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
UNSPLASH_BASE_URL = "https://api.unsplash.com/search/photos"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_weather', methods=['POST'])
def get_weather():
    city = request.form.get('city')
    units = request.form.get('units', 'metric')
    if not city:
        return jsonify({"error": "City name is required"}), 400

    # Fetch weather data
    weather_response = requests.get(WEATHER_BASE_URL, params={
        'q': city,
        'appid': WEATHER_API_KEY,
        'units': units
    })
    weather_data = weather_response.json()

    if weather_response.status_code != 200:
        return jsonify({"error": "City not found"}), 404

    # Fetch city image
    image_response = requests.get(UNSPLASH_BASE_URL, params={
        'query': city,
        'client_id': UNSPLASH_API_KEY,
        'per_page': 1
    })
    image_data = image_response.json()

    if image_data.get("results"):
        image_url = image_data["results"][0]["urls"]["regular"]
    else:
        image_url = None  # Fallback if no image is found

    return jsonify({
        "weather": weather_data,
        "image_url": image_url
    })

if __name__ == '__main__':
    app.run(debug=True)

