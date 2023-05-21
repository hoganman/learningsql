"""A product type for the bank"""

from typing import Final

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class ProductType(Base):
    """A product type for the bank"""

    __tablename__: Final[str] = "product_type"

    product_type_cd: Mapped[str] = mapped_column(String(10), primary_key=True)

    name: Mapped[str] = mapped_column(String(50), nullable=False)

    def __repr__(self) -> str:
        return "ProductType(product_type_cd=%s, name=%s)" % (
            self.product_type_cd,
            self.name
        )
