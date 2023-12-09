import json

from fastapi import Depends
from sqlmodel import Session, select
from app.common.db.session import get_db
from app.common.repo.sql_repo import SQLRepository
from app.users.data.users import Users
from app.users.dto.users_dto import UsersDTO


class UsersRepository(SQLRepository):

	def __init__(self, db: Session = Depends(get_db)):
		super().__init__(Users, db)

	def get_users_by_id(self, users_id):
		return self.get_entity_by_id(users_id)

	def create_users(self, users_dto: UsersDTO):
		users = Users(name=users_dto.name, email=users_dto.email, age=users_dto.age)
		return self.create_entity(users)

	def get_all_users(self):
		return self.get_all_entities()

