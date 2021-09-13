from flask import Flask, render_template
from flask_scss import Scss

app = Flask(__name__)
app.config['DEBUG'] = True

Scss(app, static_dir='static/css', asset_dir='static/scss')


# ------------------------- Главная
@app.route('/Главная/page1')
def main_page1():
    return render_template('Главная/page1.html', title="Главная")


@app.route('/Главная/page2')
def main_page2():
    return render_template('Главная/page2.html', title="Главная")


# ------------------------- Игры
@app.route('/игры/page1')
def play_page1():
    return render_template('игры/page 1.html', title="Игры")


@app.route('/игры/page2')
def play_page2():
    return render_template('игры/page 2.html', title="Игры")


# ------------------------- Киберзона
@app.route('/киберзона/page1')
def kiberzone_page1():
    return render_template('киберзона/page 1.html', title="Киберзона")


@app.route('/киберзона/page2')
def kiberzone_page2():
    return render_template('киберзона/page 2.html', title="Киберзона")


@app.route('/киберзона/page3')
def kiberzone_page3():
    return render_template('киберзона/page 3.html', title="Киберзона")


@app.route('/киберзона/page4')
def kiberzone_page4():
    return render_template('киберзона/page 4.html', title="Киберзона")


if __name__ == '__main__':
    app.run()
