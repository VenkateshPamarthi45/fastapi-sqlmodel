from fastapi import Depends, HTTPException

from app.products.dto.products_dto import ProductsDTO
from app.products.repository.products_repository import ProductsRepository


class ProductsService:

	def __init__(self, repo: ProductsRepository = Depends(ProductsRepository)):
		self.repo = repo

	def get_products_by_id(self, products_id):
		try:
			return self.repo.get_products_by_id(products_id)
		except:
			raise HTTPException(404, "No products found")

	def create_products(self, products_dto: ProductsDTO):
		return self.repo.create_products(products_dto)

	def get_all_products(self):
		try:
			return self.repo.get_all_products()
		except:
			raise HTTPException(404, "No products found")

