"""A transaction with the bank"""
import enum
from datetime import datetime
from typing import Final, Optional

from sqlalchemy import String, Enum, DateTime, ForeignKey, Double
from sqlalchemy.orm import Mapped, mapped_column

from .base import Base


class TransactionTypeEnum(enum.Enum):
    """Transaction type as either credit 'CDT' or debit 'DBT'"""

    credit = "CDT"
    debit = "DBT"


class Transaction(Base):
    """A transaction with the bank"""

    __tablename__: Final[str] = "transactions"

    txn_id: Mapped[int] = mapped_column(primary_key=True)

    txn_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    """Transaction datetime, non-nullable"""

    account_id: Mapped[int] = mapped_column(
        ForeignKey("account.account_id"), nullable=False
    )

    txn_type_cd: Mapped[str] = mapped_column(Enum(TransactionTypeEnum), nullable=True)

    amount: Mapped[float] = mapped_column(Double(10), nullable=False)

    teller_emp_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("employee.emp_id"), nullable=True
    )

    execution_branch_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("branch.branch_id"), nullable=True
    )

    funds_avail_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True
    )
