import json
import requests
from fpdf import FPDF
from flask import Flask, request, render_template

API_KEY = "enter your API key"  # Ensure this is valid
API_HOST = "weatherapi-com.p.rapidapi.com"
API_URL = "https://weatherapi-com.p.rapidapi.com/current.json"

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home5.html')  # Ensure the HTML file name is correct

@app.route('/predict_weather', methods=['POST'])
def predict_weather():
    if request.method == 'POST':
        q = request.form['location']  # Get the location from the form
        url = API_URL
        querystring = {"q": q}
        headers = {
            "X-RapidAPI-Key": API_KEY,
            "X-RapidAPI-Host": API_HOST
        }
        
        try:
            response = requests.get(url, headers=headers, params=querystring)
            print("API Response:", response.text)  # Log the API response for debugging

            # Load the response JSON and extract the data
            json_data = json.loads(response.text)

            # Extract weather data from the API response
            name = json_data['location']['name']
            region = json_data['location']['region']
            country = json_data['location']['country']
            lat = json_data['location']['lat']
            lon = json_data['location']['lon']
            tz_id = json_data['location']['tz_id']
            localtime_epoch = json_data['location']['localtime_epoch']
            localtime = json_data['location']['localtime']
            last_updated_epoch = json_data['current']['last_updated_epoch']
            last_updated = json_data['current']['last_updated']
            temp_c = json_data['current']['temp_c']
            temp_f = json_data['current']['temp_f']
            is_day = json_data['current']['is_day']
            condition_text = json_data['current']['condition']['text']
            condition_icon = json_data['current']['condition']['icon']
            wind_mph = json_data['current']['wind_mph']
            wind_kph = json_data['current']['wind_kph']
            wind_degree = json_data['current']['wind_degree']
            wind_dir = json_data['current']['wind_dir']
            pressure_mb = json_data['current']['pressure_mb']
            pressure_in = json_data['current']['pressure_in']
            precip_mm = json_data['current']['precip_mm']
            precip_in = json_data['current']['precip_in']
            humidity = json_data['current']['humidity']
            cloud = json_data['current']['cloud']
            feelslike_c = json_data['current']['feelslike_c']
            feelslike_f = json_data['current']['feelslike_f']
            vis_km = json_data['current']['vis_km']
            vis_miles = json_data['current']['vis_miles']
            uv = json_data['current']['uv']
            gust_mph = json_data['current']['gust_mph']
            gust_kph = json_data['current']['gust_kph']

            # Render the home template with the weather data
            return render_template('home5.html', name=name, region=region, country=country, lat=lat, lon=lon,
                                   tz_id=tz_id, localtime_epoch=localtime_epoch, localtime=localtime,
                                   last_updated_epoch=last_updated_epoch, last_updated=last_updated, temp_c=temp_c,
                                   temp_f=temp_f, is_day=is_day, condition_text=condition_text,
                                   condition_icon=condition_icon, wind_mph=wind_mph, wind_kph=wind_kph,
                                   wind_degree=wind_degree, wind_dir=wind_dir, pressure_mb=pressure_mb,
                                   pressure_in=pressure_in, precip_mm=precip_mm, precip_in=precip_in,
                                   humidity=humidity, cloud=cloud, feelslike_c=feelslike_c, feelslike_f=feelslike_f,
                                   vis_km=vis_km, vis_miles=vis_miles, uv=uv, gust_mph=gust_mph, gust_kph=gust_kph)

        except Exception as e:
            # Log the exact error for debugging purposes
            print(f"Error: {e}")
            return render_template('home5.html', error='Please enter a correct Place name or check your connection...')

if __name__ == '__main__':
    app.run(debug=True)
