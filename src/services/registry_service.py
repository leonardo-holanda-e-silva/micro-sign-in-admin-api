from datetime import datetime, timedelta
import logging
import uuid

from http import HTTPStatus

from src.models.general_response import GeneralResponse
from src.models.schemas.company_registry_schema import CompanyRegistrySchema
from src.models.schemas.registry_schema import RegistrySchema
from src.models.schemas.user_registry_schema import UserRegistrySchema
from src.services.rabbit_mq.rabbit_mq_service import RabbitMQService
from src.services.redis.redis_service import RedisService
from config.configs import settings

redis_service = RedisService(settings.REDIS_URL)
rabbit_mq_service = RabbitMQService(settings.RABBIT_MQ_URL_URL)
logging.basicConfig(level=logging.INFO)

class RegistryService:
    def init_registration(self, schema:RegistrySchema) -> GeneralResponse:
        key = uuid.uuid4()
        expire = datetime.now() + timedelta(minutes=45)
        logging.info(f"Starting new registry request. \nUser: {schema.user_name} - Key: {key}")

        registry_content = {
            "key":key,
            "user_name":schema.user_name,
            "email":schema.email,
            "company_name":schema.company_name,
            "step":"start",
            "expire": expire
        }

        try:
            logging.info("Posting new registry request to Redis")
            redis_service.post_to_queue(queue_name=settings.REDIS_REGISTRY_COLLECTION, data=registry_content)
        except Exception as e:
            return GeneralResponse(
                status=HTTPStatus.INTERNAL_SERVER_ERROR,
                message="Error when posting on Redis",
                info=e
            )

        try:
            logging.info("Posting new registry request to RabbitMQ Queue")
            rabbit_mq_service.post_to_queue(queue_name=settings.RABBIT_MQ_REGISTRY_QUEUE, data={"key":key})
        except Exception as e:
            return GeneralResponse(
                status=HTTPStatus.INTERNAL_SERVER_ERROR,
                message="Error when posting on Rabbit",
                info=e
            )

        return GeneralResponse(
            status=HTTPStatus.CREATED,
            message="Request created successfully",
            info=str(key)
        )

    def user_registration(self, schema: UserRegistrySchema, key:str) -> GeneralResponse:
        pass

    def company_registration(self, schema: CompanyRegistrySchema, key:str) -> GeneralResponse:
        pass