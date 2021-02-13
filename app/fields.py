from flask_restful import fields
from app import app

class GenericField(fields.Raw):
    def format(self, value):
        return {
            "id": value.id,
            "name": value.name,
            "external_id": value.external_id
        }
