import sqlite3

def create_database():
    conn = sqlite3.connect('diseases.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS diseases
              (user_id INTEGER, name TEXT, vector TEXT, differential diagnoses TEXT
              symptoms TEXT, treatments TEXT)''')
    conn.commit()
    conn.close()

create_database()