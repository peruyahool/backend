from flask import Flask, jsonify
import sqlite3
import datetime

app = Flask(__name__)

@app.route('/trains', methods=['GET'])
def get_trains():
    now = datetime.datetime.now()
    end_time = now + datetime.timedelta(hours=12)

    conn = sqlite3.connect('trains.db')
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT train_id, departure_time, seats_available, price
        FROM train_schedule
        WHERE departure_time BETWEEN ? AND ?
        """,
        (now, end_time),
    )

    trains = []
    for row in cursor.fetchall():
        train = {
            'train_id': row[0],
            'departure_time': row[1],
            'seats_available': row[2],
            'price': row[3],
        }
        trains.append(train)

    conn.close()

    return jsonify(trains)

if __name__ == '__main__':
    app.run(debug=True)
