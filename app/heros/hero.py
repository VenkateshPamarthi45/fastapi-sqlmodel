from fastapi import APIRouter, Depends
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.exceptions import HTTPException
from starlette.responses import JSONResponse

from app.heros.data.hero import Hero
from app.heros.errors.custom_exceptions import HeroNotFoundException
from app.heros.dto.requests import HeroRequest
from app.heros.service.hero_service import HeroService

router = APIRouter()


@router.get("/{hero_id}", response_model=Hero)
def get_hero(hero_id: str, handler=Depends(HeroService)):
    return handler.get_hero_detail(hero_id)


@router.get("", response_model=list[Hero])
def get_all_hero(service=Depends(HeroService)):
    return service.get_all_heros()


@router.post("", response_model=Hero)
def create_hero(heroRequest: HeroRequest, handler=Depends(HeroService)):
    hero = handler.new_hero(heroRequest)
    if isinstance(hero, str):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=hero)
    else:
        return JSONResponse(
            status_code=status.HTTP_200_OK, content=jsonable_encoder(hero)
        )
