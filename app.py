from flask import Flask, render_template
from flask_scss import Scss

app = Flask(__name__)
app.config['DEBUG'] = True

Scss(app, static_dir='static/css', asset_dir='static/scss')


@app.route('/Главная/page1')
def main_page1():
    return render_template('Главная/page1.html', title="Главная")


@app.route('/Главная/page2')
def main_page2():
    return render_template('Главная/page2.html', title="Главная")


if __name__ == '__main__':
    app.run()
