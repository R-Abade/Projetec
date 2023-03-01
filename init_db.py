import sqlite3


connection = sqlite3.connect('database.db')
with open('bd.sql') as f:
    connection.executescript(f.read())


cur = connection.cursor()

cur.execute(
    "INSERT INTO users VALUES ('Abade', 'raphaelabade10@gmail.com', '123')")

cur.execute("INSERT INTO users VALUES ('Kevin', 'kevin@gmail.com', '321')")


connection.commit()
connection.close()
