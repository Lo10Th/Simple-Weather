from flask import Flask, render_template, request, jsonify
from getweather import weather_data_rain_True
from getcityname import get_city_name

app = Flask(__name__)

latitude = None
longitude = None

def get_weather_for_hours(hours):
    global latitude, longitude

    if request.method == 'POST':
        data = request.get_json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if latitude is None or longitude is None:
            return jsonify({"error": "Location data is missing."})

        city_name = get_city_name(latitude, longitude)
        weather = weather_data_rain_True(city_name, hours)

        return jsonify({"weather": weather, "city_name": city_name})

    if latitude is not None and longitude is not None:
        city_name = get_city_name(float(longitude), float(latitude))
        weather = weather_data_rain_True(city_name, hours)
    else:
        weather = {"message": "No location data available."}
        city_name = "No location data available."

    return render_template('showweather.html', weather=weather)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/1', methods=['POST', 'GET'])
def onehour():
    return get_weather_for_hours(1)

@app.route('/2', methods=['POST', 'GET'])
def twohours():
    return get_weather_for_hours(2)

@app.route('/3', methods=['POST', 'GET'])
def threehours():
    return get_weather_for_hours(3)

@app.route('/4', methods=['POST', 'GET'])
def fourhours():
    return get_weather_for_hours(4)

if __name__ == '__main__':
    app.run(debug=True, port=5500, host='0.0.0.0')
