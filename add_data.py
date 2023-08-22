import sqlite3
from datetime import datetime, timedelta

# Create or connect to the SQLite database
conn = sqlite3.connect('trains.db')
cursor = conn.cursor()

# Insert sample data into the train_schedule table
sample_data = [
    (1, '2023-08-23 08:00:00', 100, 50.0),
    (2, '2023-08-23 10:30:00', 75, 65.0),
    (3, '2023-08-23 12:45:00', 50, 80.0),
    (4, '2023-08-23 15:15:00', 30, 100.0),
    (5, '2023-08-23 18:00:00', 90, 45.0),
]

insert_query = '''
    INSERT INTO train_schedule (train_id, departure_time, seats_available, price)
    VALUES (?, ?, ?, ?)
'''

cursor.executemany(insert_query, sample_data)

# Commit the changes and close the connection
conn.commit()
conn.close()

print("Sample data added successfully.")
