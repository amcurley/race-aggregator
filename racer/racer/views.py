import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup, NavigableString, Tag
# from racer.models import Headline

# def scrape(requests):
resp = requests.get('https://localraces.com/middletown-ny')
txt = resp.text
soup = BeautifulSoup(txt, 'html.parser')

location = []
for races in soup.find_all('ul', {'id': 'events'}):
    # print(races)
    for race in races:
        a = race.find('h4')
        if a == -1 or a == None:
            pass
        else:
            location.append(str(a).replace(' ', '').replace('<h4>', '').replace('</h4>', '').replace('\n', ''))
print(location)
