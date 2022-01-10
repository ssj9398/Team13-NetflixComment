from flask import Flask
from detail import detail

app = Flask(__name__)

app.register_blueprint(detail)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!!'


if __name__ == '__main__':
    app.run()
