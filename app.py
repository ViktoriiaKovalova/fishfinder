from flask import Flask, render_template, request, flash
from db import get_all_fishes
from fish import Fish, str2diet
from fish import Diet

app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='djdfskfjlsfjdlfjslev')

default_color = '000000'


def create_fish_from_values(lifespan, mass, diet, length, height, color, length_fin, height_fin):
    fish = Fish()
    if lifespan:
        fish.lifespan = float(lifespan)
    if mass:
        fish.mass = float(mass)
    if diet != 'not chosen':
        fish.diet = str2diet(diet)
    if length:
        fish.length = float(length)
    if height:
        fish.height = float(height)
    if color != default_color:
        rgb = tuple([int('0x' + color[2*i + 1: 2*i + 2], 16) for i in range(3)])
        fish.color = rgb
    if length_fin:
        fish.length_fin = float(length_fin)
    if height_fin:
        fish.height_fin = float(height_fin)
    return fish


def calculate_relative_difference(a: float, b: float) -> float:
    return abs(a - b) / min(a, b)


def calculate_similarity(fish, db_fish) -> float:
    score = 0.0
    if fish.lifespan is not None:
        score -= calculate_relative_difference(fish.lifespan, db_fish.lifespan)
    if fish.mass is not None:
        score -= calculate_relative_difference(fish.mass, db_fish.mass)
    if fish.color is not None:
        for i in range(3):
            score -= abs(fish.color[i] - db_fish.color[i]) / 64
    if fish.length is not None:
        score -= calculate_relative_difference(fish.length, db_fish.length)
    if fish.height is not None:
        score -= calculate_relative_difference(fish.height, db_fish.height)
    if fish.diet is not None:
        score += 3 * (fish.diet == db_fish.diet)
    if fish.length_fin is not None:
        score -= calculate_relative_difference(fish.length_fin, db_fish.length_fin)
    if fish.height_fin is not None:
        score -= calculate_relative_difference(fish.height_fin, db_fish.height_fin)
    return score


def get_the_closest_fish_from_db(fish):
    fishes = get_all_fishes()
    best_fish = max(fishes, key=lambda x: calculate_similarity(fish, x))
    return best_fish


@app.route('/', methods=('GET', 'POST'))
def index():
    if request.method == "POST":
        lifespan = request.form['lifespan']
        mass = request.form['mass']
        diet = request.form['diet_select']
        length = request.form['length']
        height = request.form['height']
        color = request.form['color']
        length_fin = request.form['length_fin']
        height_fin = request.form['height_fin']
        filled_values = 0
        for val in [lifespan, mass, length, height, length_fin, height_fin]:
            if val:
                filled_values += 1
        filled_values += (color != default_color) + (diet != 'not chosen')
        if filled_values < 3:
            flash('Too few values entered, the results might be incorrect')
        fish = create_fish_from_values(lifespan, mass, diet, length, height, color, length_fin, height_fin)
        result = get_the_closest_fish_from_db(fish)
        message = f"Your fish is {result.name}!"
        results = [message]
    else:
        results = []
    return render_template('index.html',
                           diet_values=['not chosen', 'carnivorous', 'herbivorous', 'omnivorous'],
                           fish_pic="clownclownfish.jpg",
                           num_colors=1,
                           results=results)


if __name__ == '__main__':
    app.run()
