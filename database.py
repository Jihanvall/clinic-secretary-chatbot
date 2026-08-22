import sqlite3

DB_NAME = "clinic.db"

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS appointments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            day TEXT NOT NULL,
            time TEXT NOT NULL,
            patient_name TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_booked_slots():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT day, time FROM appointments")
    rows = cursor.fetchall()
    conn.close()
    return [f"{day} {time}" for day, time in rows]

def add_appointment(day: str, time: str, patient_name: str):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO appointments (day, time, patient_name) VALUES (?, ?, ?)",
        (day, time, patient_name),
    )
    conn.commit()
    conn.close()