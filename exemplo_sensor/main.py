import os
import time
import random
from dotenv import load_dotenv
from services.mongo import client
from datetime import datetime

load_dotenv()

SENSOR_NAME_ENV_VAR = "SENSOR_NAME"
MONGODB_NAME_ENV_VAR = "MONGODB_URL"

SENSOR_NAME = os.environ.get(SENSOR_NAME_ENV_VAR, None)
MONGODB_URL = os.environ.get(MONGODB_NAME_ENV_VAR, None)


def send_to_mongo():
    interval = random.uniform(0.1, 1)
    time.sleep(interval)

    num_digits = random.randint(1, 5)

    random_number = (
        random.randint(10 ** (num_digits - 1), 10**num_digits - 1)
        if num_digits > 1
        else random.randint(0, 9)
    )

    data = {"reading": random_number, "sensor": SENSOR_NAME, "date": datetime.now()}

    print(f"Enviando para o db: {data}")

    db = client.get_database("x4glass")
    col = db.get_collection("sensor_log")
    col.insert_one(data)


def main():
    while True:
        print(f"Requisição do sensor: {SENSOR_NAME}")
        send_to_mongo()


if __name__ == "__main__":
    if not SENSOR_NAME:
        raise Exception("Variável de ambiente SENSOR_NAME não foi encontrada!")

    if not MONGODB_URL:
        raise Exception("Variável de ambiente MONGODB_URL não foi encontrada!")

    main()
