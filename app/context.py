from app import app
from app.models import City

@app.context_processor
def cities():
    cities = City.query.order_by(City.external_id.asc()).all()
    return dict(cities=cities)
