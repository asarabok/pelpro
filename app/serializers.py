from flask_restful import fields
from .fields import GenericField


measurement_serializer = {
    "id": fields.Integer,
    "measurement_date": fields.String,
    "plant": GenericField,
    "city": GenericField,
    "value": fields.Fixed(decimals=1),
}
