from fastapi import FastAPI
import uvicorn

from config.configs import settings
from src.services.mongo.mongo_service import MongoService
from src.services.rabbit_mq.rabbit_mq_service import RabbitMQService
from src.services.registry_service import RegistryService
from src.controllers.registry_controller import RegistryController

app = FastAPI()

#Registry Domain
mongo_service = MongoService(settings.MONGO_DB_URL, settings.MONGO_DB_REGISTRY_COLLECTION)
rabbit_mq_service = RabbitMQService(settings.RABBIT_MQ_URL)
registry_service = RegistryService(mongo_service, rabbit_mq_service)

registry_controller = RegistryController(mongo_service, registry_service)
app.include_router(registry_controller.router)

@app.get("/")
def read_root():
    return {"message": "API is running"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
