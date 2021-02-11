from .views import HomeView, CityView
from app import app

app.add_url_rule("/", view_func=HomeView.as_view("homeview"))
app.add_url_rule(
    "/city/<string:external_id>", view_func=CityView.as_view("cityview")
)
