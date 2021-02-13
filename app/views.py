from flask import redirect, render_template, url_for
from flask.views import View
from flask_restful import Resource, fields, marshal, reqparse

from app import app
from app.models import City, Measurement, Plant

from .fields import DateField

DEFAULT_CITY_EXTERNAL_ID = app.config.get("DEFAULT_CITY_EXTERNAL_ID")

resource_fields = {
    "id": fields.Integer,
    "measurement_date": DateField,
    "plant": fields.String(attribute=lambda x: x.plant.name),
    "city": fields.String(attribute=lambda x: x.city.name),
    "value": fields.Fixed(decimals=1),
}


class HomeView(View):
    methods = ["GET"]

    def dispatch_request(self):
        return redirect(
            url_for("cityview", external_id=DEFAULT_CITY_EXTERNAL_ID), code=302
        )


class CityView(View):
    methods = ["GET"]

    def dispatch_request(self, external_id):
        selected_city = City.query.filter_by(external_id=external_id).first()
        if not selected_city:
            return render_template("404.html"), 404

        return render_template("city.html", selected_city=selected_city)


class MeasurementsApiView(Resource):
    def get(self):
        data = Measurement.query.all()
        return marshal(data, resource_fields), 200


class CityMeasurementsApiView(Resource):
    def get(self, city_external_id):
        city = City.query.filter_by(
            external_id=city_external_id
        ).first_or_404()

        return marshal(city.measurements.all(), resource_fields), 200


class PlantMeasurementsApiView(Resource):
    def get(self, plant_external_id):
        plant = Plant.query.filter_by(
            external_id=plant_external_id
        ).first_or_404()

        return marshal(plant.measurements.all(), resource_fields), 200


class CityPlantMeasurementsApiView(Resource):
    def get(self, city_external_id, plant_external_id):
        city = City.query.filter_by(
            external_id=city_external_id
        ).first_or_404()

        plant = Plant.query.filter_by(
            external_id=plant_external_id
        ).first_or_404()

        data = city.measurements.filter_by(plant=plant).all()

        return marshal(data, resource_fields), 200
