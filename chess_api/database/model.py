import sqlalchemy as sa
from . import db


class User(db.Model):
    userId = sa.Column(sa.Integer, primary_key=True)
    isParent = sa.Column(sa.Boolean, nullable=False)
    name = sa.Column(sa.String)
    phone = sa.Column(sa.String)
    child_id = db.relationship("Child", backref="user")

class Child(db.Model):
    userId = sa.Column(sa.Integer, sa.ForeignKey(User.userId))
    childId = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    birth = sa.Column(sa.Date)
    sex = sa.Column(sa.Boolean)
    category = sa.Column(sa.String)
    fshrId = sa.Column(sa.Integer, default=0)
    fideId = sa.Column(sa.Integer, default=0)
    trainer = sa.Column(sa.String)
    parent = sa.Column(sa.String)

