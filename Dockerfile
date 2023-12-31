FROM python:3.11-slim-buster
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN pip install -U pip
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
