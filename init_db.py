import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

cur.execute("INSERT INTO diets (id, name) VALUES (?, ?)", (1, "herbivorous"))
cur.execute("INSERT INTO diets (id, name) VALUES (?, ?)", (2, "carnivorous"))
cur.execute("INSERT INTO diets (id, name) VALUES (?, ?)", (3, "omnivorous"))

cur.execute("INSERT INTO colors (id, red, green, blue) VALUES (?, ?, ?, ?)", (0, 255, 0, 0))  # red

cur.execute("INSERT INTO fins (id, length, height) VALUES(?, ?, ?)", (0, 2.0, 2.0))

cur.execute("INSERT INTO fishes (id, name, lifespan, mass, diet_id, length, height, color_id, fin_id) VALUES"
            "(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (0, 'Clownfish', 8.0, 0.25, 3, 10.0, 4.0, 0, 0)
            )

cur.execute("INSERT INTO images (id, name, fish_id) VALUES (?, ?, ?)",
            (0, "clownfish.jpg", 0))

connection.commit()
connection.close()
