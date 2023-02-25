from flask import Flask

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres@localhost/chess"

from chess_api.api import api
app.register_blueprint(api)
