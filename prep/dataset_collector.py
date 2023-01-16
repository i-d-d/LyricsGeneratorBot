import re
import urllib.request as req
from bs4 import BeautifulSoup

BASE_URL = "https://www.songlyrics.com/"
FILE_PATH = 'song_dataset.txt'


class Artist:
    def __init__(self, name):
        self.url = BASE_URL + name + '-lyrics'

    def songs(self, number):
        r = req.Request(
            url=self.url,
            headers={'User-Agent': 'Mozilla/5.0'}
        )
        art_page = req.urlopen(r)
        art_soup = BeautifulSoup(art_page, features="html.parser")

        track_tag = art_soup.find('table', class_="tracklist")
        song_ref_tags = track_tag.find_all('tr')

        urls = []

        counter = 0
        for ref_tag in song_ref_tags:
            url = ref_tag.find('a').get('href')
            urls.append(url)
            counter += 1
            if counter == number:
                break

        return urls

    @staticmethod
    def write(self, urls, f):
        for url in urls:
            r = req.Request(
                url=url,
                headers={'User-Agent': 'Mozilla/5.0'}
            )
            page = req.urlopen(r)
            soup = BeautifulSoup(page, features="html.parser")
            f.write("<BOS>\n")
            f.write(soup.find('p', id='songLyricsDiv').get_text())
            f.write("\n<EOS>\n")


art = open("artist_names.txt", 'r')
artists = art.read().splitlines()

file = open(FILE_PATH, 'a')

for name in artists:
    webscrapper = Artist(name)
    song_urls = webscrapper.songs(100)
    webscrapper.write(song_urls, file)

file.close()
