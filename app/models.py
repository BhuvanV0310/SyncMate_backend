from . import db
from sqlalchemy.dialects.postgresql import ARRAY

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    age = db.Column(db.Integer, nullable=False)
    interests = db.Column(ARRAY(db.String), nullable=False)
    bio = db.Column(db.String(255), nullable=True)
    profile_picture = db.Column(db.String(255), nullable=True)

class Shortlist(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    match_id = db.Column(db.Integer, nullable=False)
