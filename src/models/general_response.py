from pydantic import BaseModel, Field
from http import HTTPStatus


class GeneralResponse(BaseModel):
    status: int = Field(..., description="HTTP status code")
    message: str = Field(..., description="Response message")
    info: dict = Field(None, description="Additional information")

    @classmethod
    def from_http_status(cls, status: HTTPStatus, message: str, info: dict = None):
        return cls(status=status.value, message=message, info=info)
