from fastapi import APIRouter, Depends, status
from sqlalchemy.orm import Session

from app.auth.dependencies import get_current_user
from app.auth.dependencies import require_admin
from app.db.dependencies import get_db
from app.inventory.schemas import (
    InventoryCreate,
    InventoryResponse,
)
from app.inventory.service import InventoryService
from app.users.models import User


router = APIRouter(
    prefix="/inventory",
    tags=["Inventory"],
)

service = InventoryService()


@router.post(
    "",
    response_model=InventoryResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_inventory(
    data: InventoryCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin),
):
    return service.create_inventory(
        db,
        data,
    )


@router.get(
    "/product/{product_id}",
    response_model=InventoryResponse,
)
def get_product_inventory(
    product_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user),
):
    return service.get_by_product_id(
        db,
        product_id,
    )