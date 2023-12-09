from fastapi import APIRouter, Depends
from app.products.data.products import Products
from app.products.dto.products_dto import ProductsDTO
from app.products.service.products_service import ProductsService

router = APIRouter()


@router.get("/products_id", response_model=Products)
def get_products_by_id(products_id: str, service: ProductsService = Depends(ProductsService)):
	return service.get_products_by_id(products_id=products_id)


@router.post("", response_model=Products)
def create_products(products_dto: ProductsDTO, service: ProductsService = Depends(ProductsService)):
	return service.create_products(products_dto)


@router.get("", response_model=list[Products])
def get_all_products(service: ProductsService = Depends(ProductsService)):
	return service.get_all_products()


