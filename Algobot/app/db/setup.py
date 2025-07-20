import sqlite3

conn = sqlite3.connect("conversation_history.db", check_same_thread=False)
cursor = conn.cursor()

def init_db():
    cursor.execute('''CREATE TABLE IF NOT EXISTS history (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        question TEXT,
        explanation TEXT,
        algorithm TEXT,
        quote TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS doubts (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        doubt TEXT,
        answer TEXT
    )''')
    conn.commit()