FROM python:3.11-alpine


WORKDIR /app

COPY . .

RUN pip install pipenv && pipenv install --deploy --system

EXPOSE 5000

CMD ["sh", "-c", "FLASK_APP=./src/main.py flask run -h 0.0.0.0 -p 5000"]