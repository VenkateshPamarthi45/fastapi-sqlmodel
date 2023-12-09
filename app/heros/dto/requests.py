from pydantic import BaseModel


class HeroRequest(BaseModel):
    name: str
    description: str
    price: int
