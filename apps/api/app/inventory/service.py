from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from app.inventory.models import Inventory
from app.inventory.repository import InventoryRepository
from app.inventory.schemas import InventoryCreate
from app.products.repository import ProductRepository


class InventoryService:

    def __init__(self):
        self.repository = InventoryRepository()
        self.product_repository = ProductRepository()

    def create_inventory(
        self,
        db: Session,
        data: InventoryCreate,
    ) -> Inventory:

        product = self.product_repository.get_by_id(
            db,
            data.product_id,
        )

        if product is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Product not found",
            )

        existing = self.repository.get_by_product_id(
            db,
            data.product_id,
        )

        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Inventory already exists for this product",
            )

        inventory = Inventory(
            product_id=data.product_id,
            available_quantity=data.available_quantity,
            reserved_quantity=0,
        )

        return self.repository.create(
            db,
            inventory,
        )