import sqlite3

def save_to_db(city, temperature, condition):
    conn = sqlite3.connect("weather.db")
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS history 
                      (city TEXT, temperature REAL, condition TEXT)''')
    cursor.execute("INSERT INTO history VALUES (?, ?, ?)", (city, temperature, condition))
    conn.commit()
    conn.close()
