import re

from flask import Blueprint, render_template, jsonify
import requests
from bs4 import BeautifulSoup
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.netflix_comment
home = Blueprint('home', __name__)


# home 라우터 (컨텐츠 디비에서 가져온 후 보여줌)
@home.route('/home')
def main():
    r = requests.get('http://127.0.0.1:5000/movies')
    response = r.json()
    movie_title = response['title']
    movie_image = response['image']
    movie_href = response['href']
    return render_template('home.html', movie_title=movie_title, movie_image=movie_image, movie_href=movie_href)


# 모든 컨텐츠 디비에서 가져오기
@home.route("/movies")
def read_movies():
    all_movies = list(db.movie.find({}, {'_id': False}))
    title = []
    image = []
    href = []
    star = []
    for movie in all_movies:
        title.append(movie['movie_title'])
        image.append(movie['movie_image'])
        href.append(movie['href'])
        star.append(movie['star'])
    return jsonify({'title': title,
                    'image': image,
                    'href': href,
                    'star': star})


# 모든 컨텐츠 디비에 저장 (❗️한 번만 실행되야함)
@home.route("/save_movies")
def save_movies():
    url = 'https://www.justwatch.com/kr/%EB%8F%99%EC%98%81%EC%83%81%EC%84%9C%EB%B9%84%EC%8A%A4/netflix'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    data = requests.get(url, headers=headers)
    soup = BeautifulSoup(data.text, 'html.parser')

    new_tags = soup.select(
        '#base > div.title-list.title-list--CLS-block > div div:nth-child(2) > div:nth-child(1) > div > div > a')

    # 컨텐츠 각 항목에 접근 후 디비에 저장
    for tags in new_tags:
        title = tags.img.get('alt')
        href_tag = re.sub('/kr', '/detail', tags['href'])
        star = 0
        if tags.img.get('data-src'):
            src = tags.img.get('data-src')
        else:
            src = tags.img.get('src')

        doc = {
            'movie_title': title,
            'movie_image': src,
            'href': href_tag,
            'star': star,
        }

        db.movie.insert_one(doc)
    return jsonify({'msg': '성공'})
