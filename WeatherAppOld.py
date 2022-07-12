import tkinter as tk
from tkinter import INSERT, Text, font
from PIL import ImageTk, Image
import requests
import datetime


def get_weather(city):
    BASE_URL = "http://api.openweathermap.org/weather/2.5/weather"
    API_KEY = ""
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city.title()}"
    response = requests.get(request_url)
    # params = {"APPID": API_KEY, 'q': city}
    # response = requests.get(BASE_URL, params=params)
    # weather = response.json()

    if response.status_code == 200:
        weather = response.json()
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
    
        # print("City:", city_name)
        # print("Temperature:", temperature, "°C")
        # print("Feels like:", feels_like, "°C")
        # print("Conditions:", conditions)
        # print("Humidity:", humidity, "%")
        # print("Wind:", wind, "m/s")
        # print("Pressure:", pressure, "hPa")
        # print("Sunrise:", sunrise_local)
        # print("Sunset:", sunset_local)

        weather_info = "City: %s \nTemperature: %s °C \nFeels like: %s °C \nConditions: %s \nHumidity: %s % \nWind: %s m/s \nPressure: %s hPa \nSunrise: %s \nSunset: %s" % (city_name, temperature, feels_like, conditions, humidity, wind, pressure, sunrise_local, sunset_local)
        
    else:
        weather_info = "Information could not be retrieved"
        
    # tfield.insert(INSERT, weather_info)

    label["text"] = weather_info

        # info = "City:" + city_name + "\nTemperature:" + temperature + "°C" + "\nFeels like:" + feels_like + "°C" + "\nConditions:" + conditions + "\nHumidity:" + humidity + "%" + "\nWind:" + wind + "m/s" + "\nPressure:" + pressure + "hPa" + "\nSunrise:" + sunrise_local + "\nSunset:" + sunset_local

        # label.config(text= info)

    

        # final_str = "City: %s \nTemperature: %s °C \nFeels like: %s °C \nConditions: %s \nHumidity: %s % \nWind: %s m/s \nPressure: %s hPa \nSunrise: %s \nSunset: %s" % (city_name, temperature, feels_like, conditions, humidity, wind, pressure, sunrise_local, sunset_local)
    # except:
        # final_str = "Something went wrong..."
        # print("Something went wrong...")

    # return final_str
    


root = tk.Tk()
root.title("Weather")

canvas = tk.Canvas(root, height=700, width=800, bg="#99d2e6")
canvas.pack()

frame = tk.Frame(root, bg="#bae8f7", bd=10)
frame.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor="n")

buttonFont = font.Font(family= "Verdana", size=24)
barFont = font.Font(family="Verdana", size=20)
frameFont = font.Font(family="Verdana", size=20)

entry = tk.Entry(frame, font=barFont, bd=0)
entry.place(relheight=1, relwidth=0.65)

button = tk.Button(frame, text="Search", bg="#baf7e8", fg="black", font=buttonFont, bd=0, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relheight=1, relwidth=0.3)

lowerFrame = tk.Frame(root, bg="#bae8f7", bd=10)
lowerFrame.place(relx=0.5, rely=0.25, relheight=0.6, relwidth=0.75, anchor="n")

label = tk.Label(lowerFrame, bg="#fdfde8", font=frameFont, anchor="w", justify="left", bd=10)
label.place(relheight=1, relwidth=1)

# tfield = Text(lowerFrame, bd=15)
# tfield.place(relx=0.5, rely=0.25, relheight=0.6, relwidth=0.75, anchor="n")

root.mainloop()