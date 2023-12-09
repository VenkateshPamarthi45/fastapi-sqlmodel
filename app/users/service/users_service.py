from fastapi import Depends, HTTPException

from app.users.dto.users_dto import UsersDTO
from app.users.repository.users_repository import UsersRepository


class UsersService:

	def __init__(self, repo: UsersRepository = Depends(UsersRepository)):
		self.repo = repo

	def get_users_by_id(self, users_id):
		try:
			return self.repo.get_users_by_id(users_id)
		except:
			raise HTTPException(404, "No users found")

	def create_users(self, users_dto: UsersDTO):
		return self.repo.create_users(users_dto)

	def get_all_users(self):
		try:
			return self.repo.get_all_users()
		except:
			raise HTTPException(404, "No users found")

