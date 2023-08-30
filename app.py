from flask import Flask, render_template, request, jsonify
from getweather import weather_data_rain_True
from getcityname import get_city_name

app = Flask(__name__)

latitude = None
longitude = None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/1', methods=['POST', 'GET'])
def onehour():
    global latitude, longitude

    if request.method == 'POST':
        data = request.get_json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if latitude is None or longitude is None:
            return jsonify({"error": "Location data is missing."})

        city_name = get_city_name(latitude, longitude)
        weather = weather_data_rain_True(city_name, 1)

        return jsonify({"weather": weather})
    
    if latitude is not None and longitude is not None:
        city_name = get_city_name(float(longitude), float(latitude))
        weather = weather_data_rain_True(city_name, 1)
    else:
        weather = {"message": "No location data available."}

    return render_template('showweather.html', weather=weather)

@app.route('/2', methods=['POST', 'GET'])
def twohours():
    global latitude, longitude

    if request.method == 'POST':
        data = request.get_json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if latitude is None or longitude is None:
            return jsonify({"error": "Location data is missing."})

        city_name = get_city_name(latitude, longitude)
        weather = weather_data_rain_True(city_name, 2)

        return jsonify({"weather": weather})
    
    if latitude is not None and longitude is not None:
        city_name = get_city_name(float(longitude), float(latitude))
        weather = weather_data_rain_True(city_name, 2)
    else:
        weather = {"message": "No location data available."}

    return render_template('showweather.html', weather=weather)

@app.route('/3', methods=['POST', 'GET'])
def threehours():
    global latitude, longitude

    if request.method == 'POST':
        data = request.get_json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if latitude is None or longitude is None:
            return jsonify({"error": "Location data is missing."})

        city_name = get_city_name(latitude, longitude)
        weather = weather_data_rain_True(city_name, 3)

        return jsonify({"weather": weather})
    
    if latitude is not None and longitude is not None:
        city_name = get_city_name(float(longitude), float(latitude))
        weather = weather_data_rain_True(city_name, 3)
    else:
        weather = {"message": "No location data available."}

    return render_template('showweather.html', weather=weather)

@app.route('/4', methods=['POST', 'GET'])
def fourhours():
    global latitude, longitude

    if request.method == 'POST':
        data = request.get_json()
        latitude = data.get('latitude')
        longitude = data.get('longitude')

        if latitude is None or longitude is None:
            return jsonify({"error": "Location data is missing."})

        city_name = get_city_name(latitude, longitude)
        weather = weather_data_rain_True(city_name, 4)

        return jsonify({"weather": weather})
    
    if latitude is not None and longitude is not None:
        city_name = get_city_name(float(longitude), float(latitude))
        weather = weather_data_rain_True(city_name, 4)
    else:
        weather = {"message": "No location data available."}

    return render_template('showweather.html', weather=weather)


if __name__ == '__main__':
    app.run(debug=True, port=5500, host='0.0.0.0')
