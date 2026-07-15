
import tkinter as tk
from tkinter import messagebox
import requests
import datetime
from io import BytesIO
from PIL import Image, ImageTk
from config import API_KEY

root=tk.Tk()
root.title("Advanced Weather App")
root.geometry("560x820")
root.configure(bg="#87CEEB")
root.resizable(False,False)

history=[]
favorites=[]

title=tk.Label(root,text="Advanced Weather App",font=("Segoe UI",20,"bold"),bg="#87CEEB")
title.pack(pady=10)

city_entry=tk.Entry(root,font=("Segoe UI",14),justify="center",width=25)
city_entry.pack()

icon_label=tk.Label(root,bg="#87CEEB")
icon_label.pack()

output=tk.Label(root,text="Enter a city and press Get Weather",justify="left",
                font=("Segoe UI",11),bg="#87CEEB")
output.pack(pady=8)

forecast_box=tk.Text(root,height=8,width=55)
forecast_box.pack(pady=5)

history_box=tk.Listbox(root,height=5,width=55)
history_box.pack(pady=5)

def update_bg(weather):
    colors={"Clear":"#87CEEB","Clouds":"#C8D6E5","Rain":"#95A5A6",
            "Snow":"#EAF6FF","Thunderstorm":"#7F8C8D"}
    c=colors.get(weather,"#87CEEB")
    root.configure(bg=c)
    title.configure(bg=c)
    output.configure(bg=c)
    icon_label.configure(bg=c)

def refresh_history():
    history_box.delete(0,tk.END)
    for h in history[-10:][::-1]:
        history_box.insert(tk.END,h)

def get_weather():
    city=city_entry.get().strip()
    if not city:
        messagebox.showerror("Error","Enter a city.")
        return
    try:
        current=requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric",
            timeout=10).json()
        if str(current.get("cod"))!="200":
            messagebox.showerror("Error",current.get("message","Unknown error"))
            return
        forecast=requests.get(
            f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={API_KEY}&units=metric",
            timeout=10).json()

        w=current["weather"][0]["main"]
        update_bg(w)

        icon=current["weather"][0]["icon"]
        img=requests.get(f"https://openweathermap.org/img/wn/{icon}@2x.png",timeout=10).content
        im=Image.open(BytesIO(img)).resize((90,90))
        photo=ImageTk.PhotoImage(im)
        icon_label.configure(image=photo)
        icon_label.image=photo

        sr=datetime.datetime.fromtimestamp(current["sys"]["sunrise"]).strftime("%I:%M %p")
        ss=datetime.datetime.fromtimestamp(current["sys"]["sunset"]).strftime("%I:%M %p")

        output.config(text=f"""City: {current['name']}, {current['sys']['country']}

Weather: {current['weather'][0]['description'].title()}
Temperature: {current['main']['temp']} °C
Feels Like: {current['main']['feels_like']} °C
Min/Max: {current['main']['temp_min']} / {current['main']['temp_max']} °C
Humidity: {current['main']['humidity']} %
Pressure: {current['main']['pressure']} hPa
Wind: {current['wind']['speed']} m/s
Visibility: {current['visibility']/1000:.1f} km
Sunrise: {sr}
Sunset: {ss}
Updated: {datetime.datetime.now().strftime("%d-%m-%Y %I:%M %p")}
""")

        forecast_box.delete("1.0",tk.END)
        forecast_box.insert(tk.END,"5-Day Forecast\n\n")
        shown=set()
        for item in forecast["list"]:
            if "12:00:00" in item["dt_txt"]:
                d=item["dt_txt"].split()[0]
                if d not in shown:
                    shown.add(d)
                    forecast_box.insert(tk.END,
                        f"{d}  {item['main']['temp']}°C  {item['weather'][0]['main']}\n")

        history.append(city.title())
        refresh_history()

    except Exception as e:
        messagebox.showerror("Error",str(e))

def refresh():
    if city_entry.get().strip():
        get_weather()

def add_favorite():
    c=city_entry.get().strip().title()
    if c and c not in favorites:
        favorites.append(c)
        messagebox.showinfo("Favourite",f"{c} added to favourites.")

btn_frame=tk.Frame(root,bg="#87CEEB")
btn_frame.pack(pady=5)

tk.Button(btn_frame,text="Get Weather",command=get_weather,width=14,bg="#1E90FF",fg="white").grid(row=0,column=0,padx=5)
tk.Button(btn_frame,text="Refresh",command=refresh,width=10).grid(row=0,column=1,padx=5)
tk.Button(btn_frame,text="Add Favourite",command=add_favorite,width=14).grid(row=0,column=2,padx=5)

city_entry.bind("<Return>",lambda e:get_weather())

tk.Label(root,text="Recent Searches",bg="#87CEEB",font=("Segoe UI",10,"bold")).pack()

root.mainloop()
