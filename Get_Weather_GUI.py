import tkinter as tk
import requests

root = tk.Tk()
win = tk.Canvas(root, height=600, width = 600)
win.pack()
def getweather(city):
    API_KEY = "3a2fc642e84cf20a84e5b87ae88e8ed2"
    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"
    request_url = f"{BASE_URL}?q={city}&appid={API_KEY}"
    response = requests.get(request_url)
    if response.status_code == 200:
        format(response)
    else:
        error = "An error occurred while\ntrying the gather data"
        label['text'] = error
def format(response):
    data = response.json()
    weather = data['weather'][0]['description']
    temperature = round(data["main"]["temp"] - 273.15, 2)
    re = "Weather: " + str(weather) + "\nTemperature: " + str(temperature) + "celsius"
    label['text'] = re


background = tk.PhotoImage(file= '2825704.gif')
backgroundlabel = tk.Label(root, image=background)
backgroundlabel.place(relheight=1, relwidth=1)

fram = tk.Frame(root, bg = '#D3D3D3', bd=5)
fram.place(relx=0.5, rely=0.1, relheight=0.1, relwidth=0.75, anchor='n')

input = tk.Entry(fram, font = 50)
input.place(relheight=1, relwidth=0.65)

enter = tk.Button(fram, text="Get Weather", bg = '#2F4F4F', font=40, command=lambda: getweather(input.get()))
enter.place(relx=0.67, rely=0, relwidth=0.32, relheight=1)

lowerfram = tk.Frame(root, bg = '#D3D3D3', bd=5)
lowerfram.place(relx=0.5, rely=0.22, relheight=0.6, relwidth=0.75, anchor='n')

label = tk.Label(lowerfram, font = 40 )
label.place(relheight=1, relwidth=1)

root.mainloop()