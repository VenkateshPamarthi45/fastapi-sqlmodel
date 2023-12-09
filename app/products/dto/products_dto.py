from sqlmodel import SQLModel


class ProductsDTO(SQLModel):
	name: str

