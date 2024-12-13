from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    try:
        conn = psycopg2.connect(
            host="db",
            database="flaskdb",
            user="user",
            password="password"
        )
        return conn
    except psycopg2.Error as e:
        print("Erreur de connexion à la base de données", e)
        return None

@app.route("/home")
def home():
    return "Bienvenue sur Flask !"

@app.route("/check-db")
def check_db():
    conn = get_db_connection()
    if conn is None:
        return "Échec de la connexion à la base de données", 500

    try:
        cur = conn.cursor()
        cur.execute("SELECT 'Connexion à la base de données réussie!'")
        message = cur.fetchone()[0]
        cur.close()
        conn.close()
        return message
    except psycopg2.Error as e:
        return f"Erreur lors de l'exécution de la requête: {e}", 500

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
