import os

from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

from .settings import CUSTOM_SETTINGS

app = Flask(__name__)

app.config.update(**CUSTOM_SETTINGS)

if app.config["ENV"] == "production":
    app.config.from_object("config.ProductionConfig")
elif app.config["ENV"] == "development":
    app.config.from_object("config.DevelopmentConfig")

db = SQLAlchemy(app)
api = Api(app)

from app import context, urls
from app.models import City, Measurement, Plant
