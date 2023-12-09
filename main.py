from pprint import pprint

from fastapi import FastAPI
from app.heros import hero
from app.users import users_router

app = FastAPI()
app.include_router(hero.router, prefix="/v1/heros")
app.include_router(users_router.router, prefix="/v1/users")


@app.get("/index")
def index():
    return {"message": "welcome Venky"}