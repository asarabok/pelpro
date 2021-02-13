from enum import Enum
from datetime import datetime

from app import db

from .models_mixins import GenericMixin


class PlantOriginsEnum(Enum):
    drvece = "drvece"
    korovi = "korovi"


class City(db.Model, GenericMixin):
    def __repr__(self):
        return f"<City {self.name}>"


class Plant(db.Model, GenericMixin):
    origin = db.Column(db.Enum(PlantOriginsEnum), nullable=False)

    def __repr__(self):
        return f"<Plant {self.name}>"


class Measurement(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    scraped_datetime = db.Column(
        db.DateTime, nullable=False, default=datetime.now
    )
    measurement_date = db.Column(
        db.Date,
        nullable=False,
    )

    city_id = db.Column(db.Integer, db.ForeignKey("city.id"), nullable=False)
    city = db.relationship(
        "City", backref=db.backref("measurements", lazy='dynamic')
    )

    plant_id = db.Column(db.Integer, db.ForeignKey("plant.id"), nullable=False)
    plant = db.relationship(
        "Plant", backref=db.backref("measurements", lazy='dynamic')
    )

    value = db.Column(db.Numeric(10, 1), nullable=False)

    __table_args__ = (
        db.UniqueConstraint(
            "measurement_date", "city_id", "plant_id", name="_measurement_uc"
        ),
    )

    def __repr__(self):
        return f"<Measurement {self.id}>"
