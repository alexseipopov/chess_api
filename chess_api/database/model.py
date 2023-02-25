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


class Tournament(db.Model):
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String)
    start = sa.Column(sa.Date)
    finish = sa.Column(sa.Date)
    register = sa.Column(sa.Date)
    place = sa.Column(sa.String)
    address = sa.Column(sa.String)
    map = sa.Column(sa.String)
    stage = db.relationship("Stage", backref="tournament")
    image = db.relationship("Images", backref="tournament")


class Stage(db.Model):
    stageId = sa.Column(sa.Integer, primary_key=True)
    tournamentId = sa.Column(sa.Integer, sa.ForeignKey(Tournament.id))
    name = sa.Column(sa.String)
    start = sa.Column(sa.Date)
    finish = sa.Column(sa.Date)


class Images(db.Model):
    imageId = sa.Column(sa.Integer, primary_key=True)
    tournamentId = sa.Column(sa.Integer, sa.ForeignKey(Tournament.id))
    src = sa.Column(sa.String)
    type = sa.Column(sa.Integer)
