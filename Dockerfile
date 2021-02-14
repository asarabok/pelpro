FROM python:3.7

RUN mkdir /code
WORKDIR /code
ADD . /code

RUN apt-get update && apt-get install gcc python3-dev -y
RUN pip install --upgrade pip
RUN pip install -r requirements/development.txt

EXPOSE 5000

COPY docker-entrypoint.sh /
ENTRYPOINT ["sh", "/docker-entrypoint.sh"]
