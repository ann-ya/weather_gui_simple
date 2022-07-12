import tkinter as tk
from tkinter import font
import requests
import datetime


def get_weather(city):
    url = "http://api.openweathermap.org/weather/2.5/weather"
    key = ""
    request_url = f"{url}?appid={key}&q={city.title()}"
    response = requests.get(request_url)
    weather = response.json()

    label["text"] = format_response(weather)


def format_response(weather):
    try:
        city_name = weather['name']
        temperature = round(weather['main']['temp'] - 273.15, 1)
        feels_like = round(weather['main']['feels_like'] - 273.15, 1)
        conditions = weather['weather'][0]['description']
        humidity = weather['main']['humidity']
        wind = round(weather['wind']['speed'], 2)
        pressure = weather['main']['pressure']
        city_timezone = int(weather['timezone'])
        sunrise_utc = weather['sys']['sunrise']
        sunrise_local = datetime.datetime.utcfromtimestamp(sunrise_utc + city_timezone).strftime("%a %d-%m-%Y %H:%M:%S")
        sunset_utc = weather['sys']['sunset']
        sunset_local = datetime.datetime.utcfromtimestamp(sunset_utc + city_timezone).strftime("%a %d-%m-%Y %H:%M:%S")

        # info = "City: %s \nTemperature: %s °C \nFeels like: %s °C \nConditions: %s \nHumidity: %s % \nWind: %s m/s \nPressure: %s hPa \nSunrise: %s \nSunset: %s" % (city_name, temperature, feels_like, conditions, humidity, wind, pressure, sunrise_local, sunset_local)

        info = f"\nCity: {city_name}\nTemperature: {temperature}°C\nFeels like: {feels_like}°C\nConditions: {conditions}\nHumidity: {humidity}%\nWind: {wind}m/s\nPressure: {pressure}hPa\nSunrise: {sunrise_local}\nSunset: {sunset_local}"
    except:
        info = f"\nInformation could not be retrieved"

    return info


root = tk.Tk()
root.title("Weather")

canvas = tk.Canvas(root, height=700, width=800, bg="#99d2e6")
canvas.pack()

frame = tk.Frame(root, bg="#bae8f7", bd=10)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor="n")

buttonFont = font.Font(family= "Verdana", size=24)
entryFont = font.Font(family="Verdana", size=20)
frameFont = font.Font(family="Verdana", size=20)

entry = tk.Entry(frame, font=entryFont, bd=0)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Search", bg="#baf7e8", fg="black", font=buttonFont, bd=0, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

lowerFrame = tk.Frame(root, bg="#bae8f7", bd=10)
lowerFrame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor="n")

label = tk.Label(lowerFrame, bg="#fdfde8", font=frameFont, anchor="w", justify="left", bd=10)
label.place(relheight=1, relwidth=1)

root.mainloop()