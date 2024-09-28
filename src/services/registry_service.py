from datetime import datetime, timedelta
import logging
import uuid

from http import HTTPStatus

from src.models.general_response import GeneralResponse
from src.models.schemas.company_registry_schema import CompanyRegistrySchema
from src.models.schemas.registry_schema import RegistrySchema
from src.models.schemas.user_registry_schema import UserRegistrySchema
from src.services.mongo.mongo_service import MongoService
from src.services.rabbit_mq.rabbit_mq_service import RabbitMQService
from config.configs import settings

class RegistryService:
    def __init__(self, mongo_service:MongoService, rabbit_mq_service:RabbitMQService):
        self.mongo_service = mongo_service
        self.rabbit_mq_service = rabbit_mq_service
        logging.basicConfig(level=logging.INFO)

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
            self.mongo_service.insert_schema(registry_content)
        except Exception as e:
            return GeneralResponse(
                status=HTTPStatus.INTERNAL_SERVER_ERROR,
                message="Error when posting on Mongo",
                info=e
            )

        try:
            logging.info("Posting new registry request to RabbitMQ Queue")
            self.rabbit_mq_service.post_to_queue(queue_name=settings.RABBIT_MQ_REGISTRY_QUEUE, data={"key":key})
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