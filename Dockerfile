FROM python:3.12-slim

ARG APP_PORT, APP_HOST

ENV APP_PORT=${APP_PORT}\
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .

RUN pip install --upgrade pip && pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE ${APP_PORT}

CMD python manage.py runserver 0.0.0.0:${APP_PORT}
