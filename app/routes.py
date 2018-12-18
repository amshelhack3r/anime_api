from flask import  Flask, render_template, jsonify
import requests
from app.otaku import Otaku
import json as myjson

app = Flask(__name__, template_folder='views')
base_url = "https://api.jikan.moe/v3"
manga = Otaku("manga")
anime = Otaku("anime")

@app.route("/")
def main():
    return render_template("index.html")

@app.route("/anime/random")
def random_anime():
    response = requests.get(base_url+anime.get_random_media())
    if response.status_code == 200:
        return render_template('random.html', data = response.json())
    else:
        return random_anime()


@app.route("/manga/random")
def random_manga():
    response = requests.get(base_url+manga.get_random_media())
    if response.status_code == 200:
        print(response.json())
        return render_template('random.html', data = response.json())
    else:
        return random_manga()


@app.route("/anime/<title>")
def search_anime(title):
    print(base_url+anime.get_media_by_title(title))
    response = requests.get(base_url+anime.get_media_by_title(title))
    return jsonify(response.json())


@app.route("/manga/<title>")
def search_manga(title):
    response = requests.get(base_url+manga.get_media_by_title(title))
    return jsonify(response.json())


@app.route("/season/<season>/<year>")
def get_anime_by_season(season, year):
    response = requests.get(base_url + Otaku.get_anime_by_season(year, season))
    return jsonify(response.json())

@app.route("/anime/genre/<genre>")
def get_anime_by_genre(genre):
    response = requests.get(base_url+anime.get_media_by_genre(genre))
    return jsonify(response.json())


@app.route("/manga/genre/<genre>")
def get_manga_by_genre(genre):
    response = requests.get(base_url+manga.get_media_by_genre(genre))
    return jsonify(response.json())

if __name__ == '__main__':
    app.run(port=3000, debug=True)
