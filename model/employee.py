"""An employee in a department model"""
from datetime import date
from typing import Final, Optional, List

from sqlalchemy import String, Date, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from .base import Base


class Employee(Base):
    """An employee of the company"""

    __tablename__: Final[str] = "employee"

    emp_id: Mapped[int] = mapped_column(primary_key=True)
    """Employee ID, primary key"""

    fname: Mapped[str] = mapped_column(String(20), nullable=False)
    """First name of the employee, non-nullable"""

    lname: Mapped[str] = mapped_column(String(20), nullable=False)
    """Last name of the employee, non-nullable"""

    start_date: Mapped[date] = mapped_column(Date, nullable=False)
    """Start date of the employee, non-nullable"""

    end_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    """End date of the employee, nullable if still employed"""

    superior_emp_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("employee.emp_id"), nullable=True
    )
    """Superior officer primary key as a foreign key, nullable if no superior"""

    dept_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("department.dept_id"), nullable=True
    )
    """Department of the employee as a foreign key, nullable if no department"""

    title: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    """Title of the employee, nullable if no title"""

    assigned_branch_id: Mapped[Optional[int]] = mapped_column(
        ForeignKey("branch.branch_id"), nullable=True
    )
    """Assigned branch ID of the employee as a foreign key, nullable if no assigned branch"""

    superior_emp: Mapped[Optional["Employee"]] = relationship(
        "Employee", remote_side=[emp_id]
    )
    """Adjacency relationship that accesses the superior (Employee) of the employee"""

    employee_dept: Mapped[Optional["Department"]] = relationship(
        "Department", back_populates="dept_employees"
    )
    """Relationship that accesses the assigned department of the employee"""

    employee_branch: Mapped[List["Branch"]] = relationship(
        "Branch", back_populates="branch_employees"
    )
    """Relationship that accesses the assigned branch of the employee"""

    def __repr__(self) -> str:
        return (
            "Employee(emp_id=%d, fname=%s, lname=%s, start_date=%s, end_date=%s, superior_emp_id=%s, dept_id=%s,"
            " title=%s, assigned_branch_id=%s)"
            % (
                self.emp_id,
                self.fname,
                self.lname,
                self.start_date.isoformat(),
                self.end_date.isoformat() if self.end_date is not None else "",
                str(self.superior_emp_id) if self.superior_emp_id is not None else "",
                str(self.dept_id) if self.dept_id is not None else "",
                str(self.title) if self.title is not None else "",
                str(self.assigned_branch_id)
                if self.assigned_branch_id is not None
                else "",
            )
        )
