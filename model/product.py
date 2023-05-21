"""A product offered by the bank"""
from datetime import date
from typing import Final, Optional

from sqlalchemy import String, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Product(Base):
    """A product offered by the bank"""

    __tablename__: Final[str] = "product"

    product_cd: Mapped[str] = mapped_column(String(10), primary_key=True)

    name: Mapped[str] = mapped_column(String(50), nullable=False)

    product_type_cd: Mapped[str] = mapped_column(
        ForeignKey("product_type.product_type_cd"), nullable=False
    )

    date_offered: Mapped[date] = mapped_column(Date, nullable=True)
    """Offering date of the product, nullable"""

    date_retired: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    """Retiring date of the product, nullable"""

    def __repr__(self) -> str:
        return (
            "Product(product_cd=%s, name=%s, product_type_cd=%s"
            ", date_offered=%s, date_retired=%s)"
        ) % (
            self.product_cd,
            self.name,
            self.product_type_cd,
            self.date_offered.isoformat() if self.date_offered is not None else "",
            self.date_retired.isoformat() if self.date_retired is not None else ""
        )
