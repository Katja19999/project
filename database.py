import os
import sqlite3

from constants import Constants


connection = sqlite3.connect(os.path.join(Constants.data_directory, Constants.database_directory, 'results'))
cursor = connection.cursor()
cursor.execute("""
               CREATE TABLE IF NOT EXISTS results (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   result TEXT
               )
               """)

connection.commit()


def get_result(cur=cursor):
    cur.execute("SELECT result FROM results ORDER BY id DESC LIMIT 1")
    result = cursor.fetchone()

    if result:
        return result[0]
    else:
        return None


def write_result(result, con=connection, cur=cursor):
    existing_result = get_result()
    if (existing_result is None) or (int(result) > int(existing_result)):
        cur.execute("INSERT INTO results (result) VALUES (?)", (result, ))
        con.commit()
