from flask_restful import fields
from app import app


class DateField(fields.Raw):
    def format(self, value):
        return value.strftime(app.config.get("MEASUREMENT_DATE_FORMAT"))


class GenericField(fields.Raw):
    def format(self, value):
        return {
            "id": value.id,
            "name": value.name,
            "external_id": value.external_id
        }
