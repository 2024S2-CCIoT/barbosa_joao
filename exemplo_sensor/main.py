import os
import time
import random
from dotenv import load_dotenv

load_dotenv()

SENSOR_NAME_ENV_VAR = "SENSOR_NAME"
SENSOR_NAME = os.environ.get(SENSOR_NAME_ENV_VAR, None)


def esperar_aleatorio():
    intervalo = random.uniform(0.1, 2)
    time.sleep(intervalo)


def main():
    while True:
        print(f"Requisição do sensor: {SENSOR_NAME}")
        esperar_aleatorio()


if __name__ == "__main__":
    if not SENSOR_NAME:
        raise Exception("Variável de ambiente SENSOR_NAME não foi encontrada!")

    main()
