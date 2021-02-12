import scrapy

from app import app

from .utils import (
    get_city_id_from_external_id,
    get_date_obj_from_str,
    get_plant_id_from_external_id,
)


class MeasurementsSpider(scrapy.Spider):
    name = "measurements"

    def start_requests(self):
        for external_city_id in app.config.get("CITIES_EXTERNAL_IDS"):
            url = app.config.get("MEASUREMENT_CITY_URL").format(
                external_city_id
            )
            yield scrapy.Request(
                url=url,
                callback=self.parse,
                cb_kwargs={"external_city_id": external_city_id},
            )

    def parse(self, response, external_city_id):
        wrapper_header = response.css(
            "#block-system-main > .view-peludna > .view-header"
        )
        wrapper_content = response.css(
            "#block-system-main > .view-peludna > .view-content"
        )
        city_measurement = {
            "measurement_date": self._get_measurement_date(wrapper_header),
            "city_id": get_city_id_from_external_id(external_city_id),
            "measurements": self._get_city_measurements(wrapper_content),
        }

        print(city_measurement)

    def _get_measurement_date(self, wrapper):
        measurement_date_string = wrapper.css(
            (".view-content " ".views-row-1 " "span[data-orig-datum]" "::text")
        ).get()

        return get_date_obj_from_str(measurement_date_string)

    def _get_city_measurements(self, wrapper):
        plant_rows = wrapper.css("div.views-row.span3:nth-child(3n+1)")
        city_measurements = []

        for target_column in plant_rows:
            plant_external_id = self._get_plant_external_id(target_column)
            value = self._get_measurement_value(target_column)
            city_measurements.append(
                {
                    "plant_id": get_plant_id_from_external_id(
                        plant_external_id
                    ),
                    "value": value,
                }
            )

        return city_measurements

    def _get_plant_external_id(self, wrapper):
        return (
            wrapper.css("div.naziv a")
            .attrib["href"]
            .strip()
            .replace("/hr/", "")
        )

    def _get_measurement_value(self, wrapper):
        return wrapper.css("div.vrijednost::text").get()
