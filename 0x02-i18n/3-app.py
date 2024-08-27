from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)


class Config:
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale():
    languages = app.config.get('LANGUAGES')
    return request.accept_languages.best_match(languages)



@app.get('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()
