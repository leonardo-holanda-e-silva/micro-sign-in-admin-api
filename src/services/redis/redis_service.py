import json
import aioredis

class RedisService:
    def __init__(self, redis_url: str):
        self.redis_url = redis_url

    async def post_to_queue(self, queue_name: str, data: dict):
        redis = await aioredis.from_url(self.redis_url)
        try:
            json_data = json.dumps(data)
            await redis.rpush(queue_name, json_data)
        finally:
            await redis.close()

