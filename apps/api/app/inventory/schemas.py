from pydantic import BaseModel, ConfigDict, Field


class InventoryCreate(BaseModel):
    product_id: str

    available_quantity: int = Field(
        ge=0,
    )


class InventoryResponse(BaseModel):
    id: str
    product_id: str
    available_quantity: int
    reserved_quantity: int

    model_config = ConfigDict(
        from_attributes=True,
    )