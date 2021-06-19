import tkinter as tk
import requests

# 03c0a91b84dfa72076acb159618dce8b
# api.openweathermap.org/data/2.5/forecast?q={city name}&appid={API key}

def test_function(en):
    print("It Works!! ", en)

def format_out(condition):
    try:
        name = condition['name']
        weather = condition['weather'][0]['description']
        temp_max = condition['main']['temp_max']
        temp_min = condition['main']['temp_min']

        final_str = str('City: %s\nWeather: %s\nMax Temperature (°C): %s\nMin Temperature (°C): %s' % (name, weather, temp_max, temp_min))
    except:
        final_str = str('There was some error retrieving\n the information.')

    return final_str

def get_weather(city):
    weather_key = '03c0a91b84dfa72076acb159618dce8b'
    url = 'https://api.openweathermap.org/data/2.5/weather'
    params = {'APPID': weather_key, 'q': city, 'units': 'metric'}
    response = requests.get(url, params=params)
    condition = response.json()
    print(condition)

    label['text'] = format_out(condition)

root = tk.Tk()

canvas = tk.Canvas(root, height=500, width=600)
canvas.pack()

bg_image = tk.PhotoImage(file='img.png')
bg_label = tk.Label(root, image=bg_image)
bg_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#cf8b7a', bd=5)
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.15)

entry = tk.Entry(frame, font=('Lucida Fax', 20), bd=1)
entry.place(relwidth=0.6, relheight=1)

button = tk.Button(frame, text="Get Weather", bg='#b5cf63', font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.65, relwidth=0.35, relheight=1)

frame2 = tk.Frame(root, bg='#cf8b7a', bd=10)
frame2.place(relx=0.1, rely=0.35, relwidth=0.8, relheight=0.5)

entry2 = tk.Entry(frame2, font=50, bd=7)
entry2.place(relx=0.05, rely=0.1, relwidth=0.9, relheight=0.8)

label = tk.Label(frame2, bg='white', font=('Courier', 18))
label.place(relwidth=1, relheight=1)

root.mainloop()