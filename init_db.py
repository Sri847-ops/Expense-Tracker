import sqlite3

# Connect or create the database
conn = sqlite3.connect("expenses.db")
c = conn.cursor()

# Create table
c.execute('''CREATE TABLE IF NOT EXISTS expenses (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                amount REAL NOT NULL,
                category TEXT NOT NULL,
                date TEXT NOT NULL
            )''')

conn.commit()
conn.close()

print("Database and table created successfully!")
