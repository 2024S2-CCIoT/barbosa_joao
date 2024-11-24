from domain.abstract.service import AbstractService
import redis
import time
import random

redis_host = "redis-service"
redis_port = 6379
r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)

class ControllerService(AbstractService):
    def __init__(self):
        super().__init__()

    def run(self, id: str):
        while True:
            data = {"sensor_id": id, "value": 25.5}
            r.rpush("sensor_data", str(data))
            print("Data sent to queue")
            time.sleep(1)

if __name__ == '__main__':
    ControllerService().run(str(random.choice(0, 100)))