from flask import Flask, render_template, jsonify, make_response
from flask_restful import Resource, Api
import requests
from app.otaku import Otaku

app = Flask(__name__, template_folder='views')
# initialize flask restful
api = Api(app)

# get our models
base_url = "https://api.jikan.moe/v3"


class Default(Resource):
    def get(self):
        return make_response(render_template('index.html'),200)


class SearchMedia(Resource):
    def get(self, title, type):
        media = Otaku(type)
        response = requests.get(base_url+media.get_media_by_title(title))
        return jsonify(response.json())


class RandomMedia(Resource):
    def get(self, type):
        media = Otaku(type)
        response = requests.get(base_url+media.get_random_media())
        if(response.status_code == 200):
            return make_response(render_template('random.html', data=response.json()),200)
        else:
            return self.get(type)


class Season(Resource):
    def get(self, year, season):
        response = requests.get(base_url + Otaku.get_anime_by_season(year, season))
        return jsonify(response.json())


class MediaGenre(Resource):
    def get(self, type, genre):
        media = Otaku(type)
        response = requests.get(base_url+media.get_media_by_genre(genre))
        return jsonify(response.json())


# add endpoints to resources
api.add_resource(Default, '/')
api.add_resource(SearchMedia, '/<string:type>/<string:title>')
api.add_resource(RandomMedia, '/random/<string:type>')
api.add_resource(Season, '/season/<string:year>/<string:season>')
api.add_resource(MediaGenre, '/<string:type>/genre/<string:genre>')


if __name__ == '__main__':
    app.run(port=3000, debug=True)
