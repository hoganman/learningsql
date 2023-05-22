"""A customer in the schema"""
import enum
from typing import Final, Optional

from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class CustomerTypeEnum(enum.Enum):
    """Customer type as either individual 'I' or business 'B'"""

    I = "I"
    B = "B"


class Customer(Base):
    """A customer in the schema"""

    __tablename__: Final[str] = "customer"

    cust_id: Mapped[int] = mapped_column(primary_key=True)

    fed_id: Mapped[str] = mapped_column(String(12), nullable=False)

    cust_type_cd: Mapped[CustomerTypeEnum] = mapped_column(Enum(CustomerTypeEnum), nullable=False)

    address: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    """Address of the customer, nullable"""

    city: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    """City of the branch, nullable"""

    state: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    """State of the branch, nullable"""

    postal_code: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    """postal code of the branch, nullable"""

    def __repr__(self) -> str:
        return (
            "Customer(cust_id=%d, fed_id=%s, cust_type_cd=%s, address=%s"
            ", city=%s, state=%s, postal_code=%s)"
        ) % (
            self.cust_id,
            self.fed_id,
            str(self.cust_type_cd.value),
            self.address if self.address is not None else "",
            self.city if self.city is not None else "",
            self.state if self.state is not None else "",
            self.postal_code if self.postal_code is not None else "",
        )
