from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host="db",
        database="flaskdb",
        user="user",
        password="password"
    )
    return conn

@app.route("/")
def home():
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("SELECT 'Bienvenue sur Flask avec PostgreSQL!'")
    message = cur.fetchone()[0]
    cur.close()
    conn.close()
    return message

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")