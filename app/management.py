import importlib
import json
from os import path

from flask_script import Command, Option
from scrapy.crawler import CrawlerProcess

from app import app, db
from app.crawlers import MeasurementsSpider


class LoadFixture(Command):
    option_list = (Option("--model-class", "-m", dest="model_class_name"),)
    messages = {
        "success": "SUCCESS: {} fixtures sucessfully added to DB",
        "error": "ERROR: Error while importing {} fixtures to DB",
    }

    def run(self, model_class_name):
        fixture_path = f"{app.root_path}/fixtures/{model_class_name}.json"
        file_exists = path.exists(fixture_path)
        model_class = self.get_model_class(model_class_name)
        if file_exists and model_class:
            with open(fixture_path) as json_fixture:
                fixture_data = json.load(json_fixture)
                for fixture_item in fixture_data:
                    db_record = model_class(**fixture_item)
                    db.session.add(db_record)
                db.session.commit()
                self.print_output_message("success", model_class_name)

    def print_output_message(self, message_type, model_class_name):
        message = self.messages.get(message_type)
        print(message.format(model_class_name))

    def get_model_class(self, model_class_name):
        try:
            return getattr(
                importlib.import_module("app.models"), model_class_name
            )
        except AttributeError:
            return None


class CrawlMeasurements(Command):
    def run(self):
        process = CrawlerProcess()
        process.crawl(MeasurementsSpider)
        process.start()
