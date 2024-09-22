import json

import aio_pika
from aio_pika import Message

class RabbitMQService:
    def __init__(self, rabbitmq_url: str):
        self.rabbitmq_url = rabbitmq_url

    async def post_to_queue(self, queue_name: str, data: dict):
        connection = await aio_pika.connect_robust(self.rabbitmq_url)
        try:
            async with connection.channel() as channel:
                queue = await channel.declare_queue(queue_name, durable=True)

                json_data = json.dumps(data)

                message = Message(json_data.encode())
                await channel.default_exchange.publish(message, routing_key=queue_name)
        finally:
            await connection.close()