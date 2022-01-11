from flask import Flask
from home import home_page, get_movies,save_movies
from detail import detail

app = Flask(__name__)

app.register_blueprint(home_page)
app.register_blueprint(get_movies)
app.register_blueprint(save_movies)
app.register_blueprint(detail)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!!'


if __name__ == '__main__':
    app.run()
