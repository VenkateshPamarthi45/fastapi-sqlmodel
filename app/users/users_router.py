from fastapi import APIRouter, Depends
from app.users.data.users import Users
from app.users.dto.users_dto import UsersDTO
from app.users.service.users_service import UsersService

router = APIRouter()


@router.get("/{users_id}", response_model=Users)
def get_users_by_id(users_id: str, service: UsersService = Depends(UsersService)):
	return service.get_users_by_id(users_id=users_id)


@router.post("", response_model=Users)
def create_users(users_dto: UsersDTO, service: UsersService = Depends(UsersService)):
	return service.create_users(users_dto)


@router.get("", response_model=list[Users])
def get_all_users(service: UsersService = Depends(UsersService)):
	return service.get_all_users()


