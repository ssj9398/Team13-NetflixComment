from flask import Blueprint
import requests
from bs4 import BeautifulSoup

get_contents = Blueprint('get_contents', __name__)


# 모든 컨텐츠 받아오기 (크롤링)
@get_contents.route("/api/contents")
def contents():
    # url = 'https://www.justwatch.com/kr/%EB%8F%99%EC%98%81%EC%83%81%EC%84%9C%EB%B9%84%EC%8A%A4/netflix'
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.86 Safari/537.36'}
    # data = requests.get(url, headers=headers)
    # soup = BeautifulSoup(data.text, 'html.parser')
    # title = soup.select_one()
    return "contents API"
