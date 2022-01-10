from flask import render_template, Blueprint

detail = Blueprint('detail', __name__)

@detail.route('/detail')
def main():
    return render_template('detail.html')