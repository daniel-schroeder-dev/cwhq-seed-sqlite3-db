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


def seed_db(users):
    query = """
        INSERT INTO users (first_name, last_name, gender, age) 
        VALUES(?, ?, ?, ?);
    """
    for user in users:
        first_name = user["name"]["first"]
        last_name = user["name"]["last"]
        gender = user["gender"]
        age = user["dob"]["age"]
        cur.execute(query, [first_name, last_name, gender, age])


def seed_users_db(users):
    drop_users_table()
    create_users_table()

    seed_db(users)
    
    con.commit()
