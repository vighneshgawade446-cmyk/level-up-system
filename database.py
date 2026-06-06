import sqlite3
DB_NAME = "/app/levelup.db"
def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        user_id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        height REAL,
        weight REAL,
        rank TEXT,
        level INTEGER,
        gold INTEGER
    )
    """)
    conn.commit()
    conn.close()
def create_user(user_id, name, age, height, weight):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    INSERT OR REPLACE INTO users
    (user_id, name, age, height, weight, rank, level, gold)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """,
    (user_id, name, age, height, weight, "E", 1, 0))
    conn.commit()
    conn.close()
def get_user(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT * FROM users WHERE user_id=?",
        (user_id,)
    )
    user = cursor.fetchone()
    conn.close()
    return user
