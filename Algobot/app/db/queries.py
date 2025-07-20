from .setup import cursor, conn

def save_history(question, explanation, algorithm, quote):
    cursor.execute("INSERT INTO history (question, explanation, algorithm, quote) VALUES (?, ?, ?, ?)",
                   (question, explanation, algorithm, quote))
    conn.commit()

def fetch_all_history():
    cursor.execute("SELECT * FROM history ORDER BY id DESC")
    return cursor.fetchall()

def delete_all_history():
    cursor.execute("DELETE FROM history")
    conn.commit()

def save_doubt(doubt, answer):
    cursor.execute("INSERT INTO doubts (doubt, answer) VALUES (?, ?)", (doubt, answer))
    conn.commit()

def fetch_all_doubts():
    cursor.execute("SELECT * FROM doubts ORDER BY id DESC")
    return cursor.fetchall()

def delete_all_doubts():
    cursor.execute("DELETE FROM doubts")
    conn.commit()