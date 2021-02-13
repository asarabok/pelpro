FROM python:3.9

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD . /code

RUN apt-get update && apt-get install gcc python3-dev -y
RUN pip install --upgrade pip
RUN pip install -r requirements/development.txt

RUN python manage.py db upgrade
RUN python manage.py load_fixture -m City
RUN python manage.py load_fixture -m Plant
RUN python manage.py load_fixture -m Measurement

COPY docker-entrypoint.sh /
ENTRYPOINT ["sh", "/docker-entrypoint.sh"]
