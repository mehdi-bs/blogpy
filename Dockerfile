FROM python:3.8
LABEL MAINTAINER="Mehdi BS | github.com/mehdi-bs"

ENV PYTHONUNBUFFERED 1

RUN mkdir /blogpy
WORKDIR /blogpy
COPY docker-compose /blogpy

ADD requirements/requirements.txt /blogpy
RUN pip install --upgrade pip
RUN pip install -r re

RUN python manage.py collectstatic --no-input

CMD ["gunicorn","--chdir","blogpy","--bind","8000","blogpy.wsgi:application"]