import sqlite3

connection = sqlite3.connect('database.db')


with open('schema.sql') as f:
    connection.executescript(f.read())

cur = connection.cursor()

# Clownfish
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

#Carp
fish_id = 1
cur.execute("INSERT INTO colors (id, red, green, blue) VALUES (?, ?, ?, ?)", (fish_id, 196, 194, 195))

cur.execute("INSERT INTO fins (id, length, height) VALUES(?, ?, ?)", (fish_id, 12.3, 10.2))

cur.execute("INSERT INTO fishes (id, name, lifespan, mass, diet_id, length, height, color_id, fin_id) VALUES"
            "(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (fish_id, 'Carp', 20.0, 8.0, 3, 60.0, 15.0, fish_id, fish_id)
            )

cur.execute("INSERT INTO images (id, name, fish_id) VALUES (?, ?, ?)",
            (fish_id, "carpo.png", fish_id))

#Tuna
fish_id = 2
cur.execute("INSERT INTO colors (id, red, green, blue) VALUES (?, ?, ?, ?)", (fish_id, 84, 129, 123))

cur.execute("INSERT INTO fins (id, length, height) VALUES(?, ?, ?)", (fish_id, 70.0, 25.0))

cur.execute("INSERT INTO fishes (id, name, lifespan, mass, diet_id, length, height, color_id, fin_id) VALUES"
            "(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (fish_id, 'Tuna', 30.0, 235.0, 3, 170.0, 45.0, fish_id, fish_id)
            )

cur.execute("INSERT INTO images (id, name, fish_id) VALUES (?, ?, ?)",
            (fish_id, "tuna.png", fish_id))

#Salmon
fish_id = 3
cur.execute("INSERT INTO colors (id, red, green, blue) VALUES (?, ?, ?, ?)", (fish_id, 51, 52, 54))

cur.execute("INSERT INTO fins (id, length, height) VALUES(?, ?, ?)", (fish_id, 10.0, 12.0))

cur.execute("INSERT INTO fishes (id, name, lifespan, mass, diet_id, length, height, color_id, fin_id) VALUES"
            "(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (fish_id, 'Salmon', 5.0, 4.4, 3, 72.5, 12.0, fish_id, fish_id)
            )

cur.execute("INSERT INTO images (id, name, fish_id) VALUES (?, ?, ?)",
            (fish_id, "Salmon.png", fish_id))


#Mackerel
fish_id = 4
cur.execute("INSERT INTO colors (id, red, green, blue) VALUES (?, ?, ?, ?)", (fish_id, 218, 238, 220))

cur.execute("INSERT INTO fins (id, length, height) VALUES(?, ?, ?)", (fish_id, 10.0, 12.0))

cur.execute("INSERT INTO fishes (id, name, lifespan, mass, diet_id, length, height, color_id, fin_id) VALUES"
            "(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (fish_id, 'Mackerel', 17.0, 1.9, 2, 30.0, 5.8, fish_id, fish_id))

cur.execute("INSERT INTO images (id, name, fish_id) VALUES (?, ?, ?)",
            (fish_id, "mackerel.png", fish_id))

#Sardinella
fish_id = 5
cur.execute("INSERT INTO colors (id, red, green, blue) VALUES (?, ?, ?, ?)", (fish_id, 207, 199, 192))

cur.execute("INSERT INTO fins (id, length, height) VALUES(?, ?, ?)", (fish_id, 1.0, 1.1))

cur.execute("INSERT INTO fishes (id, name, lifespan, mass, diet_id, length, height, color_id, fin_id) VALUES"
            "(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (fish_id, 'Sardinella', 2.5, 0.120, 1, 7, 1.2, fish_id, fish_id))

cur.execute("INSERT INTO images (id, name, fish_id) VALUES (?, ?, ?)",
            (fish_id, "sardinella.png", fish_id))

#Picasso triggerfish
fish_id = 6
cur.execute("INSERT INTO colors (id, red, green, blue) VALUES (?, ?, ?, ?)", (fish_id, 106, 106, 54))

cur.execute("INSERT INTO fins (id, length, height) VALUES(?, ?, ?)", (fish_id, 6, 5.5))

cur.execute("INSERT INTO fishes (id, name, lifespan, mass, diet_id, length, height, color_id, fin_id) VALUES"
            "(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (fish_id, 'Picasso Triggerfish', 10, 1.5, 1, 30, 6, fish_id, fish_id))

cur.execute("INSERT INTO images (id, name, fish_id) VALUES (?, ?, ?)",
            (fish_id, "picasso_triggerfish.png", fish_id))

#Swordfish
fish_id = 7
cur.execute("INSERT INTO colors (id, red, green, blue) VALUES (?, ?, ?, ?)", (fish_id, 196, 246, 246))

cur.execute("INSERT INTO fins (id, length, height) VALUES(?, ?, ?)", (fish_id, 20, 35))

cur.execute("INSERT INTO fishes (id, name, lifespan, mass, diet_id, length, height, color_id, fin_id) VALUES"
            "(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (fish_id, 'Swordfish', 9, 59, 2, 274, 30, fish_id, fish_id))

cur.execute("INSERT INTO images (id, name, fish_id) VALUES (?, ?, ?)",
            (fish_id, "swordfish.png", fish_id))

#White Shark
fish_id = 8
cur.execute("INSERT INTO colors (id, red, green, blue) VALUES (?, ?, ?, ?)", (fish_id, 14, 38, 58))

cur.execute("INSERT INTO fins (id, length, height) VALUES(?, ?, ?)", (fish_id, 77, 163))

cur.execute("INSERT INTO fishes (id, name, lifespan, mass, diet_id, length, height, color_id, fin_id) VALUES"
            "(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (fish_id, 'White Shark', 70, 846, 2, 463, 147, fish_id, fish_id))

cur.execute("INSERT INTO images (id, name, fish_id) VALUES (?, ?, ?)",
            (fish_id, "white_shark.png", fish_id))

#Goldfish
fish_id = 9
cur.execute("INSERT INTO colors (id, red, green, blue) VALUES (?, ?, ?, ?)", (fish_id, 244, 157, 58))

cur.execute("INSERT INTO fins (id, length, height) VALUES(?, ?, ?)", (fish_id, 3.5, 4.4))

cur.execute("INSERT INTO fishes (id, name, lifespan, mass, diet_id, length, height, color_id, fin_id) VALUES"
            "(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (fish_id, 'Goldfish', 12, 0.227, 3, 10.16, 4.3, fish_id, fish_id))

cur.execute("INSERT INTO images (id, name, fish_id) VALUES (?, ?, ?)",
            (fish_id, "goldfish.png", fish_id))

#Pufferfish
fish_id = 10
cur.execute("INSERT INTO colors (id, red, green, blue) VALUES (?, ?, ?, ?)", (fish_id, 80, 100, 101))

cur.execute("INSERT INTO fins (id, length, height) VALUES(?, ?, ?)", (fish_id, 3.3, 8.3))

cur.execute("INSERT INTO fishes (id, name, lifespan, mass, diet_id, length, height, color_id, fin_id) VALUES"
            "(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (fish_id, 'Pufferfish', 10, 2.8, 2, 44, 12.2, fish_id, fish_id))

cur.execute("INSERT INTO images (id, name, fish_id) VALUES (?, ?, ?)",
            (fish_id, "pufferfish.png", fish_id))

#Piranha
fish_id = 11
cur.execute("INSERT INTO colors (id, red, green, blue) VALUES (?, ?, ?, ?)", (fish_id, 67, 87, 137))

cur.execute("INSERT INTO fins (id, length, height) VALUES(?, ?, ?)", (fish_id, 8.7, 14.7))

cur.execute("INSERT INTO fishes (id, name, lifespan, mass, diet_id, length, height, color_id, fin_id) VALUES"
            "(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (fish_id, 'Piranha', 7, 2.7, 2, 35, 17.2, fish_id, fish_id))

cur.execute("INSERT INTO images (id, name, fish_id) VALUES (?, ?, ?)",
            (fish_id, "piranha.png", fish_id))

#Anglerfish
fish_id = 12
cur.execute("INSERT INTO colors (id, red, green, blue) VALUES (?, ?, ?, ?)", (fish_id, 97, 46, 9))

cur.execute("INSERT INTO fins (id, length, height) VALUES(?, ?, ?)", (fish_id, 27.8, 54.7))

cur.execute("INSERT INTO fishes (id, name, lifespan, mass, diet_id, length, height, color_id, fin_id) VALUES"
            "(?, ?, ?, ?, ?, ?, ?, ?, ?)",
            (fish_id, 'Anglerfish', 12, 13.1, 2, 100.5, 93.1, fish_id, fish_id))

cur.execute("INSERT INTO images (id, name, fish_id) VALUES (?, ?, ?)",
            (fish_id, "anglerfish.png", fish_id))

connection.commit()
connection.close()
