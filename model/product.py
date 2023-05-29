"""A product offered by the bank"""
from datetime import date
from typing import Final, Optional, List

from sqlalchemy import String, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Product(Base):
    """A product offered by the bank"""

    __tablename__: Final[str] = "product"
    """Table name for the associated object"""

    product_cd: Mapped[str] = mapped_column(String(10), primary_key=True)
    """Product code for the product, primary key"""

    name: Mapped[str] = mapped_column(String(50), nullable=False)
    """Name of the product, non-nullable"""

    product_type_cd: Mapped[str] = mapped_column(
        ForeignKey("product_type.product_type_cd"), nullable=False
    )
    """Product type code, foreign key to product_type table, non-nullable"""

    date_offered: Mapped[date] = mapped_column(Date, nullable=True)
    """Offering date of the product, nullable"""

    date_retired: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    """Retiring date of the product, nullable"""

    product_accounts: Mapped[List["Account"]] = relationship(
        "Account", back_populates="account_product"
    )
    """Pointer to all accounts associated with the product"""

    product_product_type: Mapped["ProductType"] = relationship(
        "ProductType", back_populates="product_type_products"
    )
    """Pointer to the product type associated with the product"""

    def __repr__(self) -> str:
        return (
            "Product(product_cd=%s, name=%s, product_type_cd=%s"
            ", date_offered=%s, date_retired=%s)"
        ) % (
            self.product_cd,
            self.name,
            self.product_type_cd,
            self.date_offered.isoformat() if self.date_offered is not None else "",
            self.date_retired.isoformat() if self.date_retired is not None else "",
        )
