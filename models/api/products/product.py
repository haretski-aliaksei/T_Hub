from pydantic import BaseModel, Field

from constants.api.products.constraints import MIN_PRODUCT_PRICE


class Product(BaseModel):
    id: int
    title: str = Field(min_length=1)
    category: str = Field(min_length=1)
    price: float = Field(ge=MIN_PRODUCT_PRICE)
