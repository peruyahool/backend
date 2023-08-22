import sqlite3

# Create or connect to the SQLite database
conn = sqlite3.connect('trains.db')
cursor = conn.cursor()

# Create the train_schedule table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS train_schedule (
        train_id INTEGER PRIMARY KEY,
        departure_time DATETIME,
        seats_available INTEGER,
        price REAL
    )
''')

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Database and table created successfully.")
