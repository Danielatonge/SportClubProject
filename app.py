from flask import Flask, render_template, redirect, url_for
from flask_scss import Scss

app = Flask(__name__)
app.config['DEBUG'] = True

Scss(app, static_dir='static/css', asset_dir='static/scss')


@app.route('/')
def main():
    return redirect(url_for('main_page1'))


@app.route('/Главная/page1')
def main_page1():
    return render_template('Главная/page1.html', title="Главная")


@app.route('/Главная/page2')
def main_page2():
    return render_template('Главная/page2.html', title="Главная")


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


# ------------------------- Игры
@app.route('/игры/page1')
def play_page1():
    return render_template('игры/page 1.html', title="Игры")


@app.route('/игры/page2')
def play_page2():
    return render_template('игры/page 2.html', title="Игры")


# ------------------------- Клубы
@app.route('/Клубы/page1')
def club_page1():
    return render_template('Клубы/page 1.html', title="Клубы")


@app.route('/Клубы/page2')
def club_page2():
    return render_template('Клубы/page 2.html', title="Клубы")


@app.route('/Клубы/page3')
def club_page3():
    return render_template('Клубы/page 3.html', title="Клубы")


@app.route('/Клубы/page4')
def club_page4():
    return render_template('Клубы/page 4.html', title="Клубы")


@app.route('/Клубы/page5')
def club_page5():
    return render_template('Клубы/page 5.html', title="Клубы")


@app.route('/Клубы/page6')
def club_page6():
    return render_template('Клубы/page 6.html', title="Клубы")


@app.route('/Клубы/page7')
def club_page7():
    return render_template('Клубы/page 7.html', title="Клубы")


@app.route('/Клубы/page8')
def club_page8():
    return render_template('Клубы/page 8.html', title="Клубы")


# ------------------------- маркетинг
@app.route('/маркетинг/page1')
def marketing_page1():
    return render_template('маркетинг/page 1.html', title="маркетинг")


@app.route('/маркетинг/page2')
def marketing_page2():
    return render_template('маркетинг/page 2.html', title="маркетинг")


@app.route('/маркетинг/page3')
def marketing_page3():
    return render_template('маркетинг/page 3.html', title="маркетинг")


@app.route('/маркетинг/page4')
def marketing_page4():
    return render_template('маркетинг/page 4.html', title="маркетинг")


@app.route('/маркетинг/page5')
def marketing_page5():
    return render_template('маркетинг/page 5.html', title="маркетинг")


# ------------------------- медиа
@app.route('/медиа/page1')
def media_page1():
    return render_template('медиа/page 1.html', title="медиа")


@app.route('/медиа/page2')
def media_page2():
    return render_template('медиа/page 2.html', title="медиа")


@app.route('/медиа/page3')
def media_page3():
    return render_template('медиа/page 3.html', title="медиа")


@app.route('/медиа/page4')
def media_page4():
    return render_template('медиа/page 4.html', title="медиа")


@app.route('/медиа/page5')
def media_page5():
    return render_template('медиа/page 5.html', title="медиа")


# ------------------------- Мероприятия
@app.route('/Мероприятия/page1')
def event_page1():
    return render_template('Мероприятия/page1.html', title="Мероприятия")


@app.route('/Мероприятия/page2')
def event_page2():
    return render_template('Мероприятия/page2.html', title="Мероприятия")


@app.route('/Мероприятия/page3')
def event_page3():
    return render_template('Мероприятия/page3.html', title="Мероприятия")


@app.route('/Мероприятия/page4')
def event_page4():
    return render_template('Мероприятия/page4.html', title="Мероприятия")


@app.route('/Мероприятия/page5')
def event_page5():
    return render_template('Мероприятия/page5.html', title="Мероприятия")


@app.route('/Мероприятия/page6')
def event_page6():
    return render_template('Мероприятия/page6.html', title="Мероприятия")


@app.route('/Мероприятия/page7')
def event_page7():
    return render_template('Мероприятия/page7.html', title="Мероприятия")


@app.route('/Мероприятия/page8')
def event_page8():
    return render_template('Мероприятия/page8.html', title="Мероприятия")


# ------------------------- новости
@app.route('/новости/main')
def news_page1():
    return render_template('новости/main.html', title="новости")


@app.route('/новости/min')
def news_page2():
    return render_template('новости/min.html', title="новости")


@app.route('/новости/max')
def news_page3():
    return render_template('новости/max.html', title="новости")


# ------------------------- поиск игроков
@app.route('/поискигроков/page1')
def search_player_page1():
    return render_template('поиск игроков/page 1.html', title="поиск игроков")


@app.route('/поискигроков/page2')
def search_player_page2():
    return render_template('поиск игроков/page 2.html', title="поиск игроков")


# ------------------------- сборные
@app.route('/сборные/page1')
def team_page1():
    return render_template('сборные/page 1.html', title="сборные")


@app.route('/сборные/page2')
def team_page2():
    return render_template('сборные/page 2.html', title="сборные")


@app.route('/сборные/page3')
def team_page3():
    return render_template('сборные/page 3.html', title="сборные")


@app.route('/сборные/page4')
def team_page4():
    return render_template('сборные/page 4.html', title="сборные")


@app.route('/сборные/page5')
def team_page5():
    return render_template('сборные/page 5.html', title="сборные")


@app.route('/сборные/page6')
def team_page6():
    return render_template('сборные/page 6.html', title="сборные")


@app.route('/сборные/page7')
def team_page7():
    return render_template('сборные/page 7.html', title="сборные")


@app.route('/сборные/page8')
def team_page8():
    return render_template('сборные/page 8.html', title="сборные")


# ------------------------- секция
@app.route('/секция/page1')
def section_page1():
    return render_template('секция/page1.html', title="секция")


@app.route('/секция/page2')
def section_page2():
    return render_template('секция/page2.html', title="секция")


@app.route('/секция/page3')
def section_page3():
    return render_template('секция/page3.html', title="секция")


@app.route('/секция/page4')
def section_page4():
    return render_template('секция/page4.html', title="секция")


# ------------------------- спортклуб
@app.route('/спортклуб/page1')
def sport_club_page1():
    return render_template('спортклуб/page 1.html', title="спортклуб")


@app.route('/спортклуб/page2')
def sport_club_page2():
    return render_template('спортклуб/page 2.html', title="спортклуб")


@app.route('/спортклуб/page3')
def sport_club_page3():
    return render_template('спортклуб/page 3.html', title="спортклуб")


@app.route('/спортклуб/page4')
def sport_club_page4():
    return render_template('спортклуб/page 4.html', title="спортклуб")


@app.route('/спортклуб/page5')
def sport_club_page5():
    return render_template('спортклуб/page 5.html', title="спортклуб")


@app.route('/спортклуб/page6')
def sport_club_page6():
    return render_template('спортклуб/page 6.html', title="спортклуб")


# ------------------------- турниры
@app.route('/турниры/page1')
def tour_page1():
    return render_template('турниры/page 1.html', title="турниры")


@app.route('/турниры/page2')
def tour_page2():
    return render_template('турниры/page 2.html', title="турниры")


@app.route('/турниры/page3')
def tour_page3():
    return render_template('турниры/page 3.html', title="турниры")


@app.route('/турниры/page4')
def tour_page4():
    return render_template('турниры/page 4.html', title="турниры")


@app.route('/турниры/page5')
def tour_page5():
    return render_template('турниры/page 5.html', title="турниры")


if __name__ == '__main__':
    app.run()
