from flask import Flask, render_template
from flask_scss import Scss

app = Flask(__name__)
app.config['DEBUG'] = True

Scss(app, static_dir='static/css', asset_dir='static/scss')


#------------------------- Главная
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


# ------------------------- Клубы
@app.route('/Клубы/page1')
def club_page1():
    return render_template('Клубы/page 1.html', title="Клубы")


# ------------------------- маркетинг
@app.route('/маркетинг/page1')
def marketing_page1():
    return render_template('маркетинг/page 1.html', title="маркетинг")


# ------------------------- медиа
@app.route('/медиа/page1')
def media_page1():
    return render_template('медиа/page 1.html', title="медиа")


# ------------------------- Мероприятия
@app.route('/Мероприятия/page1')
def event_page1():
    return render_template('Мероприятия/page1.html', title="Мероприятия")


# ------------------------- новости
@app.route('/новости/page1')
def news_page1():
    return render_template('новости/main.html', title="новости")


# ------------------------- поиск игроков
@app.route('/поискигроков/page1')
def search_player_page1():
    return render_template('поиск игроков/page 1.html', title="поиск игроков")


# ------------------------- сборные
@app.route('/сборные/page1')
def team_page1():
    return render_template('сборные/page 1.html', title="сборные")


# ------------------------- секция
@app.route('/секция/page1')
def section_page1():
    return render_template('секция/page1.html', title="секция")


# ------------------------- спортклуб
@app.route('/спортклуб/page1')
def sport_club_page1():
    return render_template('спортклуб/page 1.html', title="спортклуб")


# ------------------------- турниры
@app.route('/турниры/page1')
def tour_page1():
    return render_template('турниры/page 1.html', title="турниры")


if __name__ == '__main__':
    app.run()
