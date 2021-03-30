FROM python:3.8

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY ./requirements.txt .
RUN pip install -r requirements.txt

WORKDIR /code
COPY . /code/

RUN pip install psycopg2-binary

RUN pip install psycopg2