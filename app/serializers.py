from flask_restful import fields
from .fields import GenericField, DateField


measurement_serializer = {
    "id": fields.Integer,
    "measurement_date": DateField,
    "plant": GenericField,
    "city": GenericField,
    "value": fields.Fixed(decimals=1),
}
