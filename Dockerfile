FROM python:3.9

RUN mkdir /code
WORKDIR /code
ADD . /code

RUN apt-get update && apt-get install gcc python3-dev cron -y
RUN pip install --upgrade pip
RUN pip install -r requirements/development.txt

EXPOSE 5000

COPY cron/cron /etc/cron.d/cron
RUN chmod 0644 /etc/cron.d/cron
RUN crontab /etc/cron.d/cron
RUN touch /var/log/cron.log

COPY docker-entrypoint.sh /
ENTRYPOINT ["sh", "/docker-entrypoint.sh"]
