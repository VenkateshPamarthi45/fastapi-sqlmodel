from sqlmodel import SQLModel


class UsersDTO(SQLModel):
	name: str
	email: str
	age: int
