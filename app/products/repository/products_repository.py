from fastapi import Depends
from sqlmodel import Session, select
from app.common.db.session import get_db
from app.products.dto.products_dto import ProductsDTO
from app.common.repo.sql_repo import SQLRepository
from app.products.data.products import Products


class ProductsRepository(SQLRepository):

	def __init__(self, db: Session = Depends(get_db)):
		super().__init__(Products, db)

	def get_products_by_id(self, products_id):
		return self.get_entity_by_id(products_id)

	def create_products(self, products_dto: ProductsDTO):
		products = Products(name=products_dto.name)
		return self.create_entity(products)

	def get_all_products(self):
		return self.get_all_entities()

