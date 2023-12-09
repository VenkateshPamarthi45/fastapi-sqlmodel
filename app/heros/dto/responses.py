class HeroResponse:
    id: str
    name: str
    description: str
    price: int

    def __init__(self, hero_id, name, description, price):
        self.name = name
        self.description = description
        self.price = price
