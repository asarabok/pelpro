from flask_restful import fields
from app import app


class DateField(fields.Raw):
    def format(self, value):
        return value.strftime(app.config.get("MEASUREMENT_DATE_FORMAT"))
