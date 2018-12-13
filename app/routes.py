from flask import  Flask, jsonify
import requests
from app.otaku import Otaku

app = Flask(__name__)
base_url = "https://api.jikan.moe/v3"
manga = Otaku("manga")
anime = Otaku("anime")


@app.route("/random")
def random_media():
    req = requests.get(base_url+anime.get_random_media())
    if req.status_code == 200:
        return jsonify(req.json())
    else:
        return random_media()

if __name__ == '__main__':
    app.run(port=3000, debug=True)
