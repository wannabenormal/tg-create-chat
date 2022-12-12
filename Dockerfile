FROM akhmetov/python-telegram:latest

WORKDIR /app

ENV PYTHONBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

COPY ./requirements.txt .

RUN pip install -r requirements.txt

COPY . /app