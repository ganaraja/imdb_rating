#!/usr/bin/env python

import sys
import requests
import json

API_KEY = 'd77bda73'


class Imdb:
    def __init__(self, url):
        self.request_url = url

    def get_rating(self):
        result = json.loads(requests.get(self.request_url).text)
        if 'imdbRating' in result.keys():
            return result['imdbRating']
        else:
            return ''


if sys.argv[1]:
    request_url = 'http://www.omdbapi.com/?t=' + \
        sys.argv[1] + '&apikey=' + API_KEY


try:
    imdb = Imdb(request_url)
    print("Imdb rating for the film  - " + sys.argv[1])
    print(imdb.get_rating())
except requests.exceptions.RequestException as e:
    print(e)
    sys.exit(1)
