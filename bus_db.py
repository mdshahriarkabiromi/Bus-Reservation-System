import sqlite3
from flask import Blueprint, render_template

# Create database if not exists
def create_db():
    with sqlite3.connect("bus_db.db") as conn:
        conn.execute('''CREATE TABLE IF NOT EXISTS seats 
                       (seat_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        seat_number INTEGER,
                        seat_type TEXT,
                        available BOOLEAN DEFAULT 1)''')

# Query to get all seats
def get_all_seats():
    with sqlite3.connect("bus_db.db") as conn:
        rows = conn.execute("SELECT * FROM seats").fetchall()
        return [row[2] for row in rows]

# Query to update seat availability
def update_seat(seat_id, available):
    with sqlite3.connect("bus_db.db") as conn:
        conn.execute("UPDATE seats SET available = ? WHERE id = ?", (available, seat_id))

main = create_db