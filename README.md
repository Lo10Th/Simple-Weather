Certainly, here's a README in English for your "Simple Weather" project:

---

# Simple Weather

Simple Weather is a Python web application that checks the weather for a given location and provides two outputs: Red or Blue. Blue indicates rain, and Red indicates no rain.

## Table of Contents
- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
- [Usage](#usage)
- [API Keys](#api-keys)
- [Contributing](#contributing)
- [License](#license)

### Prerequisites

Before you start using Simple Weather, make sure you have the following prerequisites in place:

- Python 3.x installed on your system.
- The Flask web framework.
- API keys for the Google Maps API and OpenWeather API.

### Getting Started

1. Clone this repository to your local machine:

   ```
   git clone https://github.com/your-username/simple-weather.git
   ```

2. Change into the project directory:

   ```
   cd simple-weather
   ```

3. Create a virtual environment (recommended) and install the required Python packages:

   ```
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root and add your API keys for Google Maps and OpenWeather as follows:

   ```
   API_KEY=   <--- here your OpenWeather API Key
   google_api_key=    <--- here your Google Maps API Key
   ```

5. Start the Flask web application:

   ```
   python app.py
   ```

6. Open your web browser and navigate to `http://localhost:5500` to use the Simple Weather application.

### Usage

Simple Weather offers weather information for the next four hours. You can access the weather for different timeframes by clicking the corresponding links in the navigation bar.

### API Keys

To use this application, you need to obtain API keys from two sources:

- **OpenWeather API**: Sign up for a free API key at [OpenWeather](https://openweathermap.org/api) and add it to the `.env` file as `API_KEY`.

- **Google Maps API**: You also need a Google Maps API key, which you can obtain by following the instructions [here](https://developers.google.com/maps/gmp-get-started). Add the Google API key to the `.env` file as `google_api_key`.

### Contributing

If you want to contribute to Simple Weather, please follow these steps:

1. Fork the repository on GitHub.
2. Clone your fork to your local machine.
3. Create a new branch for your feature: `git checkout -b feature-name`
4. Make your changes and commit them with descriptive messages.
5. Push your changes to your fork: `git push origin feature-name`
6. Create a pull request on the original repository.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Feel free to customize this README to better suit your project's specific needs.