from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres@localhost/chess"

from chess_api.database.model import User

@app.route("/")
def index():
    test = User.query.all()
    print(test)
    return "OK"