from typing import Optional
from sqlmodel import SQLModel, Field 


class Products(SQLModel, table=True):
	__tablename__ = "products"
	id: Optional[int] = Field(default=None, primary_key=True)
	name: str
