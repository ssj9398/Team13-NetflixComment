<h3 align="center"><b>항해99 1주차 팀 미니프로젝트, NetflixComment</b></h3>

<h4 align="center">📆 2022.01.10 ~ 2022.01.13</h4>
<br>
<br>

## 📌 팀원 소개

|[팀장] 장윤철|[팀원] 손성진|[팀원] 임현우|
|:----:|:-----:|:----:|
|<img src="https://avatars.githubusercontent.com/u/46017029?v=4" alt="avatar" height="150px" width="150px" /> | <img src="https://avatars.githubusercontent.com/u/48196352?v=4" alt="avatar" height="150px" width="150px" /> | <img src="https://avatars.githubusercontent.com/u/76833697?v=4" alt="avatar" height="150px" width="150px" /> |
|[name8965](https://github.com/name8965)|[ssj9398](https://github.com/ssj9398)|[hyunwoome](https://github.com/hyunwoome)|

<br>

---

<h3><b>🎫 프로젝트 소개 🎫</b></h3>
- "이 넷플릭스 유명하던데 재미있나?"
- 사람들과 넷플릭스의 드라마/영화의 한줄평을 공유해보자!!
<br><br> 

<h3><b>🎞 프로젝트 시연영상 🎞</b></h3>
https://youtu.be/-lMBHvXTHxU

---

<br>
<h3 align="center"><b>🛠 Tech Stack 🛠</b></h3>
<p align="center">
<img src="https://img.shields.io/badge/javascript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black">
<img src="https://img.shields.io/badge/jquery-0769AD?style=for-the-badge&logo=jquery&logoColor=white">
<img src="https://img.shields.io/badge/html-E34F26?style=for-the-badge&logo=html5&logoColor=white">
<img src="https://img.shields.io/badge/css-1572B6?style=for-the-badge&logo=css3&logoColor=white">
<img src="https://img.shields.io/static/v1?style=for-the-badge&message=Bootstrap&color=7952B3&logo=Bootstrap&logoColor=FFFFFF&label=">
<img src="https://img.shields.io/badge/github-181717?style=for-the-badge&logo=github&logoColor=white">
<img src="https://img.shields.io/badge/linux-FCC624?style=for-the-badge&logo=linux&logoColor=black">
<img src="https://img.shields.io/badge/aws-232F3E?style=for-the-badge&logo=aws&logoColor=white">
</br>
<img src="https://img.shields.io/badge/Python-F80000?style=for-the-badge&logo=Python&logoColor=white">
<img src="https://img.shields.io/badge/Flask-4FC08D?style=for-the-badge&logo=Flask&logoColor=white">
<img src="https://img.shields.io/badge/Jinja-7952B3?style=for-the-badge&logo=Jinja&logoColor=white">
<img src="https://img.shields.io/badge/MongoDB-61DAFB?style=for-the-badge&logo=MongoDB&logoColor=white">

<br><br>
<h3 align="center"><b>🎬 Getting Started 🎬</b></h3>
<pre>
<code>
~$ cd Team13-NetflixComment
~$ sudo chmod 755 initail_ec2.sh
~$ ./initial_ec2.sh
~$ pip install flask
~$ pip install mongo
~$ python3 app.py
</code>
</pre>

<br>
<h3 align="center"><b>📂 Project Directory Structure 📁</b></h3>
<pre>
<code>
/static
     ├── /bookmark.svg
     ├── /detail.css
     ├── /home.css
     ├── /login.css
     ├── /Netflix-logo.png
/templates
     ├── /detail.html
     ├── /home.html
     └── /login.html
├── /detail.py
├── /app.py
└── /home.py
</code>
</pre>
<br>

---


<h3 align="center"><b>🏷 API Table 🏷</b></h3>

#### User
|기능|Method|URL|request|response|
|:--:|:--:|:--:|:--:|:--:|
|로그인|POST|/login| id,pw  |    |
|회원가입|POST|/register|  id,pw  |  가입 완료 메세지  |
|로그아웃|GET|/logout|    |    |
|즐겨찾기 추가|POST|/api/addfavorite|movie_title|추가된 영화제목|
|즐겨찾기 삭제|POST|/api/delfavorite|movie_title|삭제된 영화제목|

#### Movie

|기능|Method|URL|request|response|
|:--:|:--:|:--:|:--:|:--:|
|컨텐츠 전체 조회|GET|/movies||전체 컨텐츠 리스트|
|특정 컨텐츠 상세 조회|GET|/detail/:category/:movie_name||특정 컨텐츠|
|즐겨찾기 확인|GET|/check_bookmark||


#### Review

 기능  |      Method     | URL |  request   |        response       |
| :-: | :----------: | :----: | :-------------: | :--------------: |
|  리뷰 리스트  | GET  |  /review   |                 |   "리뷰 조회"     |
|  리뷰 작성  |  POST |  /review  |review, star, movieTitle | "리뷰 등록 완료"  |
|  리뷰 수정  |  PUT |  /review|  id, date, review   |  "수정 완료"     |
|  리뷰 삭제  | DELETE  |  /review |  userid, review, starValue, writeTime   |  "삭제 완료"    |
| 모든 리뷰 리스트 | GET | /allReview |  | review list |

#### Movie Crawling (❗️최초 1회만 실행)

기능  |      Method     | URL |  request   |        response       |
| :-: | :----------: | :----: | :-------------: | :--------------: |
|  영화 크롤링  | GET  |  /save_movies   |                 |   성공     |


---

<h3 align="center"><b>✏ Trouble Shooting ✏</b></h3>
<br>
<details>
    <summary>
        <b>ajax로 데이터를 받아오고 화면으로 뿌려줄 때, 비동기로 작동하기 때문에 
요소들이 생성되기전에 dom에 접근하게 되어 UI를 다루기가 쉽지 않았습니다. </b>
    </summary>
    <br>해결 : 순차적으로 실행되 접근할 수 있게끔 ajax메서드 안에서 작성해서 해결했습니다.
</details>
<details>
    <summary>
        <b>순환 참조(임포트) 문제
개별 파이썬 파일 작업으로 blueprint를 사용하였는데
ex) app.py <- detail.py
이때 detail에서도 app.py를 임포트 할 경우 에러가 발생하였다. </b>
    </summary>
    <br>해결 : 전역으로 임포트 하지 않고 함수내에서 임포트 하는 방법으로 해결
</details>
