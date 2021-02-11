from app import db


class GenericMixin:
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False, unique=True)
    external_id = db.Column(db.String(30), nullable=False, unique=True)
