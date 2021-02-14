import click
from flask import Flask
from flask_migrate import Migrate
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from .settings import CUSTOM_SETTINGS

app = Flask(__name__)

app.config.update(**CUSTOM_SETTINGS)

if app.config["ENV"] == "production":
    app.config.from_object("config.DevelopmentConfig")
elif app.config["ENV"] == "development":
    app.config.from_object("config.DevelopmentConfig")
else:
    app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)


@app.cli.command("load_fixture")
@click.argument("model_class_name")
def load_fixture(model_class_name):
    from .management import LoadFixture
    command = LoadFixture(model_class_name)
    command.run()


@app.cli.command("scrape_measurements")
def scrape_measurements():
    from .management import ScrapeMeasurements
    command = ScrapeMeasurements()
    command.run()


from app import context, urls
from app.models import City, Measurement, Plant
