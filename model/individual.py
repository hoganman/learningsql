"""An employee in a department model"""
from datetime import date
from typing import Final, Optional, List

from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Individual(Base):
    """An individual customer"""

    __tablename__: Final[str] = "individual"

    cust_id: Mapped[int] = mapped_column(
        ForeignKey("customer.cust_id"), primary_key=True
    )
    """Individual ID, primary key and foreign key to customer ID"""

    fname: Mapped[str] = mapped_column(String(30), nullable=False)
    """First name of the employee, non-nullable"""

    lname: Mapped[str] = mapped_column(String(30), nullable=False)
    """Last name of the employee, non-nullable"""

    birth_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    """Start date of the employee, non-nullable"""

    def __repr__(self) -> str:
        return "Individual(cust_id=%s, fname=%s, lname=%s, birthdate=%s)" % (
            self.cust_id,
            self.fname,
            self.lname,
            self.birth_date.isoformat() if self.birth_date is not None else "",
        )
