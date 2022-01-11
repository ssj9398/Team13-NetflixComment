import urllib

from flask import render_template, Blueprint, request, jsonify
import requests
from bs4 import BeautifulSoup
from urllib import parse
import datetime

from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client.netflix_comment

detail = Blueprint('detail', __name__)


@detail.route('/detail/<category>/<movie_name>')
def main(movie_name, category):
    movie_name = urllib.parse.quote(movie_name, safe='')
    category = parse.quote(category)
    url = f'https://www.justwatch.com/kr/{category}/{movie_name}'

    data = requests.get(url)
    soup = BeautifulSoup(data.text, 'html.parser')

    global movieTitle
    movieTitle = soup.select_one(
        '#base > div.jw-info-box > div > div.jw-info-box__container-content > div:nth-child(2) > div.title-block__container > div.title-block > div').text
    print("movieTitle = " + movieTitle)

    movieGenre = soup.select_one(
        '#base > div.jw-info-box > div > div.jw-info-box__container-sidebar > div > aside > div.hidden-sm.visible-md.visible-lg.title-sidebar__desktop > div.title-info > div:nth-child(3) > div.detail-infos__value').text
    print("movieGenre = " + movieGenre)

    movieTime = soup.select_one(
        '#base > div.jw-info-box > div > div.jw-info-box__container-sidebar > div > aside > div.hidden-sm.visible-md.visible-lg.title-sidebar__desktop > div.title-info > div:nth-child(4) > div.detail-infos__value').text
    print("movieTime = " + movieTime)

    movieImage = soup.select_one(
        '#base > div.jw-info-box > div > div.jw-info-box__container-sidebar > div > aside > div.hidden-xs.visible-sm.hidden-md.hidden-lg.title-sidebar__desktop > div > picture > source:nth-child(1)')[
        "data-srcset"].split(',')[0]
    print("movieImage = " + movieImage)

    movieSummary = soup.select_one(
        '#base > div.jw-info-box > div > div.jw-info-box__container-content > div:nth-child(2) > div:nth-child(6) > div:nth-child(1) > div:nth-child(4) > p > span')

    dramaSummary = soup.select_one(
        '#base > div.jw-info-box > div > div.jw-info-box__container-content > div:nth-child(2) > div:nth-child(7) > div:nth-child(1) > div:nth-child(4) > p > span')
         ##base > div.jw-info-box.jw-info-box--no-card > div > div.jw-info-box__container-content > div:nth-child(2) > div:nth-child(6) > div:nth-child(1) > div:nth-child(4) > p
    if str(movieSummary) != 'None':
        movieSummary = movieSummary.text

    elif str(movieSummary) == 'None':
        movieSummary = dramaSummary.text

    return render_template('detail.html', movieTitle=movieTitle, movieGenre=movieGenre, movieTime=movieTime,
                           movieSummary=movieSummary, movieImage=movieImage)


@detail.route('/review', methods=['POST'])
def write_review():
    print(movieTitle)
    now = datetime.datetime.now()
    review = request.form['Review']
    review = review.replace("  ", " ")
    starValue = request.form['starValue']
    #print("Review length"+len(str(Review)))
    print("Review = " +review + "starValue = " +starValue)
    if starValue != "" and review !="":
        nowDatetime = now.strftime('%Y-%m-%d %H:%M:%S')

        doc = {
            'Review': review,
            'starValue': starValue,
            'movieTitle': movieTitle,
            'nowDatetime': nowDatetime
        }
        db.review.insert_one(doc)

        return jsonify({'msg': '이 요청은 POST!'})


@detail.route('/review', methods=['GET'])
def read_reviews():
    reviews = list(db.review.find({"movieTitle":movieTitle}, {'_id': False}))
    return jsonify({'all_reviews': reviews})
