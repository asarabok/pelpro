from .views import HomeView
from app import app

app.add_url_rule('/', view_func=HomeView.as_view('homeview'))
