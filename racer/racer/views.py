import requests
from django.shortcuts import render, redirect
from bs4 import BeautifulSoup, NavigableString, Tag
# from racer.models import Headline

def scrape(requests):
    resp = requests.get('https://localraces.com/middletown-ny')
    txt = resp.text
    soup = BeautifulSoup(txt, 'lxml')


    print(txt) # before souped
    print(soup)
scrape(requests)







    # session = resquests.Session()
    # url = 'https://localraces.com/middletown-ny'
    # r = requests.get(url)
    # html = r.text
    # # print(r.text)
    # soup = BeautifulSoup(html, features="html.parser")
    #
    # for races in soup.find_all('ul', {'id': 'events'}):
    #     dates = races.find({'class': 'month-day'})
    #     # print(races)
    #     print(dates)
        # for race in races:
        #     print('=============================')
        #     # print(race)
        #     location = race.find('h4') # Location
        #     date = race.find('h3')
        #     print(type(date))
        #     print(location)
