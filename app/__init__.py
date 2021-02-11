import os
from .settings import CUSTOM_SETTINGS

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config.update(**CUSTOM_SETTINGS)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "development":
    app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)

from app import urls
from app.models import City, Measurement, Plant