FROM python:alpine3.18

ENV PYTHONBUFFERED 1

WORKDIR /app
COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD python manage.py runserver 0.0.0.0:80