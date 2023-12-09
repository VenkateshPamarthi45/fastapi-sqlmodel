from fastapi import Depends
from sqlmodel import Session

from app.common.db.session import get_db
from app.heros.data.hero import Hero


class HeroRepository:

    def __init__(self, db: Session = Depends(get_db)):
        self.db = db

    def create_hero(self, name: str, description: str, price: int):
        hero = Hero(name=name, description=description, price=price)
        self.db.add(hero)
        self.db.commit()
        self.db.refresh(hero)
        return hero

    def get_heros(self):
        return self.db.query(Hero)

    def get_hero(self, hero_id=int):
        return self.db.query(Hero).filter(Hero.id == hero_id).one()
