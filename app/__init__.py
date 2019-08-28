import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


MAIN_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.abspath(os.path.join(MAIN_DIR, '..'))
SQLALCHEMY_DATABASE_URI = f"sqlite:///journal.db"

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = SQLALCHEMY_DATABASE_URI
app.config["SECRET_KEY"] = SECRET_KEY = 'f\x95\xb7}\xea\xa6\x05\x08\x91:\x0f\xc4\xfd\xa1VYd`\x15\x94N\xdd\xb6\xe4+M\xd9\xa9\xf1\xea\x8fg'
db = SQLAlchemy(app)

from app import views

if __name__ == '__main__':
    db.create_all()
