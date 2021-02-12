import scrapy

from app import app


class MeasurementsSpider(scrapy.Spider):
    name = "measurements"

    def start_requests(self):
        for external_city_id in app.config.get("CITIES_EXTERNAL_IDS"):
            url = app.config.get("MEASUREMENT_CITY_URL").format(
                external_city_id
            )
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        print(response)
