"""An account of the bank"""
import enum
from datetime import date
from typing import Final, Optional

from sqlalchemy import Date
from sqlalchemy import Enum, ForeignKey, Float
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class AccountStatusEnum(enum.Enum):
    """Account status values"""

    ACTIVE = "ACTIVE"
    """Account is open and active"""

    CLOSED = "CLOSED"
    """Account is closed and inactive"""

    FROZEN = "FROZEN"
    """Account has been frozen due to something"""


class Account(Base):
    """An account of the bank, held by a single customer"""

    __tablename__: Final[str] = "account"
    """Table name for the associated object"""

    account_id: Mapped[int] = mapped_column(primary_key=True)
    """Account ID, primary key"""

    product_cd: Mapped[str] = mapped_column(
        ForeignKey("product.product_cd"), nullable=False
    )
    """The product code, foreign key to a product's code, nullable"""

    cust_id: Mapped[int] = mapped_column(ForeignKey("customer.cust_id"), nullable=False)
    """Customer ID, foreign key to a customer's ID"""

    open_date: Mapped[date] = mapped_column(Date, nullable=False)
    """Open date of the account, non-nullable"""

    close_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    """Close date of the account, nullable if not closed"""

    last_activity_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    """Last activity date of the account, nullable means use open date"""

    status: Mapped[Optional[AccountStatusEnum]] = mapped_column(
        Enum(AccountStatusEnum), nullable=True
    )
    """Status of the account, nullable if undefined"""

    open_emp_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("employee.emp_id"), nullable=True
    )
    """Employee's ID who opened the account, foreign key to an employee's ID"""

    open_branch_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("branch.branch_id"), nullable=True
    )
    """Branch's ID where the account was opened, foreign key to a branch's ID"""

    avail_balance: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    """Available balance of the account, nullable if no activity"""

    pending_balance: Mapped[Optional[float]] = mapped_column(Float, nullable=True)
    """"Pending balance of the account, nullable if no activity"""

    account_customer: Mapped["Customer"] = relationship(
        "Customer", back_populates="customer_accounts"
    )
    """A pointer to the Customer of the account"""

    account_product: Mapped["Product"] = relationship(
        "Product", back_populates="product_accounts"
    )
    """A pointer to the account's Product"""

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
            str(self.status.value) if self.status is not None else "",
            str(self.open_emp_id) if self.open_emp_id is not None else "",
            str(self.open_branch_id) if self.open_branch_id is not None else "",
            str(round(self.avail_balance, 2)) if self.avail_balance is not None else "",
            str(round(self.pending_balance, 2))
            if self.pending_balance is not None
            else "",
        )
