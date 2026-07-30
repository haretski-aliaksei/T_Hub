from pydantic import BaseModel, Field

from constants.api.products.constraints import (
    MAX_DISCOUNT_PERCENTAGE,
    MAX_PRODUCT_RATING,
    MIN_DISCOUNT_PERCENTAGE,
    MIN_PRODUCT_PRICE,
    MIN_PRODUCT_RATING,
    MIN_PRODUCT_STOCK,
)


class Product(BaseModel):
    id: int
    title: str = Field(min_length=1)
    category: str = Field(min_length=1)
    price: float = Field(ge=MIN_PRODUCT_PRICE)
    stock: int = Field(ge=MIN_PRODUCT_STOCK)
    rating: float = Field(ge=MIN_PRODUCT_RATING, le=MAX_PRODUCT_RATING)
    discountPercentage: float = Field(
        ge=MIN_DISCOUNT_PERCENTAGE, le=MAX_DISCOUNT_PERCENTAGE
    )
