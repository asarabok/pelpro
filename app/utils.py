from app import app, db
from datetime import datetime
from app.models import City, Plant


def get_date_obj_from_str(date_string):
    return datetime.strptime(
        date_string,
        app.config.get("MEASUREMENT_DATE_FORMAT"),
    ).date()


def get_city_id_from_external_id(external_id):
    city = City.query.filter_by(external_id=external_id).first()

    if not city:
        return None

    return city.id


def get_plant_id_from_external_id(external_id):
    plant = Plant.query.filter_by(external_id=external_id).first()

    if not plant:
        return None

    return plant.id
