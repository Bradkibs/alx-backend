#!/usr/bin/env python3
"""FLASK APP WITH I18N"""

from flask import Flask, render_template, request, g
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """CONFIG CLASS FOR LANGUAGE"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """returns the dict or None"""
    idx = request.args.get('login_as')
    if int(idx) in users:
        return users[int(idx)]
    return None


@app.before_request
def before_request():
    """Function to store an instance of a user in g.user"""
    l_user = get_user()
    if l_user:
        g.user = l_user


@babel.localeselector
def get_locale():
    """Setting languages"""
    locale = request.args.get("locale")
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """entry point"""
    login = False
    if g.get('user') is not None:
        login = True
    return render_template("5-index.html", login=login)


if __name__ == "__main__":
    app.run()
