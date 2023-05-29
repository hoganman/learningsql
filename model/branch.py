"""A department branch of the bank"""
from typing import Final, Optional, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Branch(Base):
    """A department branch of the bank"""

    __tablename__: Final[str] = "branch"
    """Table name for the associated object"""

    branch_id: Mapped[int] = mapped_column(primary_key=True)
    """Branch ID, primary key"""

    name: Mapped[str] = mapped_column(String(20), nullable=False)
    """Name of the branch, non-nullable"""

    address: Mapped[Optional[str]] = mapped_column(String(30), nullable=True)
    """Address of the branch, nullable"""

    city: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    """City of the branch, nullable"""

    state: Mapped[Optional[str]] = mapped_column(String(2), nullable=True)
    """State of the branch, nullable"""

    zip: Mapped[Optional[str]] = mapped_column(String(12), nullable=True)
    """ZIP code of the branch, nullable"""

    branch_employees: Mapped[List["Employee"]] = relationship(
        "Employee", back_populates="employee_branch"
    )
    """Relationship that lists all the employee with the branch"""

    def __repr__(self) -> str:
        return (
            "Branch(branch_id=%d, name=%s, address=%s, city=%s, state=%s, zip=%s)"
            % (
                self.branch_id,
                self.name,
                self.address if self.address is not None else "",
                self.city if self.city is not None else "",
                self.state if self.state is not None else "",
                self.zip if self.zip is not None else "",
            )
        )
