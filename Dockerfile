FROM python:3.10-alpine

WORKDIR /app

ENV ENVIRONMENT 'docker'

RUN apk add --no-cache libpq-dev gcc musl-dev linux-headers

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "app.py" ]