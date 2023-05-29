"""A business customer for the bank"""
from datetime import date
from typing import Final, Optional

from sqlalchemy import String, ForeignKey, Date
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class Business(Base):
    """A business customer for the bank"""

    __tablename__: Final[str] = "business"
    """Table name for the associated object"""

    cust_id: Mapped[int] = mapped_column(
        ForeignKey("customer.cust_id"), primary_key=True
    )
    """ID of the business customer, primary key"""

    name: Mapped[str] = mapped_column(String(40), nullable=False)
    """Name of the business, non-nullable"""

    state_id: Mapped[str] = mapped_column(String(10), nullable=False)
    """State ID of the business, non-nullable"""

    incorp_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    """Incorporation date of the business, nullable"""

    def __repr__(self) -> str:
        return "Business(cust_id=%d, name=%s, state_id=%s, incorp_date=%s)" % (
            self.cust_id,
            self.name,
            self.state_id,
            self.incorp_date.isoformat() if self.incorp_date is not None else "",
        )
