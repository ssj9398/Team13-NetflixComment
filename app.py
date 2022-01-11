import hashlib
import datetime
from datetime import datetime, timedelta
import jwt  #패키지 PyJWT
from flask import Flask, render_template,jsonify, request,redirect,url_for
from pymongo import MongoClient
from home import get_contents
from detail import detail

#암호화 키 / JWT 토큰을 사용할때 쓰는 비밀문자열
SECRET_KEY = 'hanghae_13'

client = MongoClient('localhost', 27017)
db = client.netflix_comment

app = Flask(__name__)

app.register_blueprint(get_contents)
app.register_blueprint(detail)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!!'

# 로그인라우터
@app.route('/login', methods=['GET'])
def login_page():

    msg = request.args.get("msg")
    token_receive = request.cookies.get('mytoken')

    try:
        payload = jwt.decode(token_receive,SECRET_KEY,algorithms=['HS256'])
        user_info = db.User.find_one({"id":payload['id']})
        return redirect(url_for("home"))

    except:
        return render_template('login.html')

# 회원가입 api
@app.route('/api/register',methods=['POST'] )
def register():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    # pwc_receive = request.form['pwc_give']
    #필요없나?

    #sha256방법으로 암호화해서 저장
    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    doc = {
        'id':id_receive,
        'pw':pw_hash
    }
    db.User.insert_one(doc)

    return jsonify({'msg':id_receive})

#회원가입 ID중복 확인
@app.route('/id_dup_check',methods=['POST'])
def id_dup_check():
    id = request.form['id_give']
    dup_check = bool(db.User.find_one({'id':id}))
    return jsonify({'msg':dup_check})

#로그인 시
@app.route('/api/login', methods=['POST'])
def login():
    id_receive = request.form['id_give']
    pw_receive = request.form['pw_give']

    pw_hash = hashlib.sha256(pw_receive.encode('utf-8')).hexdigest()

    result = db.User.find_one({'id':id_receive,'pw':pw_hash})

    if result is not None:
        payload = {
            'id' : id_receive,
            # 'exp' : datetime.datetime.utcnow() + timedelta(seconds = 60 * 60 * 24)
            'exp' : datetime.utcnow() + timedelta(seconds = 30) #test

        }
        extest =datetime.utcnow() + timedelta(seconds = 30) #test
        token = jwt.encode(payload,SECRET_KEY, algorithm='HS256')

        return jsonify({'result':'success','token':token})
    #로그인 실패 시(아이디/비번 다름)
    else:
        return jsonify({'result':'fail','msg':'아이디/비밀번호가 일치하지 않습니다.'})


# @detail.route('/home')
# def home():
#     token_receive = request.cookies.get('mytoken')
#     try:
#         payload = jwt.decode(token_receive, SECRET_KEY, algorithms=['HS256'])
#         user_info = db.User.find_one({"id": payload['id']})
#         return render_template('home.html')
#     except jwt.ExpiredSignatureError:
#         return redirect(url_for("login_page",msg="로그인 시간 만료"))
#     except jwt.exceptions.DecodeError:
#         return redirect(url_for("login_page",msg="로그인 정보 없음"))


if __name__ == '__main__':
    app.run()
