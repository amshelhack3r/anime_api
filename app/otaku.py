'''
Create a class otaku(japanese for lover of games and anime)
constructor will have a type(manga or anime) since most endpoints are
similar the difference is the type of content.

'''

#bring in the random library to generate a random integer
from random import randint


class Otaku:
    def __init__(self, media):
        self.media = media;
        self.endpoint = '/'+media+'/'
        pass

    def get_media_by_id(self, id):
        return self.endpoint+str(id)

    def get_random_media(self):
        return self.endpoint+str(randint(1, 30000))
