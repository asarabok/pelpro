from app import app, db
from datetime import datetime
from app.models import Measurement
import importlib


def get_model_class(model_class_name):
    try:
        return getattr(
            importlib.import_module("app.models"), model_class_name
        )
    except AttributeError:
        return None


def get_date_obj_from_str(date_string):
    return datetime.strptime(
        date_string,
        app.config.get("MEASUREMENT_DATE_FORMAT"),
    ).date()


def get_model_obj_id_from_external_id(external_id, model_class_name):
    model_class = get_model_class(model_class_name)
    if not model_class:
        return None

    obj = model_class.query.filter_by(external_id=external_id).first()

    return obj.id if obj else None


def save_measurements(data):
    for measurement in data:
        measurement_obj = Measurement(**measurement)
        db.session.add(measurement_obj)

    db.session.commit()
