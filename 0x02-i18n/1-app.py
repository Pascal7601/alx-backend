from flask import Flask, render_template
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)

class Config:
    LANGUAGES = ['fr']
    BABEL_DEFAULT_LOCALE = 'fr'
    BABEL_DEFAULT_TIMEZONE = 'UTC'

app.config.from_object(Config)

@app.get('/')
def home():
    return render_template('0-index.html')

if __name__ == '__main__':
    app.run()
