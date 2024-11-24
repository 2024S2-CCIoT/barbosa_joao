from domain.abstract.service import AbstractService
import redis
import time

redis_host = "redis-service"
redis_port = 6379
batch_size = 10
r = redis.StrictRedis(host=redis_host, port=redis_port, decode_responses=True)


class ProcessorService(AbstractService):
    def __init__(self):
        super().__init__()

    def run(self):
        queue_length = r.llen("sensor_data")
        if queue_length >= batch_size:
            batch = [r.lpop("sensor_data") for _ in range(batch_size)]
            print(f"Processing batch: {batch}")
            time.sleep(1)

if __name__ == '__main__':
    ProcessorService().run()