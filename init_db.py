import sqlite3

connection = sqlite3.connect('database.db')


""" with open('schema.sql') as f:
    connection.executescript(f.read()) """

cur = connection.cursor()

cur.execute("INSERT INTO tbl_add_user_data (age, gender) VALUES (?, ?)",
            (19, 'male')
            )

cur.execute("INSERT INTO tbl_add_user_data (age, gender) VALUES (?, ?)",
            (18, 'female')
            )

connection.commit()
connection.close()