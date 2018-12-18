from flask import Flask, render_template, jsonify
import requests
from app.otaku import Otaku


app = Flask(__name__, template_folder='views')
base_url = "https://api.jikan.moe/v3"


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/random/<string:type>")
def random_media(type):
    media = Otaku(type)
    response = requests.get(base_url+media.get_random_media())
    if response.status_code == 200:
        return render_template('random.html', data=response.json())
    else:
        return random_media(type)


@app.route("/search/<string:type>/<title>")
def search_media(title, type):
    media = Otaku(type)
    response = requests.get(base_url+media.get_media_by_title(title))
    return jsonify(response.json())


@app.route("/season/<string:season>/<string:year>")
def get_anime_by_season(season, year):
    response = requests.get(base_url + Otaku.get_anime_by_season(year, season))
    return jsonify(response.json())


@app.route("/<string:type>/genre/<genre>")
def get_media_by_genre(genre, type):
    media = Otaku(type)
    response = requests.get(base_url+media.get_media_by_genre(genre))
    return jsonify(response.json())


if __name__ == '__main__':
    app.run(port=3000, debug=True)
