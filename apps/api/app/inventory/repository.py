from sqlalchemy.orm import Session

from app.inventory.models import Inventory


class InventoryRepository:

    def create(
        self,
        db: Session,
        inventory: Inventory,
    ) -> Inventory:
        db.add(inventory)
        db.commit()
        db.refresh(inventory)

        return inventory

    def get_by_product_id(
        self,
        db: Session,
        product_id: str,
    ) -> Inventory | None:
        return (
            db.query(Inventory)
            .filter(
                Inventory.product_id == product_id
            )
            .first()
        )

    def get_by_id(
        self,
        db: Session,
        inventory_id: str,
    ) -> Inventory | None:
        return (
            db.query(Inventory)
            .filter(
                Inventory.id == inventory_id
            )
            .first()
        )