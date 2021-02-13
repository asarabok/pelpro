from flask_restful import reqparse
from datetime import datetime, timedelta
from app.models import Measurement


class DaysDeltaFilter():
    def get_filter_expression(self):
        parser = reqparse.RequestParser()
        parser.add_argument('days_delta', type=int, store_missing=False)
        args = parser.parse_args()

        filter_expression = True
        if args:
            now = datetime.now()
            days_delta = now - timedelta(days=args.get("days_delta"))
            filter_expression = Measurement.measurement_date > days_delta

        return filter_expression
