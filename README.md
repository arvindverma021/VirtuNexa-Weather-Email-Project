🌦 Weather Application with Email Alerts (Tkinter, SQLite, Logging)

A Python-based Weather App that fetches real-time weather data, stores history in an SQLite database, and sends email alerts for extreme weather conditions.


📌 Features
✅ Fetches real-time weather data from OpenWeatherMap API
✅ Displays weather details in a Tkinter GUI
✅ Stores weather search history in an SQLite database
✅ Sends email alerts for extreme weather conditions (e.g., temperature > 35°C, storms)
✅ Logs searches for debugging and analysis


📂 Project Structure
weather_app/
│── main.py              # Runs the entire application
│── config.py            # Stores API key & email credentials
│── weather_fetch.py     # Fetches weather data from API
│── database.py          # Saves weather data into SQLite
│── alerts.py            # Sends email alerts
│── gui.py               # Tkinter GUI


🔧 Technologies Used
Python (Core logic)
Tkinter (GUI)
SQLite (Data storage)
Requests (Fetching weather data from OpenWeatherMap API)
SMTP (smtplib) (Sending email alerts)
Logging (Recording user searches)


🚀 How It Works
1️⃣ User enters a city name in the GUI.
2️⃣ The app fetches real-time weather data from OpenWeatherMap API.
3️⃣ The data is displayed in the GUI and saved in SQLite.
4️⃣ If the temperature exceeds 35°C or a storm is detected, an email alert is sent.
5️⃣ The application logs all search history for later reference.# VirtuNexa-Weather-Email-Project
