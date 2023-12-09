from fastapi import Depends, HTTPException
from app.heros.dto.requests import HeroRequest
from app.heros.repository.hero_repository import HeroRepository


class HeroService:
    def __init__(self, repo=Depends(HeroRepository)):
        self.repo = repo

    def get_hero_detail(self, hero_id):
        if hero_id is None:
            return "Id is empty"
        else:
            try:
                return self.repo.get_hero(hero_id)
            except:
                raise HTTPException(404, "not found")

    def new_hero(self, hero_request: HeroRequest):
        if len(hero_request.name) == 0:
            return "Name is empty"
        elif len(hero_request.description) == 0:
            return "Description is empty"
        elif hero_request.price <= 0:
            return "Price is less than equal to 0"
        else:
            hero = self.repo.create_hero(
                name=hero_request.name,
                description=hero_request.description,
                price=hero_request.price,
            )
            return hero

    def get_all_heros(self):
        return self.repo.get_heros()
