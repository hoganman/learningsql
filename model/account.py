"""An account in the schema"""
from typing import Final, Optional

from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Account(Base):
    """A customer in the schema"""

    __tablename__: Final[str] = "account"

    account_id: Mapped[int] = mapped_column(primary_key=True)

    product_cd: Mapped[str] = mapped_column(String(12), nullable=False)

    cust_type_cd: Mapped[str] = mapped_column(Enum(CustomerTypeEnum), nullable=False)

    address: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    """Address of the customer, nullable"""

    city: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    """City of the branch, nullable"""

    state: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    """State of the branch, nullable"""

    postal_code: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    """postal code of the branch, nullable"""
