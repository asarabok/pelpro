from flask import redirect, render_template, url_for
from flask.views import View

from app import app
from app.models import City

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
            return render_template('404.html'), 404

        return render_template("city.html", selected_city=selected_city)
