import sqlite3
con = sqlite3.connect("database/users.db")
cur = con.cursor()


def drop_users_table():
    query = "DROP TABLE IF EXISTS users"
    cur.execute(query)


def create_users_table():
    query = """
        CREATE TABLE IF NOT EXISTS users(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT,
            last_name TEXT,
            gender TEXT,
            age INTEGER
        )
    """
    cur.execute(query)


def seed_users_db():
    drop_users_table()
    create_users_table()
    con.commit()
