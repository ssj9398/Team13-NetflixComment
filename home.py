import re

from flask import Blueprint, render_template
import requests
from bs4 import BeautifulSoup

home = Blueprint('home', __name__)
get_contents = Blueprint('get_contents', __name__)


# Home 라우터
@home.route('/home')
def home():
    return render_template('home.html')


# 모든 컨텐츠 받아오기 (크롤링)
@get_contents.route("/movies")
def movies():
    url = 'https://www.justwatch.com/kr/%EB%8F%99%EC%98%81%EC%83%81%EC%84%9C%EB%B9%84%EC%8A%A4/netflix'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    a_tags = soup.select('#base > div.title-list.title-list--CLS-block > div div:nth-child(2) > div:nth-child(1) > div > div > a')
    all_tags = soup.select(
        '#base > div.title-list.title-list--CLS-block > div > div:nth-child(2) > div:nth-child(1) > div > div > a > div > picture > img')

    for tags in all_tags:
        if tags.has_attr('data-src'):
            print(tags['data-src'])
        else:
            print(tags['src'])

    for tags in a_tags:
        href = tags['href']
        print(re.sub('/kr', '', href))
    return 'hello'
