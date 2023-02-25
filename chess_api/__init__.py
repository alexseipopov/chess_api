from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres@localhost/chess"

from chess_api.database.model import User, Child
from chess_api.database import db

@app.route("/")
def index():
    return "OK"