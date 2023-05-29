"""An officer customer of the bank"""
from datetime import date
from typing import Final, Optional

from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Officer(Base):
    """An officer customer of the bank"""

    __tablename__: Final[str] = "officer"
    """Table name for the associated object"""

    officer_id: Mapped[int] = mapped_column(primary_key=True)
    """Officer ID, primary key"""

    cust_id: Mapped[int] = mapped_column(ForeignKey("customer.cust_id"), nullable=False)
    """Customer ID, foreign key"""

    fname: Mapped[str] = mapped_column(String(30), nullable=False)
    """First name of the officer, non-nullable"""

    lname: Mapped[str] = mapped_column(String(30), nullable=False)
    """Last name of the officer, non-nullable"""

    title: Mapped[str] = mapped_column(String(20), nullable=True)
    """Title of the officer, nullable"""

    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    """Start date of the employee, non-nullable"""

    end_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    """End date of the employee, nullable if still employed"""

    officer_customer: Mapped["Customer"] = relationship(
        "Customer", back_populates="customer_officer"
    )

    def __repr__(self) -> str:
        return (
            "Officer(officer_id=%d, cust_id=%s, fname=%s, lname=%s, title=%s, start_date=%s, end_date=%s)"
            % (
                self.officer_id,
                self.cust_id,
                self.fname,
                self.lname,
                self.title if self.title is not None else "",
                self.start_date.isoformat(),
                self.end_date.isoformat() if self.end_date is not None else "",
            )
        )
