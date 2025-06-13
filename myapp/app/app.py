from flask import Flask
import psycopg2
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Подключение к базе
    conn = psycopg2.connect(
        host=os.getenv('DB_HOST'),
        database=os.getenv('DB_NAME'),
        user=os.getenv('DB_USER'),
        password=os.getenv('DB_PASSWORD')
    )
    cur = conn.cursor()
    cur.execute('SELECT version()')
    db_version = cur.fetchone()
    cur.close()
    conn.close()
    
    return f'Connected to PostgreSQL: {db_version[0]}'

if __name__ == '__main__':
    app.run(host='0.0.0.0')
