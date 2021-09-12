# SportClubProject

## Installation

Install with pip:

```
$ pip install -r requirements.txt
```

## Flask Application Structure

```
.
|────static/
| |────css/
| |────images/
| |────js/
|────templates/
| |────layout.html
| |────Главная/
| | |────page1.html
| | |────page2.html
|──────app.py
|──────Readme.md
|──────requirements.txt
```

## Flask Configuration

#### Example

```
app = Flask(__name__)
app.config['DEBUG'] = True
```

### Configuring From Files

#### Example Usage

```
app = Flask(__name__ )
app.config.from_pyfile('config.Development.cfg')
```

#### cfg example

```
##Flask settings
DEBUG = True  # True/False
TESTING = False
```

#### Builtin Configuration Values

SERVER_NAME: the name and port number of the server.

JSON_SORT_KEYS : By default Flask will serialize JSON objects in a way that the keys are ordered.

- [reference¶](http://flask.pocoo.org/docs/0.12/config/)

## Run Flask

### Run flask for develop

```
$ python app.py
```

In flask, Default port is `5000`

## Reference

Offical Website

- [Flask](http://flask.pocoo.org/)
- [Flask Extension](http://flask.pocoo.org/extensions/)

Tutorial

- [Flask Overview](https://www.slideshare.net/maxcnunes1/flask-python-16299282)
- [In Flask we trust](http://igordavydenko.com/talks/ua-pycon-2012.pdf)

[Wiki Page](https://github.com/tsungtwu/flask-example/wiki)
