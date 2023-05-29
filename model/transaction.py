"""A transaction with the bank"""
import enum
from datetime import datetime
from typing import Final, Optional

from sqlalchemy import Enum, DateTime, ForeignKey, Double
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class TransactionTypeEnum(enum.Enum):
    """Transaction type as either credit 'CDT' or debit 'DBT'"""

    CDT = "CDT"
    """Credit type transition"""

    DBT = "DBT"
    """Debit type transaction"""


class Transaction(Base):
    """A transaction with the bank"""

    __tablename__: Final[str] = "transaction"
    """Table name for the associated object"""

    txn_id: Mapped[int] = mapped_column(primary_key=True)
    """Transaction ID, primary key"""

    txn_date: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    """Transaction datetime, non-nullable"""

    account_id: Mapped[int] = mapped_column(
        ForeignKey("account.account_id"), nullable=False
    )
    """Associated account with the transaction, foreign key, non-nullable"""

    txn_type_cd: Mapped[TransactionTypeEnum] = mapped_column(
        Enum(TransactionTypeEnum), nullable=True
    )
    """Transaction type enumerated code, nullable"""

    amount: Mapped[float] = mapped_column(Double, nullable=False)
    """Transaction amount, non-nullable"""

    teller_emp_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("employee.emp_id"), nullable=True
    )
    """Teller associated with the transaction, nullable if not an employee"""

    execution_branch_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("branch.branch_id"), nullable=True
    )
    """Branch ID where the transaction was executed, nullable if not at a branch"""

    funds_avail_date: Mapped[Optional[datetime]] = mapped_column(
        DateTime, nullable=True
    )
    """Date when funds are available, nullable if transaction does not apply"""

    transaction_account: Mapped["Account"] = relationship(
        "Account", back_populates="account_transactions"
    )
    """Pointer to the account associated with the transaction"""

    transaction_teller: Mapped[Optional["Employee"]] = relationship(
        "Employee", back_populates="employee_transactions"
    )
    """Pointer to the employee who completed the transaction, else None if not an employee"""

    transaction_branch: Mapped[Optional["Branch"]] = relationship(
        "Branch", back_populates="branch_transactions"
    )
    """Pointer to the branch that executed the transaction, else None if not at a branch"""

    def __repr__(self) -> str:
        return (
            "Transaction(txn_id=%d, txn_date=%s, account_id=%d, txn_type_cd=%s"
            ", amount=%10.2f, teller_emp_id=%s, execution_branch_id=%s"
            ", funds_avail_date=%s)"
        ) % (
            self.txn_id,
            self.txn_date.isoformat(),
            self.account_id,
            str(self.txn_type_cd.value),
            self.amount,
            str(self.teller_emp_id) if self.teller_emp_id is not None else "",
            str(self.execution_branch_id)
            if self.execution_branch_id is not None
            else "",
            self.funds_avail_date.isoformat()
            if self.funds_avail_date is not None
            else "",
        )
