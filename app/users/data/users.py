from typing import Optional
from sqlmodel import SQLModel, Field 


class Users(SQLModel, table=True):
	__tablename__ = "user"
	id: Optional[int] = Field(default=None, primary_key=True)
	name: str
	email: str
	age: int
