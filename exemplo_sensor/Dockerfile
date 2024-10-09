FROM python:3.12-slim

WORKDIR /app

RUN pip install pipenv

COPY . .

RUN pipenv install --deploy --ignore-pipfile

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["pipenv", "run", "python", "-u", "main.py"]
