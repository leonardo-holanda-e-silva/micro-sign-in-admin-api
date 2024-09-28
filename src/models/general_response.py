from http import HTTPStatus


class GeneralResponse:
    def __init__(self, status:HTTPStatus, message:str, info: any ):
        self.status = status
        self.message = message
        self.info = info