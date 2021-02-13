from flask import redirect, render_template, url_for
from flask.views import View
from flask_restful import Resource, marshal

from app import app
from app.models import City, Measurement, Plant

from .filters import DaysDeltaFilter
from .serializers import measurement_serializer

DEFAULT_CITY_EXTERNAL_ID = app.config.get("DEFAULT_CITY_EXTERNAL_ID")


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


class MeasurementsApiView(Resource, DaysDeltaFilter):
    def get(self):
        data = Measurement.query.filter(self.get_filter_expression())
        return (
            marshal(
                data.order_by(Measurement.measurement_date).all(),
                measurement_serializer,
            ),
            200,
        )


class CityMeasurementsApiView(Resource, DaysDeltaFilter):
    def get(self, city_external_id):
        city = City.query.filter_by(
            external_id=city_external_id
        ).first_or_404()
        data = city.measurements.filter(self.get_filter_expression())

        return (
            marshal(
                data.order_by(Measurement.measurement_date).all(),
                measurement_serializer,
            ),
            200,
        )


class PlantMeasurementsApiView(Resource, DaysDeltaFilter):
    def get(self, plant_external_id):
        plant = Plant.query.filter_by(
            external_id=plant_external_id
        ).first_or_404()
        data = plant.measurements.filter(self.get_filter_expression())

        return (
            marshal(
                data.order_by(Measurement.measurement_date).all(),
                measurement_serializer,
            ),
            200,
        )


class CityPlantMeasurementsApiView(Resource, DaysDeltaFilter):
    def get(self, city_external_id, plant_external_id):
        city = City.query.filter_by(
            external_id=city_external_id
        ).first_or_404()

        plant = Plant.query.filter_by(
            external_id=plant_external_id
        ).first_or_404()

        plants_in_cities = city.measurements.filter_by(plant=plant)
        data = plants_in_cities.filter(self.get_filter_expression())

        return (
            marshal(
                data.order_by(Measurement.measurement_date).all(),
                measurement_serializer,
            ),
            200,
        )
