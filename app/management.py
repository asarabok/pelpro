import json
from os import path

from scrapy.crawler import CrawlerProcess

from app import app, db
from app.scrapers import MeasurementsSpider

from .utils import get_model_class


class LoadFixture:
    messages = {
        "success": "SUCCESS: {} fixtures sucessfully added to DB",
        "error": "ERROR: Error while importing {} fixtures to DB",
    }

    def __init__(self, model_class_name):
        self.model_class_name = model_class_name

    def run(self):
        fixture_path = f"{app.root_path}/fixtures/{self.model_class_name}.json"
        file_exists = path.exists(fixture_path)
        model_class = get_model_class(self.model_class_name)
        if file_exists and model_class:
            with open(fixture_path) as json_fixture:
                fixture_data = json.load(json_fixture)
                for fixture_item in fixture_data:
                    db_record = model_class(**fixture_item)
                    db.session.add(db_record)
                db.session.commit()
                self.print_output_message("success")

    def print_output_message(self, message_type):
        message = self.messages.get(message_type)
        print(message.format(self.model_class_name))


class ScrapeMeasurements:
    def run(self):
        process = CrawlerProcess()
        process.crawl(MeasurementsSpider)
        process.start()
