import sqlite3

def init_db():
    conn = sqlite3.connect('data/bookings.db')
    c = conn.cursor()
    c.execute('''
              CREATE TABLE IF NOT EXISTS bookings(
              id INTEGER PRIMARY KEY AUTOINCREMENT,
              name TEXT,
              day TEXT,
              time_slot TEXT
              )
              ''')
    conn.commit()
    conn.close()

def book_slot(name, day, time_slot):
    conn = sqlite3.connect('data/bookings.db')
    c = conn.cursor()
    c.execute("INSERT INTO bookings (name, day, time_slot) VALUES (?, ?, ?)", (name, day, time_slot))
    conn.commit()
    conn.close()

def is_slot_booked(day, time_slot):
    conn = sqlite3.connect('data/bookings.db')
    c = conn.cursor()
    c.execute("SELECT * FROM bookings WHERE day = ? AND time_slot = ?", (day, time_slot))
    booked = c.fetchone()
    conn.close()
    return booked is not None