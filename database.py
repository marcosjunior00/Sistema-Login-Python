import sqlite3

conn = sqlite3.connect("UserData.db")

cursor = conn.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Users (
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR(50) NOT NULL,
        email VARCHAR(40) NOT NULL,
        user VARCHAR(30) NOT NULL,
        pass VARCHAR(30) NOT NULL
    );
""")

print("Conected to DataBase")