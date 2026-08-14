import uuid
from decimal import Decimal

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.products.models import Product
from app.products.repository import ProductRepository
from app.products.schemas import ProductCreate


class ProductService:

    def __init__(self):
        self.repository = ProductRepository()

    def create_product(
        self,
        db: Session,
        product_data: ProductCreate,
    ) -> Product:

        product = Product(
            id=str(uuid.uuid4()),
            name=product_data.name,
            description=product_data.description,
            price=product_data.price,
            stock=product_data.stock,
        )

        return self.repository.create(
            db,
            product,
        )

    def get_product(
        self,
        db: Session,
        product_id: str,
    ) -> Product:

        product = self.repository.get_by_id(
            db,
            product_id,
        )

        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )

        return product

    def list_products(
        self,
        db: Session,
    ) -> list[Product]:
        return self.repository.list(db)