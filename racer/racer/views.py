import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup
# from racer.models import Headline

# r = requests.get('https://api.github.com/events')
# print(r.text)

def scrape(requests):

    # session = resquests.Session()
    url = 'https://localraces.com/middletown-ny'
    r = requests.get(url)
    html = r.text
    # print(r.text)
    soup = BeautifulSoup(html, features="html.parser")

    
    print(soup)
    # print(soup.find_all(id="li"))
    # print(soup.pzrettify())

    blocks = soup.find_all('div', {"class": item})
    #
    #
    for block in blocks:
        print(block)

scrape(requests)
