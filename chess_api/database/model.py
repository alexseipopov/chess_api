import sqlalchemy as sa
from . import db


class User(db.Model):
    userId = sa.Column(sa.Integer, primary_key=True)
    isParent = sa.Column(sa.Boolean, nullable=False)
    name = sa.Column(sa.String)
    phone = sa.Column(sa.String)

print("here")