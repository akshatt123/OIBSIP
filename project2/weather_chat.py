from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox
import requests
from PIL import Image, ImageTk

def get_weather(location):
    try:
        api_key = "99756c6cdb614afcb89a2efb0b42adcd"
        base_url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units={units}"
        response = requests.get(base_url)
        response.raise_for_status()
        data = response.json()

        if data["cod"] != "404":
            main = data["main"]
            condition = data["weather"][0]["main"]
            weather_desc = data["weather"][0]["description"]
            temp = main["temp"]
            pressure = main["pressure"]
            humidity = main["humidity"]
            wind_speed_mps = data["wind"]["speed"]
            
            wind_speed_kmph = wind_speed_mps * 3.6
            fahrenheit = (temp * 9/5) + 32

            if units == "metric":
                temp_feels_like = temp
            else:
                temp_feels_like = fahrenheit

            t.config(text=f"{temp:.2f}°{temp_unit}")
            c.config(text=f"{condition} | Feels like {temp_feels_like:.2f}°{temp_unit}")
            w.config(text=f"{wind_speed_kmph:.1f}Km/h")
            h.config(text=f"{humidity}%")
            d.config(text=weather_desc)
            p.config(text=f"{pressure} hPa")

        else:
            t.config(text="Invalid location. Please try again.")
            h.config(text="")
            w.config(text="")
            d.config(text="")
            p.config(text="")
    except requests.exceptions.HTTPError as e:
        t.config(text=f"Error: {e}")
        h.config(text="")
        w.config(text="")
        d.config(text="")
        p.config(text="")

def toggle_unit():
    global units, temp_unit
    if units == "metric":
        units = "imperial"
        temp_unit = "F"
    else:
        units = "metric"
        temp_unit = "C"
    update_temperature_unit()

def update_temperature_unit():
    location = location_entry.get()
    if location:
        get_weather(location)    

def get_location(event=None):
    location = location_entry.get()
    if location:
        get_weather(location)
    else:
        t.config(text="Error:Please enter a location.")

root = tk.Tk()
root.title("Weather App")
root.geometry("900x500+300+200") 
root.resizable(False, False)


Search_image = ImageTk.PhotoImage(Image.open("project2/Copy_search.png"))
location_image = Label(root ,image=Search_image)
location_image.place(x=20, y=20)

location_entry = tk.Entry(root,justify="center",font=("poppins",25,"bold"), width=20,bg="#404040",border=0,fg="#ffffff")
location_entry.place(x=50, y=40)
location_entry.focus()
location_entry.bind("<Return>", get_location)


Search_icon = ImageTk.PhotoImage(Image.open("project2/Copy_search_icon.png"))
location_icon = Button(root, image=Search_icon, borderwidth=0, cursor="hand2", background="#404040", command=get_location)
location_icon.place(x=400, y=34)

Frame_image = ImageTk.PhotoImage(Image.open("project2/Copy_box.png"))
frame_image = Label(image=Frame_image)
frame_image.pack(padx=5,pady=5,side=BOTTOM)

Label1 = Label(root, text="Wind",font=("Forte",15,"bold"), fg="white", bg="#1ab5ef")
Label1.place(x=120, y=400)
Label2 = Label(root, text="Humidity",font=("Forte",15,"bold"), fg="white", bg="#1ab5ef")
Label2.place(x=250, y=400)
Label3 = Label(root, text="Condition",font=("Forte",15,"bold"), fg="white", bg="#1ab5ef")
Label3.place(x=430, y=400)
Label4 = Label(root, text="Pressure",font=("Forte",15,"bold"), fg="white", bg="#1ab5ef")
Label4.place(x=650, y=400)

t = Label(font=("Forte", 70, "bold"), fg="#ee666d")
t.place(x=400, y=150)
c = Label(font=("Forte", 15))
c.place(x=400, y=250)

w = Label(font=("Forte", 20), background="#1ab5ef")
w.place(x=120, y=430)
h = Label(font=("Forte", 20), background="#1ab5ef")
h.place(x=300, y=430)
d = Label(font=("Forte", 20), background="#1ab5ef")
d.place(x=400, y=430)
p = Label(font=("Forte", 20), background="#1ab5ef")
p.place(x=670, y=430)

toggle_button = Button(root, text="Unit Conversion",font=("Arial", 17),background="#404040", command=toggle_unit)
toggle_button.place(x=700, y=34)

units = "metric"
temp_unit = "C"

root.mainloop()
