"""A department consisting with a name"""
from typing import Final, List

from sqlalchemy import String
from sqlalchemy.orm import Mapped, relationship, mapped_column

from .base import Base


class Department(Base):
    """A department with a name"""

    __tablename__: Final[str] = "department"

    dept_id: Mapped[int] = mapped_column(primary_key=True)
    """Department ID, primary key"""

    name: Mapped[str] = mapped_column(String(20), nullable=False)
    """Name of the department, non-nullable"""

    dept_employees: Mapped[List["Employee"]] = relationship(
        "Employee", back_populates="employee_dept"
    )
    """Relationship that lists all employees to the department"""

    def __repr__(self) -> str:
        return "Department(id=%d, name=%s)" % (self.dept_id, self.name)
