FROM python:3.12-slim

WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile.lock ./

RUN ls -l /app

RUN pipenv install --deploy --ignore-pipfile

COPY . .

ENV PYTHONPATH "${PYTHONPATH}:/app"

CMD ["pipenv", "run", "python", "-u", "./src/infra/services/controller.py"]