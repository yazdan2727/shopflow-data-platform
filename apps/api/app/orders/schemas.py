from decimal import Decimal

from pydantic import BaseModel, Field

from app.orders.enums import OrderStatus


class OrderItemCreate(BaseModel):
    product_id: str

    quantity: int = Field(
        gt=0,
    )


class OrderCreate(BaseModel):
    items: list[OrderItemCreate]


class OrderItemResponse(BaseModel):
    product_id: str
    quantity: int
    unit_price: Decimal


class OrderResponse(BaseModel):
    id: str
    user_id: str
    total_amount: Decimal
    status: OrderStatus
    items: list[OrderItemResponse]