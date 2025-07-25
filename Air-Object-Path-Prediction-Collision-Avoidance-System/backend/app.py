from flask import Flask, request, jsonify
from flask_cors import CORS
from db import get_connection

app = Flask(__name__)
CORS(app)

#  LOGIN
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    print("Received login data:", data)  # Print input from frontend

    try:
        conn = get_connection()
        print(" DB connected")  #Confirmation
    except Exception as e:
        print("DB connection error:", e)
        return jsonify(success=False)

    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s", 
                (data['username'], data['password']))
    result = cur.fetchone()
    cur.close()
    conn.close()

    if result:
        print("Login success for", data['username'])
    else:
        print("Login failed for", data['username'])

    return jsonify(success=bool(result))


# REGISTER
@app.route('/register', methods=['POST'])
def register():
    data = request.json
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute("INSERT INTO users (username, password) VALUES (%s, %s)",
                    (data['username'], data['password']))
        conn.commit()
        cur.close()
        conn.close()
        return jsonify(success=True)
    except Exception as e:
        print("Error:", e)
        return jsonify(success=False)

# CHANGE PASSWORD
@app.route('/change-password', methods=['POST'])
def change_password():
    data = request.json
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE username = %s AND password = %s",
                (data['username'], data['old_password']))
    user = cur.fetchone()
    if not user:
        cur.close()
        conn.close()
        return jsonify(success=False)
    cur.execute("UPDATE users SET password = %s WHERE username = %s",
                (data['new_password'], data['username']))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify(success=True)

@app.route('/api/aircraft')
def get_aircraft_data():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT time, pos_x, pos_y, pos_z FROM aircraft_data")
    rows = cur.fetchall()
    cur.close()
    conn.close()

    return jsonify({
        "time": [r[0] for r in rows],
        "x": [r[1] for r in rows],
        "y": [r[2] for r in rows],
        "z": [r[3] for r in rows]
    })


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)


# Ensure the database connection is established
