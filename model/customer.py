"""A generalized customer of the bank, either an individual or business"""
import enum
from typing import Final, Optional, List

from sqlalchemy import String, Enum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class CustomerTypeEnum(enum.Enum):
    """Customer type as either individual 'I' or business 'B'"""

    I = "I"
    """Individual customer of the bank"""

    B = "B"
    """Business customer of the bank"""


class Customer(Base):
    """A generalized customer of the bank, either an individual or business"""

    __tablename__: Final[str] = "customer"
    """Table name for the associated object"""

    cust_id: Mapped[int] = mapped_column(primary_key=True)
    """Customer ID, primary key"""

    fed_id: Mapped[str] = mapped_column(String(12), nullable=False)
    """Federal ID of the customer, nullable if not available"""

    cust_type_cd: Mapped[CustomerTypeEnum] = mapped_column(
        Enum(CustomerTypeEnum), nullable=False
    )
    """Customer type code, individual or business, non-nullable"""

    address: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    """Address of the customer, nullable"""

    city: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    """City of the branch, nullable"""

    state: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    """State of the branch, nullable"""

    postal_code: Mapped[Optional[str]] = mapped_column(String(10), nullable=True)
    """postal code of the branch, nullable"""

    customer_accounts: Mapped[List["Account"]] = relationship(
        "Account", back_populates="account_customer"
    )
    """Pointer to a list of all the Accounts held by the customer"""

    customer_officer: Mapped[Optional["Officer"]] = relationship(
        "Officer", back_populates="officer_customer"
    )
    """Pointer to an officer, if exists. Else none"""

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
