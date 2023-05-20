"""An account in the schema"""
import enum
from datetime import date
from typing import Final, Optional

from sqlalchemy import Date
from sqlalchemy import Enum, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class AccountStatusEnum(enum.Enum):
    active = "ACTIVE"
    closed = "CLOSED"
    frozen = "FROZEN"


class Account(Base):
    """A customer in the schema"""

    __tablename__: Final[str] = "account"

    account_id: Mapped[int] = mapped_column(primary_key=True)

    product_cd: Mapped[str] = mapped_column(
        ForeignKey("product.product_cd"), nullable=False
    )

    cust_id: Mapped[int] = mapped_column(ForeignKey("customer.cust_id"), nullable=False)

    open_date: Mapped[date] = mapped_column(Date, nullable=False)
    """Open date of the account, non-nullable"""

    close_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    """Close date of the account, nullable if not closed"""

    last_activity_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    """Last activity date of the account, nullable means use open date"""

    status: Mapped[Optional[str]] = mapped_column(
        Enum(AccountStatusEnum), nullable=True
    )

    open_emp_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("employee.emp_id"), nullable=True
    )

    open_branch_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("branch.branch_id"), nullable=True
    )

    avail_balance: Mapped[Optional[float]] = mapped_column(
        Float(precision=10), nullable=True
    )

    pending_balance: Mapped[Optional[float]] = mapped_column(
        Float(precision=10), nullable=True
    )

    def __repr__(self) -> str:
        return (
            "Account(account_id=%d, product_cd=%s, cust_id=%d, open_date=%s, close_date=%s"
            ", last_activity_date=%s, status=%s, open_emp_id=%s, open_branch_id=%s"
            ", avail_balance=%s, pending_balance=%s)"
        ) % (
            self.account_id,
            self.product_cd,
            self.cust_id,
            self.open_date.isoformat(),
            self.close_date.isoformat() if self.close_date is not None else "",
            self.last_activity_date.isoformat()
            if self.last_activity_date is not None
            else "",
            self.status if self.status is not None else "",
            str(self.open_emp_id) if self.open_emp_id is not None else "",
            str(self.open_branch_id) if self.open_branch_id is not None else "",
            str(round(self.avail_balance, 2)) if self.avail_balance is not None else "",
            str(round(self.pending_balance, 2))
            if self.pending_balance is not None
            else "",
        )
