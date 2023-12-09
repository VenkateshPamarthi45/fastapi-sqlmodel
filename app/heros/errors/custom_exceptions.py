from fastapi import HTTPException


class HeroNotFoundException(HTTPException):
    status_code: int
    message: str

    def __init__(self):
        self.status_code = 404
        self.message = "Product Not found"
