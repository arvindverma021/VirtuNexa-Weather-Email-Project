import tkinter as tk
from tkinter import messagebox
from weather_fetch import get_weather
from database import save_to_db
from alerts import send_alert


def fetch_weather():
    city = city_entry.get()
    weather = get_weather(city)

    if weather:
        save_to_db(weather["city"], weather["temperature"], weather["condition"])

        # Send email if temperature > 35°C or condition contains "storm"
        if weather["temperature"] > 35 or "storm" in weather["condition"].lower():
            send_alert("recipient_email@example.com", weather["city"], weather["temperature"], weather["condition"])

        result_label.config(text=f"{weather['city']}\nTemp: {weather['temperature']}°C\n{weather['condition']}")
    else:
        messagebox.showerror("Error", "City not found!")


def run_app():
    global city_entry, result_label

    root = tk.Tk()
    root.title("Weather App")

    tk.Label(root, text="Enter City:").pack()
    city_entry = tk.Entry(root)
    city_entry.pack()

    tk.Button(root, text="Get Weather", command=fetch_weather).pack()
    result_label = tk.Label(root, text="")
    result_label.pack()

    root.mainloop()
