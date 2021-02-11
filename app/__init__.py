import os

from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from .settings import CUSTOM_SETTINGS

app = Flask(__name__)

app.config.update(**CUSTOM_SETTINGS)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "development":
    app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import urls
from app.models import City, Measurement, Plant
