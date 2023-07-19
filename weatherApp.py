import tkinter as tk
import requests
from bs4 import BeautifulSoup

def fetch_weather_data():
    location = location_entry.get()
    #url = f'"https://www.google.com/search?q="+"weather"+{location}'
    url = "https://www.google.com/search?q=weather+" + city
    try:
        response = requests.get(url)
        locations = response.json()

        if not locations:
            error_label.config(text='Location not found.')
            return

        woeid = locations[0]['woeid']
        weather_url = f'https://www.metaweather.com/api/location/{woeid}/'
        weather_response = requests.get(weather_url)
        weather_data = weather_response.json()

        # Parse the weather data and update the display labels
        consolidated_weather = weather_data['consolidated_weather'][0]
        temperature_label.config(text=f'Temperature: {consolidated_weather["the_temp"]} °C')
        humidity_label.config(text=f'Humidity: {consolidated_weather["humidity"]}%')
        wind_speed_label.config(text=f'Wind Speed: {consolidated_weather["wind_speed"]} m/s')
        weather_condition_label.config(text=f'Weather Condition: {consolidated_weather["weather_state_name"]}')

        error_label.config(text='')

    except requests.exceptions.RequestException:
        error_label.config(text='Error fetching data. Please check your internet connection.')

# Create the tkinter application
app = tk.Tk()
app.title('Weather App')
app.geometry('400x300')

# Create widgets
location_entry = tk.Entry(app, width=30)
location_entry.pack(pady=10)

fetch_button = tk.Button(app, text='Fetch Weather', command=fetch_weather_data)
fetch_button.pack()

temperature_label = tk.Label(app, text='Temperature: ')
temperature_label.pack(pady=5)

humidity_label = tk.Label(app, text='Humidity: ')
humidity_label.pack(pady=5)

wind_speed_label = tk.Label(app, text='Wind Speed: ')
wind_speed_label.pack(pady=5)

weather_condition_label = tk.Label(app, text='Weather Condition: ')
weather_condition_label.pack(pady=5)

error_label = tk.Label(app, fg='red')
error_label.pack(pady=5)

app.mainloop()
