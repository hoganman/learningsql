"""A product type for the bank"""
from typing import Final, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class ProductType(Base):
    """A product type for the bank"""

    __tablename__: Final[str] = "product_type"
    """Table name for the associated object"""

    product_type_cd: Mapped[str] = mapped_column(String(10), primary_key=True)
    """Product type code, primary key"""

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    """Name of the product type, non-nullable"""

    product_type_products: Mapped[List["Product"]] = relationship(
        "Product", back_populates="product_product_type"
    )
    """A pointer to all products associated with the product type"""

    def __repr__(self) -> str:
        return "ProductType(product_type_cd=%s, name=%s)" % (
            self.product_type_cd,
            self.name,
        )
