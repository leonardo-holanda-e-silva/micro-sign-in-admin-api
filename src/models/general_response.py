from http import HTTPStatus

class GeneralResponse:
    def __init__(self, status : HTTPStatus, message : str, info : any):
        self.status : HTTPStatus = status
        self.message : str = message
        self.info : info