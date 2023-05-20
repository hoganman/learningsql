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
    """A customer in the schema
    create table account
 (account_id integer unsigned not null auto_increment,
  product_cd varchar(10) not null,
  cust_id integer unsigned not null,
  open_date date not null,
  close_date date,
  last_activity_date date,
  status enum('ACTIVE','CLOSED','FROZEN'),
  open_branch_id smallint unsigned,
  open_emp_id smallint unsigned,
  avail_balance float(10,2),
  pending_balance float(10,2),
  constraint fk_product_cd foreign key (product_cd)
    references product (product_cd),
  constraint fk_a_cust_id foreign key (cust_id)
    references customer (cust_id),
  constraint fk_a_branch_id foreign key (open_branch_id)
    references branch (branch_id),
  constraint fk_a_emp_id foreign key (open_emp_id)
    references employee (emp_id),
  constraint pk_account primary key (account_id)
 );
    """

    __tablename__: Final[str] = "account"

    account_id: Mapped[int] = mapped_column(primary_key=True)

    product_cd: Mapped[str] = mapped_column(ForeignKey("product.product_cd"), nullable=False)

    cust_id: Mapped[int] = mapped_column(ForeignKey("customer.cust_id"), nullable=False)

    open_date: Mapped[date] = mapped_column(Date, nullable=False)
    """Open date of the account, non-nullable"""

    close_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    """Close date of the account, nullable if not closed"""

    last_activity_date: Mapped[Optional[date]] = mapped_column(Date, nullable=True)
    """Last activity date of the account, nullable means use open date"""

    status: Mapped[Optional[str]] = mapped_column(Enum(AccountStatusEnum), nullable=True)

    open_emp_id: Mapped[Optional[int]] = mapped_column(ForeignKey("employee.emp_id"), nullable=True)

    open_branch_id: Mapped[Optional[int]] = mapped_column(ForeignKey("branch.branch_id"), nullable=True)

    avail_balance: Mapped[Optional[float]] = mapped_column(Float(precision=10), nullable=True)

    pending_balance: Mapped[Optional[float]] = mapped_column(Float(precision=10), nullable=True)
