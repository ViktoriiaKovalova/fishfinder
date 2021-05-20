import sqlite3
from fish import str2diet, Fish


def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn


def get_all_fishes():
    conn = get_db_connection()
    rows = conn.execute('SELECT fishes.id, fishes.name,lifespan, mass, fishes.length, fishes.height, red, green, blue,'
                        'diets.name as diet,'
                        'fins.height as height_fin, fins.length as length_fin'
                        ' FROM ((fishes JOIN colors ON color_id = colors.id)'
                        'JOIN diets ON diet_id = diets.id)'
                        'JOIN fins ON fin_id = fins.id').fetchall()
    fishes = []
    for row in rows:
        fish = Fish()
        fish.id = row['id']
        fish.name = row['name']
        fish.mass = row['mass']
        fish.diet = str2diet(row['diet'])
        fish.height = row['height']
        fish.length = row['length']
        fish.lifespan = row['lifespan']
        fish.color = (row['red'], row['green'], row['blue'])
        fish.height_fin = row['height_fin']
        fish.length_fin = row['length_fin']
        fishes.append(fish)
    conn.close()
    return fishes


def get_image_for_fish_id(id: int):
    conn = get_db_connection()
    rows = conn.execute('SELECT images.name FROM images WHERE fish_id = (?)', (id,))
    for row in rows:
        return row['name']
    return None
