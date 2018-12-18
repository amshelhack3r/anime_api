'''
Create a class otaku(japanese for lover of games and anime)
constructor will have a type(manga or anime) since most endpoints are
similar the difference is the type of content.

'''

# bring in the random library to generate a random integer
from random import randint


class Otaku:
    def __init__(self, media):
        self.media = media
        self.endpoint = '/'+media
        pass

    def get_media_by_id(self, id):
        return self.endpoint+str(id)

    def get_media_by_title(self, title):
        return '/search'+self.endpoint+'?q='+title+'/1'

    def get_random_media(self):
        return self.endpoint+'/'+str(randint(1, 30000))

    @staticmethod
    def get_anime_by_season(year, season):
        return '/season/'+year+'/'+season

    def get_media_by_genre(self, genre):
        genres = {
            "action": 1,
            "adventure": 2,
            "cars": 3,
            "comedy": 4,
            "dementia": 5,
            "demons": 6,
            "mystery": 7,
            "drama": 8,
            "ecchi": 9,
            "fantasy": 10,
            "game": 11,
            "harem": 35,
            "hentai": 12,
            "historical": 13,
            "horror": 14,
            "josei": 43,
            "kids": 15,
            "magic": 16,
            "martial_arts": 17,
            "mecha": 18,
            "military": 38,
            "music": 19,
            "parody": 20,
            "police": 39,
            "psychological": 40,
            "shoujo": 25,
            "shoujo ai": 26,
            "shounen": 27,
            "shounen ai": 28,
            "slice of life": 36,
            "space": 29,
            "sports": 30,
            "superpower": 31,
            "supernatural": 37,
            "thriller": 41,
            "vampire": 32,
            "yuri": 34,
            "yaoi": 33
        }
        return '/genre/'+self.media+'/'+str(genres[genre])
