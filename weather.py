import requests
import datetime as dt
import tkinter
from PIL import Image, ImageTk
window = tkinter.Tk()
window.minsize(height="400",width="400")
window.title("Weather App")
COLOR = "#80C4E9"


api_key= "?" # Insert your own Open Weather api key

def info(city):
  COLOR = "white"
  URL = f"https://api.openweathermap.org/data/2.5/weather?appid={api_key}&q={city}&units=metric"
  data = requests.get(URL).json()
  
  img = data["weather"][0]["icon"]
  if "n" in img:
    COLOR = "gray"
  else: 
    COLOR = "#80C4E9"
  image_url = f"https://openweathermap.org/img/wn/{img}@2x.png"
  weather_description = str(data["weather"][0]["description"]).upper()
  temperature = round(data["main"]["temp"],2)
  wind_speed = round(data["wind"]["speed"]*3.6,2)
  return image_url, weather_description, temperature, city, wind_speed, COLOR


image_url, weather_description, temperature, city, wind_speed, COLOR = info("Delhi")
window.config(padx=20,pady=20,background=COLOR)

weather_label = tkinter.Label(text=city.upper(),font=("Arial",24),pady=20,background=COLOR,highlightthickness=0, fg = "white")
weather_label.grid(row=0,column=1,padx=10)


icon = Image.open(requests.get(image_url,stream=True).raw)
icon.resize((200,200))
icon.crop((0,40,100,160))
image = ImageTk.PhotoImage(icon)
canvas = tkinter.Canvas(width=200,height=200,background=COLOR,highlightthickness=0)
canvas.create_image(100,100,image = image)
canvas.grid(row=1,column=1,padx=10)


weather = tkinter.Label(text=weather_description,font=("Arial",24),foreground="blue",background=COLOR, fg = "white")
weather.grid(row=2,column=1,padx=5,)

temp = tkinter.Label(text=f"Temp: {temperature}",font=("Arial",20),foreground="white",background=COLOR, fg = "white")
temp.grid(row=3,column=0,pady=20)

wind = tkinter.Label(text=f"Wind Speed: {wind_speed}",font=("Arial",20),foreground="white",background=COLOR, fg="white")
wind.grid(row=3,column=2,pady=20)

weather_city = tkinter.Entry(width=30,justify="center",font=("Arial",20),relief="flat")
weather_city.grid(row=4,column=0,columnspan=2,padx=10,pady=10)

def weather_changer():
    global canvas, icon, image
    icon.close()
    canvas.delete('all')
    City = weather_city.get()
    global image_url, weather_description, temperature, city, wind_speed
    image_url, weather_description, temperature, city, wind_speed, COLOR=info(City)
    window.config(padx=20,pady=20,background=COLOR)
    weather_label["text"]= city.upper()
    weather_label["bg"] = COLOR
    weather_city.delete(-1,len(weather_city.get()))
    
    icon = Image.open(requests.get(image_url,stream=True).raw)
    icon.resize((200,200))
    icon.crop((0,40,100,160))
    image = ImageTk.PhotoImage(icon)
    canvas.create_image(100,100,image = image)
    canvas.grid(row=1,column=1,padx=10)
    canvas["background"]=COLOR
    
    weather["text"]= weather_description
    weather["background"] = COLOR
    temp["text"] = f"Temp: {temperature}"
    temp["background"] = COLOR
    wind["text"] = f"Wind Speed: {wind_speed}"
    wind["background"] = COLOR
weather_button = tkinter.Button(text="Search",command=weather_changer,relief="flat",font=("Arial",14),background="white")
weather_button.grid(row=4,column=2,pady=10)

window.mainloop()