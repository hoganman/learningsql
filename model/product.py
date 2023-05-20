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

    product_type_cd: Mapped[str] = mapped_column(ForeignKey("product_type.product_type_cd"), nullable=False)

    date_offered: Mapped[date] = mapped_column(Date, nullable=True)
    """Offering date of the product, nullable"""

    date_retired: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    """Retiring date of the product, nullable"""
