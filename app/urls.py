from app import api, app

from .views import (
    CityMeasurementsApiView,
    CityPlantMeasurementsApiView,
    CityView,
    HomeView,
    MeasurementsApiView,
    PlantMeasurementsApiView,
)

api_base_url = "/api/measurements"

app.add_url_rule("/", view_func=HomeView.as_view("homeview"))
app.add_url_rule(
    "/city/<string:external_id>", view_func=CityView.as_view("cityview")
)
api.add_resource(MeasurementsApiView, api_base_url)
api.add_resource(
    CityMeasurementsApiView, f"{api_base_url}/city/<string:city_external_id>"
)
api.add_resource(
    PlantMeasurementsApiView,
    f"{api_base_url}/plant/<string:plant_external_id>",
)
api.add_resource(
    CityPlantMeasurementsApiView,
    f"{api_base_url}/city/<string:city_external_id>/<string:plant_external_id>",
)
